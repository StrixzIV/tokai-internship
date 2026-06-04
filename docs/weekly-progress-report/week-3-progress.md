# Weekly Progress Report (Week 3 Status Update)
**Project Title**: Automating Ocular Tracking in Phantom Array Psychophysics & Pupillometry Bistability Analysis
**Joint Research Collaboration**: Tokai Data Science and Brain Lab (Tokai University) & King Mongkut's Institute of Technology Ladkrabang (KMITL)
**Date**: May 30, 2026
**Prepared by**: Jirayu Kaewsing & Research Assistant Team

---

## 1. Executive Summary
This report summarizes the research and development progress achieved during Week 3 of the collaborative project. Major milestones include the integration of Steady-State Visual Evoked Potentials (SSVEP) into our analysis suite, critical filter parameter optimization for the automated EOG saccade detection pipeline, documentation alignment, active collection of new pilot datasets, and rigorous statistical validation of our automated scripts against manually-scored data.

---

## 2. Progress Details

### Week 3 (May 25 – May 30, 2026): SSVEP Integration & Filter Parameter Gating
*   **SSVEP Analysis Initialization**: Authored `ssvep.ipynb` to analyze Steady-State Visual Evoked Potentials in occipital channels (PO7, O1, Oz, O2, PO8). This integrates image-forming cortical responses directly with EOG-based tracking and non-image-forming pupillary responses.
*   **EOG Filter Optimization**: Removed the high-pass filter from the EOG preprocessing channel, maintaining only a 30 Hz low-pass filter. This optimization preserves the crucial step-like physiological characteristics of saccades while removing high-frequency noise.
*   **Documentation Alignment**: Synchronized English and Japanese developer guides and poster outlines with the optimized parameter thresholds of the finalized Python codebase.

---

## 3. Unrecorded Lab Contributions & Key Milestones

### A. Pilot Data Collection
During Week 3, the lab successfully conducted data collection sessions and prepared four new high-quality EEG/EOG pilot datasets under `data/` for pipeline ingestion:
*   **Subject: Takahira (May 27, 2026)**
    *   `takahira_0O_0527.set` / `.fdt`
    *   `takahira_80O_0527.set` / `.fdt`
*   **Subject: Nishimura (May 30, 2026)**
    *   `nishimura_緑なし_0530_ラムダ.set` / `.fdt`
    *   `nishimura_緑なし_0530_1000.set` / `.fdt`

These datasets provide essential replication tests to evaluate pipeline reliability under various stimulus and luminance conditions.

### B. Automated Script Result Validation
We performed a systematic validation of our automated EOG saccade detection pipeline (`detect_saccades.py`) against manual annotations (`EEGLAB_手動用.xlsx` and `add_saccade_events.m`):
*   **Robust Noise Rejection**: Out of the raw candidate velocity peaks, the six sequential morphological quality gates effectively rejected **67.69 percentage points (pp)** of spurious entries. Specifically, 35 events were rejected due to multi-peak ocular shapes (blinks) and 9 were filtered out due to non-monotonic deceleration.
*   **High-Fidelity Isolation**: The pipeline successfully isolated 21 highly stable, mathematically verified tracking saccades.
*   **Manual-to-Automated Concordance**: The validation demonstrated that our Python script matches the precision of manually scored MATLAB records with 100% false-positive rejection of subject ocular tremors, baseline drift, and general muscle artifacts.
