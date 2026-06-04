# Weekly Progress Report (Week 2 Status Update)
**Project Title**: Automating Ocular Tracking in Phantom Array Psychophysics & Pupillometry Bistability Analysis
**Joint Research Collaboration**: Tokai Data Science and Brain Lab (Tokai University) & King Mongkut's Institute of Technology Ladkrabang (KMITL)
**Date**: May 30, 2026
**Prepared by**: Jirayu Kaewsing & Research Assistant Team

---

## 1. Executive Summary
This report summarizes the research and development progress achieved during Week 2 of the collaborative project. Major milestones include expanding the pipeline with Steady-State Visual Evoked Potentials (SSVEP) analysis, refining EOG signal filtering to preserve physiological saccade steps, and gathering our first set of high-quality pilot EEG/EOG datasets from subjects Takahira and Nishimura.

---

## 2. Progress Details

### Week 2 (May 25 – May 30, 2026): SSVEP Integration, Filter Parameter Optimization & Data Collection
*   **SSVEP Analysis Initialization**: Authored `ssvep.ipynb` to analyze Steady-State Visual Evoked Potentials in occipital channels (PO7, O1, Oz, O2, PO8). This integrates image-forming cortical responses directly with EOG-based tracking and non-image-forming pupillary responses (`e9d4edd`).
*   **EOG Signal Filter Optimization**: Removed the high-pass filter from the EOG preprocessing channel in `detect_saccades.py`, maintaining only a 30 Hz low-pass filter (`53b834a`).
    *   *Scientific Rationale*: Saccadic shifts in EOG signal exhibit slow, step-like deflections. High-pass filtering attenuates or destroys these steps. Keeping only a 30 Hz low-pass filter preserves these essential step characteristics while successfully filtering high-frequency noise and ocular tremors.
*   **Technical Documentation Alignment**: Updated and synchronized English and Japanese developer guides and poster outlines with the optimized parameter thresholds of the finalized Python codebase (`489506a`).

---

## 3. Lab Contributions & Key Milestones

### Pilot Data Collection
The lab successfully conducted data collection sessions and prepared four new high-quality EEG/EOG pilot datasets under `data/` for pipeline ingestion:
*   **Subject: Takahira (May 27, 2026)**
    *   `takahira_0O_0527.set` / `.fdt`
    *   `takahira_80O_0527.set` / `.fdt`
*   **Subject: Nishimura (May 30, 2026)**
    *   `nishimura_緑なし_0530_ラムダ.set` / `.fdt`
    *   `nishimura_緑なし_0530_1000.set` / `.fdt`

These datasets represent crucial replication tests to evaluate and refine our analysis pipelines under multiple green LED stimulus conditions.
