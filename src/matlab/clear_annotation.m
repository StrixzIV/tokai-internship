% 1. Empty the event structure
EEG.event = [];

% 2. Check and update the dataset consistency (Crucial step!)
EEG = eeg_checkset(EEG);

% 3. Update the EEGLAB GUI to reflect the changes
[ALLEEG, EEG, CURRENTSET] = eeg_store(ALLEEG, EEG, CURRENTSET);
eeglab redraw;