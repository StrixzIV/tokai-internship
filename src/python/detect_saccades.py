import mne
import numpy as np
from scipy.signal import find_peaks

def detect_saccades(data_path, output_matlab_path, threshold_z=1.5, min_distance_ms=250):
    """
    Detects Saccades from an EOG channel using velocity thresholding and rigorous quality gates.
    """
    print(f"Loading data from {data_path}...")
    raw = mne.io.read_raw_eeglab(data_path, preload=True)
    
    if 'EOG' not in raw.ch_names:
        print("Error: EOG channel not found.")
        return
    
    sfreq = raw.info['sfreq']
    
    # Isolate EOG
    eog_ch = raw.copy().pick_channels(['EOG'])
    eog_ch.filter(l_freq=0.5, h_freq=30.0, fir_design='firwin')
    eog_data = eog_ch.get_data()[0]
    
    # Isolate EEG channels for overlap/artifact checking
    eeg_channels = [ch for ch in raw.ch_names if ch != 'EOG']
    eeg_raw = raw.copy().pick_channels(eeg_channels)
    eeg_raw.filter(l_freq=0.5, h_freq=30.0, fir_design='firwin')
    eeg_data = eeg_raw.get_data()
    
    # 2. Compute velocity (derivative)
    velocity = np.diff(eog_data) * sfreq
    velocity = np.insert(velocity, 0, 0)
    
    # 3. Compute threshold
    abs_velocity = np.abs(velocity)
    mean_vel = np.mean(abs_velocity)
    std_vel = np.std(abs_velocity)
    threshold = mean_vel + threshold_z * std_vel
    
    print(f"Computed velocity threshold: {threshold:.5f} (Z={threshold_z})")
    
    # 4. Find candidate peaks in absolute velocity
    min_dist_samples = int((min_distance_ms / 1000.0) * sfreq)
    candidate_peaks, _ = find_peaks(abs_velocity, height=threshold, distance=min_dist_samples)
    
    print(f"Detected {len(candidate_peaks)} putative Saccade events.")
    
    # 5. Apply Quality Gates for Noise Rejection
    valid_peaks = []
    
    global_eog_std = np.std(eog_data)
    
    # Pre-compute IQR and Median for Velocity Outlier Check
    if len(candidate_peaks) > 0:
        peak_vels = abs_velocity[candidate_peaks]
        q1 = np.percentile(peak_vels, 25)
        q3 = np.percentile(peak_vels, 75)
        iqr = q3 - q1
        median_vel = np.median(peak_vels)
        outlier_threshold = median_vel + 3 * iqr

    else:
        outlier_threshold = np.inf
        
    for peak in candidate_peaks:

        # Gate 4: Velocity Outlier Check (Global)
        if abs_velocity[peak] > outlier_threshold:
            continue
            
        # Gate 6: Minimum Step Amplitude Check (Microsaccade Rejection)
        win_mean = int(0.15 * sfreq) # 150 ms window
        gap = int(0.02 * sfreq) # 20 ms gap from peak to avoid the transition
        
        pre_start = max(0, peak - win_mean - gap)
        pre_end = max(0, peak - gap)
        pre_mean = np.mean(eog_data[pre_start:pre_end]) if pre_start < pre_end else 0
        
        post_start = min(len(eog_data), peak + gap)
        post_end = min(len(eog_data), peak + win_mean + gap)
        post_mean = np.mean(eog_data[post_start:post_end]) if post_start < post_end else 0
        
        step_amp = abs(post_mean - pre_mean)
        if step_amp < 0.000130: # 130 µV
            continue
        
        # Gate 5: EEG Overlap / Artifact Check
        win_overlap_start = int(0.1 * sfreq)
        win_overlap_end = int(0.3 * sfreq)
        start_eeg = max(0, peak - win_overlap_start)
        end_eeg = min(eeg_data.shape[1], peak + win_overlap_end)
        
        ptp_per_chan = np.ptp(eeg_data[:, start_eeg:end_eeg], axis=1)
        max_eeg_ptp = np.max(ptp_per_chan) if len(ptp_per_chan) > 0 else 0
        
        if max_eeg_ptp > 0.000110:
            continue
            
        # Gate 1: Single-Peak Velocity Shape (±100 ms window)
        win_100ms = int(0.1 * sfreq)
        start_idx = max(0, peak - win_100ms)
        end_idx = min(len(abs_velocity), peak + win_100ms)
        window_vel = abs_velocity[start_idx:end_idx]
        primary_height = abs_velocity[peak]
        
        local_peaks, _ = find_peaks(window_vel, prominence=0.4 * primary_height)
        secondary_too_high = False
        
        for lp in local_peaks:
            global_lp = start_idx + lp
            if abs(global_lp - peak) > 2:
                secondary_too_high = True
                break
                
        if secondary_too_high:
            continue
            
        # Gate 2: Post-Saccade Fixation Stability (200 ms post-peak window)
        win_200ms = int(0.2 * sfreq)
        end_idx_200 = min(len(eog_data), peak + win_200ms)
        post_eog_window = eog_data[peak:end_idx_200]
        
        if np.std(post_eog_window) >= 1.5 * global_eog_std:
            continue
            
        # Gate 3: Waveform Monotonicity of the Ramp (300 ms post-peak window)
        win_300ms = int(0.3 * sfreq)
        end_idx_300 = min(len(velocity), peak + win_300ms)
        post_vel_window = velocity[peak:end_idx_300]
        
        kernel = np.ones(25) / 25.0
        smooth_vel = np.convolve(post_vel_window, kernel, mode='valid')
        
        deadband = 0.05 * primary_height
        smooth_vel[np.abs(smooth_vel) < deadband] = 0
        
        non_zero_vel = smooth_vel[smooth_vel != 0]
        if len(non_zero_vel) > 0:
            sign_changes = np.sum(np.diff(np.sign(non_zero_vel)) != 0)
        else:
            sign_changes = 0
            
        if sign_changes > 4:
            continue
            
        # Add to valid peaks if all gates pass
        valid_peaks.append(peak)
        
    print(f"After quality gates, {len(valid_peaks)} valid Saccades remain.")
    
    # 6. Generate MATLAB script
    print(f"Saving MATLAB script to {output_matlab_path}...")
    with open(output_matlab_path, 'w') as f:
        f.write("% Saccade events auto-generated from Python script\n")
        f.write("% Copy and run these commands in MATLAB after loading your EEG dataset (EEG variable)\n\n")
        
        for p in valid_peaks:
            time = p / sfreq
            f.write(f"EEG.event(end+1).type = 'Saccade'; EEG.event(end).latency = {time:.4f} * EEG.srate;\n")
            
        f.write("\n% Check for consistency and re-sort events by latency\n")
        f.write("EEG = eeg_checkset(EEG, 'eventconsistency');\n")
        f.write("% Plot to verify\n")
        f.write("% eegplot(EEG.data, 'events', EEG.event);\n")
        
    print("Done!")

if __name__ == "__main__":

    data_file = input("Enter the path to the data file: ")
    out_file = input("Enter the output path: ")
    
    detect_saccades(data_file, out_file, threshold_z=2.0)
