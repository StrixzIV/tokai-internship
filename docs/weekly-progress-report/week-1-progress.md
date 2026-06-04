# Weekly Progress Report (Week 1 Status Update)
**Project Title**: Automating Ocular Tracking in Phantom Array Psychophysics & Pupillometry Bistability Analysis
**Joint Research Collaboration**: Tokai Data Science and Brain Lab (Tokai University) & King Mongkut's Institute of Technology Ladkrabang (KMITL)
**Date**: May 23, 2026
**Prepared by**: Jirayu Kaewsing & Research Assistant Team

---

## 1. Executive Summary
This report summarizes the research and development progress achieved during Week 1 of the collaborative project. Following arrival in Japan on May 18, 2026, the primary achievements of this initial week focused on project repository initialization, version control setup, baseline specifications of the EOG ocular tracking pipeline, stimulus setup for the Blue/Green LED Flash Experiment, blink spline interpolation, temporal sliding window alignment, and porting legacy VBA scripts to Python.

---

## 2. Progress Details

### Week 1 (May 18 – May 23, 2026): Repository Initialization, VBA Code Migration & Pupillometry Spline Interpolation
*   **Repository Initialization & Directory Architecture**: Organized and structured the project directory (`src/python/`, `docs/`, `data/`, `out/`) and successfully initialized Git version control (`1722ab4`, `c3d8efe`).
*   **Ocular Tracking Pipeline Specifications**: Authored developer guidelines and biological rationales for replacing the manual EEGLAB scoring workflow with an automated EOG-based saccade detection script (`16ee110`).
*   **Melanopsin Bistability Stimulus Setup**: Configured stimulus pairings for the Blue/Green LED Flash Experiment (Low green: 50/20 cd/m², Equal: 50/50 cd/m², and High green: 50/80 cd/m²) designed to isolate medium-wavelength light modulation of melanopsin regeneration (`ad46ce0`).
*   **Cubic Spline Interpolation for Pupil Gaps**: Designed and implemented a cubic spline interpolation algorithm within our pupillometry workflow to reconstruct pupil diameter series during eye blink intervals, minimizing transient noise and data loss (`1a76287`).
*   **Sliding Window Temporal Adjustments**: Built dynamic temporal window adjustments to synchronize raw pupil records with the onset and offset of the 1 Hz flickering light stimuli (`ee672dc`).
*   **Legacy Excel VBA to Jupyter Migration**: Replaced legacy, platform-dependent lab Excel VBA parsing scripts with a fully reproducible Jupyter Notebook pipeline (`eda.ipynb` under `src/python/led-flash/`) (`d177446`).
*   **Saccade Marker Alignment & De-duplication**: Refined `detect_saccades.py` to automatically clear pre-existing markers inside EEGLAB prior to appending new ones, avoiding event duplicate spikes across repeated runs, and implemented a **200 µV** EEG overlap rejection threshold to screen out gross body movement noise (`25c7cfc`).
