# Weekly Progress Report (Week 1 Status Update)
**Project Title**: Automating Ocular Tracking in Phantom Array Psychophysics & Pupillometry Bistability Analysis
**Joint Research Collaboration**: Tokai Data Science and Brain Lab (Tokai University) & King Mongkut's Institute of Technology Ladkrabang (KMITL)
**Date**: May 16, 2026
**Prepared by**: Jirayu Kaewsing & Research Assistant Team

---

## 1. Executive Summary
This report summarizes the research and development progress achieved during Week 1 of the collaborative project. The primary focus of this initial week was establishing repository architecture, defining the automated EOG-based saccade detection pipeline specification, and initializing stimulus conditions for the Blue/Green LED Flash Experiment.

---

## 2. Progress Details

### Week 1 (May 11 – May 16, 2026): Repository Initialization & Pipeline Specification
*   **Version Control & Repository Architecture**: Reinitialized the core repository structure to manage source code (`src/python/`), documentation (`docs/`), raw datasets (`data/`), and generated outputs (`out/`) under unified Git control.
*   **Saccade Pipeline Specification**: Authored technical guidelines and physiological rationales for replacing the manual EEGLAB scoring workflow with an automated EOG-based saccade detection script.
*   **Bistability Experiment Setup**: Established stimulus conditions for the Blue/Green LED Flash Experiment. Configured three distinct luminance pairings (Low green: 50/20 cd/m², Equal: 50/50 cd/m², and High green: 50/80 cd/m²) designed to isolate the modulating effect of green (medium-wavelength) light on melanopsin regeneration.
