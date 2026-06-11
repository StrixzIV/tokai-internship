#!/usr/bin/env python3
"""
EyeLink ASC File Parser for Pupillometry Experiments
This script extracts timestamps, pupil size, gaze coordinates, and calculates 
elapsed times and stimulus activity (blue_active) based on BUTTON events.
"""

import os
import numpy as np
import pandas as pd

def parse_eyelink_asc(file_path):
    """
    Parses an EyeLink .asc file and returns a pandas DataFrame.
    
    Parameters:
        file_path (str): Path to the EyeLink .asc file.
        
    Returns:
        pd.DataFrame: A DataFrame containing:
            - timestamp: EyeLink recording timestamp (ms)
            - elasped_ms: Elapsed time in milliseconds since the start of recording
            - elasped_sec: Elapsed time in seconds since the start of recording
            - blue_active: Binary indicator (1 if blue LED is active, 0 otherwise)
            - gaze_x: Gaze X position (np.nan for missing/blink data)
            - gaze_y: Gaze Y position (np.nan for missing/blink data)
            - pupil_size: Pupil size / diameter (0.0 for missing/blink data)
    """
    timestamps = []
    gaze_x = []
    gaze_y = []
    pupil_size = []
    button_events = [] # List of tuples: (btn_timestamp, button_id, state)

    print(f"Reading Eyelink ASC file: {file_path}")
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            parts = line.split()
            first_word = parts[0]
            
            # Check if this is a sample line (starts with an integer timestamp)
            try:
                ts = int(first_word)
                timestamps.append(ts)
                
                # Parse gaze X (represented by '.' during blinks/loss)
                if len(parts) > 1:
                    x_val = parts[1]
                    gaze_x.append(np.nan if x_val == "." else float(x_val))
                else:
                    gaze_x.append(np.nan)
                    
                # Parse gaze Y (represented by '.' during blinks/loss)
                if len(parts) > 2:
                    y_val = parts[2]
                    gaze_y.append(np.nan if y_val == "." else float(y_val))
                else:
                    gaze_y.append(np.nan)
                    
                # Parse pupil size / diameter (represented by 0.0 during blinks/loss)
                if len(parts) > 3:
                    pupil_size.append(float(parts[3]))
                else:
                    pupil_size.append(0.0)
                    
            except ValueError:
                # Event line (e.g. MSG, BUTTON, SFIX, etc.)
                if first_word == "BUTTON" and len(parts) >= 4:
                    try:
                        btn_ts = int(parts[1])
                        btn_id = int(parts[2])
                        btn_state = int(parts[3])
                        button_events.append((btn_ts, btn_id, btn_state))
                    except ValueError:
                        pass

    # Sort button events chronologically just in case they appear out of order
    button_events.sort(key=lambda x: x[0])
    
    # Convert samples to numpy arrays
    ts_arr = np.array(timestamps, dtype=np.int64)
    gaze_x_arr = np.array(gaze_x, dtype=np.float64)
    gaze_y_arr = np.array(gaze_y, dtype=np.float64)
    pupil_size_arr = np.array(pupil_size, dtype=np.float64)
    
    # Map button events to samples to check when blue light is active
    # For any sample timestamp T, blue_active is determined by the state of the 
    # latest BUTTON event that occurred on or before T.
    if button_events:
        btn_ts_list, btn_ids, btn_states = zip(*button_events)
        btn_ts_arr = np.array(btn_ts_list, dtype=np.int64)
        btn_states_arr = np.array(btn_states, dtype=np.int64)
        
        # np.searchsorted(btn_ts_arr, ts_arr, side='right') returns the index i 
        # such that btn_ts_arr[i-1] <= ts_arr < btn_ts_arr[i]
        indices = np.searchsorted(btn_ts_arr, ts_arr, side="right") - 1
        
        # Create the state mask: default to 0 for timestamps before the first button event
        blue_active = np.zeros_like(ts_arr, dtype=np.int64)
        valid_mask = (indices >= 0)
        blue_active[valid_mask] = btn_states_arr[indices[valid_mask]]
    else:
        print("Warning: No BUTTON events found in the file.")
        blue_active = np.zeros_like(ts_arr, dtype=np.int64)
        
    # Calculate elapsed_ms and elapsed_sec relative to the first sample timestamp
    if len(ts_arr) > 0:
        start_ts = ts_arr[0]
        elapsed_ms = ts_arr - start_ts
        elapsed_sec = elapsed_ms / 1000.0
    else:
        elapsed_ms = np.array([], dtype=np.int64)
        elapsed_sec = np.array([], dtype=np.float64)
        
    # Build the final output DataFrame with requested column spellings
    df = pd.DataFrame({
        "timestamp": ts_arr,
        "elasped_ms": elapsed_ms,
        "elasped_sec": elapsed_sec,
        "blue_active": blue_active,
        "gaze_x": gaze_x_arr,
        "gaze_y": gaze_y_arr,
        "pupil_size": pupil_size_arr
    })
    
    return df

if __name__ == "__main__":
    # Define default input and output paths
    input_path = "data/260611.asc"
    output_path = "data/260611_parsed.csv"
    
    if os.path.exists(input_path):
        df = parse_eyelink_asc(input_path)
        print(f"Parsing complete. Shape of DataFrame: {df.shape}")
        
        # Save to CSV
        df.to_csv(output_path, index=False)
        print(f"Data saved to {output_path}")
        
        # Print a short summary of the result
        print("\nFirst 5 rows:")
        print(df.head())
        print("\nStimulus Stats:")
        print(f"Total rows: {len(df)}")
        print(f"Blue Active rows: {(df['blue_active'] == 1).sum()} ms")
    else:
        print(f"Error: Could not find input file at {input_path}")
