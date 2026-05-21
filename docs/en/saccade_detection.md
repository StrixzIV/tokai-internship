# Saccade Detection Script Documentation

## Overview
The `detect_saccades.py` script automatically detects saccadic eye movements from an EOG channel within an EEG dataset (stored in EEGLAB `.set`/`.fdt` format). It applies velocity thresholding and a series of rigorous quality gates to filter out noise, outputting the detected events into a MATLAB script that can be used to insert the events back into EEGLAB.

## Requirements
Ensure you have the required dependencies installed. You can install them using:
```bash
pip install mne numpy scipy
```
*(Or by using `pip install -r src/python/requirements.txt` if available)*

## Usage
The script is run from the command line and will prompt you for the input and output paths.

### Running the Script
Execute the script using Python:
```bash
python src/python/detect_saccades.py
```

### Inputs
When prompted, provide the following information:
1. **Data file path**: The path to your input dataset, e.g., `data/80O.set`.
2. **Output path**: The path where you want the output MATLAB script to be saved, e.g., `out/add_saccade_events.m`.

### Output
The script generates a MATLAB `.m` file containing commands to add the detected saccades as events into your loaded `EEG` variable in EEGLAB. 

To use the output in MATLAB:
1. Load your `.set` file into EEGLAB.
2. Open the generated MATLAB script in the MATLAB editor.
3. Run the script. It will append the saccade events to `EEG.event` and check for consistency.

## How It Works
The script performs the following steps:
1. **Loads the dataset**: Reads the EEGLAB dataset using `mne`.
2. **Isolates and Filters**: Extracts the EOG channel and applies a bandpass filter (0.5–30.0 Hz).
3. **Calculates Velocity**: Computes the first derivative of the EOG signal.
4. **Detects Candidates**: Identifies initial saccade candidates based on a velocity threshold (default Z-score = 2.0).
5. **Quality Gates**: Applies strict noise-rejection criteria to each candidate:
   - Velocity outlier check
   - Minimum step amplitude check (rejects microsaccades)
   - EEG artifact overlap check
   - Single-peak velocity shape check
   - Post-saccade fixation stability check
   - Waveform monotonicity check
6. **Exports**: Writes the valid saccade timings to the output MATLAB script.
