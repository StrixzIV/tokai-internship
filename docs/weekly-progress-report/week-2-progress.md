# Weekly Progress Report (Week 2 Status Update)
**Project Title**: Automating Ocular Tracking in Phantom Array Psychophysics & Pupillometry Bistability Analysis
**Joint Research Collaboration**: Tokai Data Science and Brain Lab (Tokai University) & King Mongkut's Institute of Technology Ladkrabang (KMITL)
**Date**: May 23, 2026
**Prepared by**: Jirayu Kaewsing & Research Assistant Team

---

## 1. Executive Summary
This report summarizes the research and development progress achieved during Week 2 of the collaborative project. The major achievements include blink interpolation enhancements in pupillometry, sliding window temporal adjustments, porting legacy Excel VBA parsing code into Jupyter Notebooks, and initial optimization of our automated EOG saccade detection script.

---

## 2. Progress Details

### Week 2 (May 18 – May 23, 2026): Signal Processing Refinements & VBA Code Migration
*   **Pupillometry Blink Interpolation**: Implemented a cubic spline interpolation algorithm to reconstruct pupil diameter series during blink intervals, minimizing transient artifact corruption.
*   **Sliding Window Temporal Adjustments**: Added dynamic sliding window adjustments to align pupil recordings precisely with the onset and offset of the 1 Hz flicker stimuli.
*   **Legacy Code Migration**: Ported legacy Excel VBA data-parsing scripts into an open-source, highly reproducible Jupyter Notebook workflow (`eda.ipynb` under `src/python/led-flash/`).
*   **Saccade Script Optimization**: Updated `detect_saccades.py` to automatically clear pre-existing markers within EEGLAB prior to appending new ones, preventing duplicate event markers during repeated runs. Established an EEG overlap rejection threshold of 200 µV to gate generalized muscular and movement artifacts.
