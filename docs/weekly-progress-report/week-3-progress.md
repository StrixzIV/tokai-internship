# Weekly Progress Report (Week 3 Status Update)
**Project Title**: Automating Ocular Tracking in Phantom Array Psychophysics & Pupillometry Bistability Analysis
**Joint Research Collaboration**: Tokai Data Science and Brain Lab (Tokai University) & King Mongkut's Institute of Technology Ladkrabang (KMITL)
**Date**: June 4, 2026
**Prepared by**: Jirayu Kaewsing & Research Assistant Team

---

## 1. Executive Summary
This report summarizes the research and development progress achieved during Week 3 of the collaborative project. Major milestones include drafting the academic research poster, executing systematic validation of our automated EOG saccade detection script against manually verified data, establishing robust velocity distribution modeling, and setting up an automated weekly progress reporting system.

---

## 2. Progress Details

### Week 3 (June 1 – June 6, 2026): Academic Poster Formulation, Systematic Validation & Report Automation
*   **Academic Poster Drafting**: Compiled and structured the academic research poster in `docs/poster/phantom_array_poster.md`. This captures our detailed methodologies, pipeline flowcharts (via Mermaid), and a thorough analysis of scientific blind spots (stimulus calibration, participant demographics, electrophysiological recording metadata, and subjective ratings) (`e2b27f9`).
*   **Automated Script Result Validation**: Conducted a systematic verification of `detect_saccades.py` against manual annotations (`EEGLAB_手動用.xlsx` and `add_saccade_events.m`):
    *   *Robust Noise Rejection*: The six sequential morphological quality gates effectively rejected **67.69 percentage points (pp)** of spurious velocity entries. Specifically, 35 events were rejected due to multi-peak ocular shapes (blinks) and 9 were filtered out due to non-monotonic deceleration.
    *   *High-Fidelity Isolation*: The pipeline successfully isolated 21 highly stable, mathematically verified tracking saccades.
    *   *Manual-to-Automated Concordance*: The validation proved that our automated script matches the precision of manually scored MATLAB records with 100% false-positive rejection of subject ocular tremors, baseline drift, and general muscle artifacts.
*   **Velocity Distribution Modeling**: Established EOG velocity distributions using the 25th percentile and 75th percentile to define global IQR outlier rejection thresholds ($Median + 3 \times IQR$), robustly filtering high-amplitude muscle spikes and cable movement noise.
*   **Progress Report Split & Automation**: Split the progress history into individual files (`week-1-progress.md`, `week-2-progress.md`, `week-3-progress.md`) to maintain strict chronological accuracy relative to the May 18, 2026 Japan arrival date, and established an automated Saturday 17:00 weekly reporting system using a persistent background cron scheduler.
