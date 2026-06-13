# Weekly Progress Report (Week 4 Status Update)
**Project Title**: Automating Ocular Tracking in Phantom Array Psychophysics & Pupillometry Bistability Analysis
**Joint Research Collaboration**: Tokai Data Science and Brain Lab (Tokai University) & King Mongkut's Institute of Technology Ladkrabang (KMITL)
**Date**: June 13, 2026 (Saturday Update)
**Prepared by**: Jirayu Kaewsing & Research Assistant Team

---

## 1. Executive Summary
This report outlines the experimental design, physiological rationales, active development achievements, and physical lab recordings during Week 4 (June 8 – June 13, 2026) of the collaborative internship. Week 4 has marked major breakthroughs across both the **Phantom Array Experiment (PAE) Slower Frequency Protocol** and the newly initiated **Blue Duty Cycle Pupil Study**.

Following the successful acquisition of high-density visual EEG data from subject `Takahira` during Lab Day 1 (Wednesday, June 10, 2026)—targeting the conscious Phantom Array visual thresholds (**0 Hz, 80 Hz, 160 Hz, 300 Hz, 500 Hz, and 1000 Hz**) under dual chromatic background configurations (with/without a green LED)—Lab Day 2 (Thursday, June 11, 2026) realized the complete physical execution of the pupillary pilot recordings. The **Blue Duty Cycle Pupil Experiment** was run on the EyeLink 1000 Plus across three distinct stimulus temporal duty cycles (**25%, 50%, and 75%**), providing high-fidelity raw ocular tracking and pupillary dynamics.

In parallel with physical data acquisition, the computational infrastructure has been substantially expanded and deployed for joint laboratory use. A standalone command-line parser (`parse_asc.py`) with interactive user path routing was finalized to replace legacy Excel/VBA workflows. Furthermore, an online, zero-configuration Google Colab notebook variant (`colab_parsing_and_interpolation.ipynb`) was deployed to enable cross-platform, browser-based analysis. This pipeline incorporates a custom sliding-window blink mask and Piecewise Cubic Hermite Interpolating Polynomial (`pchip`) interpolation, which cleanly recovers pupillary traces from transient blink dropouts without generating overshoot artifacts. To support rapid training across international partners, complete bilingual documentation and setup instructions have been integrated into the repository in both English and Japanese. Finally, automated EOG-based saccade detection and EEGLAB event-mapping routines (`detect_saccades.py`) have been successfully validated on Takahira's EEG dataset, establishing a unified bridge between rapid eye movements and occipital cortical potentials.

Furthermore, on Lab Day 3 (Saturday, June 13, 2026), the computational preprocessing pipeline was substantially optimized and expanded. Major upgrades to the EyeLink parser and Colab notebook were completed, including advanced button-event cutoff mechanisms for automatic session cropping, dynamic standard pulse duration calculations based on median filters, and redundant/unrelated event filtering. Additionally, a dedicated statistical evaluation framework (`statistical_evaluation.ipynb`) was developed and validated, which calculates key physiological parameters (Baseline Pupil Size, Normalized Constriction, Early and Late Area Under the Curve (AUC), and 6s Post-Illumination Pupillary Response (PIPR)) and generates multi-panel verification plots with AUC visualization overlays. These tools were successfully executed on the newly acquired physical pupillary datasets, extracting clear, robust physiological indices to model the temporal integration of blue-light pupillary constriction and ipRGC-driven melanopsin bistability.

---

## 2. Progress Details

### Week 4 (June 8 – June 13, 2026): Phantom Array Slower Frequency Recordings & Pupil Study Script Optimization

*   **Wednesday, June 10, 2026 (Lab Day 1)**:
    *   **High-Density EEG Recording (Slower Frequency PAE)**: Successfully recorded high-density visual EEG data from subject Takahira using the TOKAI Orb headband system (1000 Hz sampling rate, Queen's Square occipital montage: PO7, O1, Oz, O2, PO8). The session completed testing across a comprehensive array of slower stimulus frequencies: **0 Hz (control), 80 Hz, 160 Hz, 300 Hz, 500 Hz, and 1000 Hz**. These slower frequencies lie close to visual saccadic thresholds, offering a high likelihood of triggering the conscious Phantom Array Effect. Each frequency was tested across two background illumination profiles: **with and without green LED** background. In addition, we successfully recorded trials using the **Lambda variant** visual stimulation.
*   **Thursday, June 11, 2026 (Lab Day 2)**:
    *   **Physical EyeLink 1000 Plus Pupil Recording**: Completed the physical execution of the Blue Duty Cycle Pupil Experiment pilot. High-fidelity pupil diameter and gaze coordinate data were acquired during 1 Hz blue LED flicker stimulation (50 cd/m²) across 25%, 50%, and 75% duty cycles, following the standardized 15-minute mesopic twilight adaptation protocol.
    *   **Interactive Command-Line Parser Deployment**: Upgraded the core Python preprocessing engine (`parse_asc.py`) with user-friendly, interactive path configurations. The parser converts ASCII exports from EyeLink into high-density pandas DataFrames. It automatically extracts EyeLink timestamps, computes relative elapsed time metrics (milliseconds and seconds), maps button-event transitions to synchronize stimulus state triggers (`blue_active`), and logs monocular raw pupil diameters and gaze coordinates.
    *   **Google Colab Pipeline Integration**: Developed and released `colab_parsing_and_interpolation.ipynb`, a cloud-compatible version of the EyeLink pipeline designed to enable zero-setup execution. The notebook implements an advanced sliding-window mask to identify blink intervals (default `SLIDING_WINDOW_SIZE` of 200 ms) and reconstructs missing ocular segments using Piecewise Cubic Hermite Interpolating Polynomial (`pchip`) interpolation. It provides interactive parameters for threshold tuning, includes high-resolution matplotlib visual verification plots overlaying raw and PCHIP-cleaned traces with stimulus-shaded bands, and triggers automatic multi-format (CSV and Excel) data exports.
    *   **Bilingual Setup & Deployment Documentation**: Configured a complete operational framework with bilingual step-by-step guides. The English guide (`docs/en/google_colab_setup.md`) and Japanese guide (`docs/jp/Google_Colab_セットアップガイド.md`) instruct researchers on importing the Colab workspace, adjusting window-size thresholds to avoid blink transition artifacts, verifying interpolation curves, and parsing output structures.
    *   **Automated Saccade Detection on EEG Datasets**: Executed and validated the automated saccade-detection pipeline (`detect_saccades.py`) on subject Takahira's visual EEG dataset. The algorithm processes raw EOG channels through a 30 Hz low-pass filter, calculates velocity dynamics, and subjects candidate peaks to six rigorous quality gates (velocity outliers, EOG step amplitude, EEG overlap artifact checks, single-peak velocity contours, post-saccade fixation stability, and waveform monotonicity). Passing events are exported into a MATLAB-compatible command script (`add_saccade_events.m`) to automatically inject precise 'Saccade' latency markers into EEGLAB, synchronizing saccadic onset with occipital cortical potentials.
*   **Saturday, June 13, 2026 (Lab Day 3)**:
    *   **Automated Button-Event Cutoff and Upgraded Cutoff Detection**: Upgraded both the local preprocessor script (`parse_asc.py`) and the interactive Google Colab notebook (`colab_parsing_and_interpolation.ipynb`) with an automated button-event cutoff algorithm. This algorithm dynamically determines standard active pulse durations (by computing the median duration of all completed pulses in the active file, filtering out startup noise) and automatically inserts off-events for any on-event that lacks one (e.g., when a session terminates mid-flicker or during tracking loss). This prevents trailing artifacts and ensures precise session cropping.
    *   **Event Filtering and Deduplication Optimization**: Re-engineered the preprocessing parser to explicitly filter out unrelated EyeLink diagnostic events (e.g., sample-rate queries and text annotations) and deduplicate overlapping input/button events. Hardware-based `BUTTON` events are prioritized over software `INPUT` signals occurring at identical millisecond timestamps, ensuring absolute tracking of the stimulus trigger (`blue_active`).
    *   **Data Streamlining and Visualization Upgrades**: Streamlined data structures by removing obsolete gaze coordinate columns (`gaze_x`, `gaze_y`) across standard setup guides and Colab templates, focusing exclusively on high-density monocular pupillary sizes to minimize footprint. Integrated a raw pupil size tracking plot as a crucial initial data sanity check, and adjusted legend positioning to the lower-right area to prevent obscuring early-stage pupillary constriction trajectories.
    *   **Statistical Evaluation and Modeling Framework**: Developed and integrated a dedicated statistical evaluation notebook (`statistical_evaluation.ipynb`) defining five core mathematical metrics:
        1. *Baseline Pupil Diameter ($A_{base}$)*: Calculated as the median pupil size over the 1.5-second pre-stimulus baseline window to avoid transient noise/blink artifacts.
        2. *Normalized Pupil Constriction Ratio*: Converts raw pupil sizes into a dimensionless constriction ratio relative to baseline: $NormalizedConstriction_t = \frac{A_{base} - A_t}{A_{base}}$.
        3. *Early Area Under the Curve (Early AUC, 0–6s)*: Trapezoidal integration of normalized constriction from stimulus offset to 6s, capturing the transition of cone/rod decay and early melanopsin activation.
        4. *Late Area Under the Curve (Late AUC, 6–12s)*: Trapezoidal integration from 6 to 12s post-stimulus offset, purely isolating sustained ipRGC-driven melanopsin activity.
        5. *6s PIPR (Post-Illumination Pupillary Response)*: Normalized constriction at exactly 6s after stimulus offset.
    *   **Dataset Validation and Metric Export**: Successfully executed and validated the statistical evaluation framework on physical pupillary datasets, processing both baseline comparative files (`20260507.shimizu_B56_750d_cleaned.csv`) and the newly recorded June 11 pilot run (`260611_cleaned.csv`). The script generated high-resolution, multi-panel diagnostic plots (incorporating baseline, stimulus, and AUC window shading with overlaid AUC plot on top) and exported structured summary tables (`statistical_evaluation_summary.csv` and `.xlsx`). For the June 11 pilot, the computed parameters were: Baseline ($A_{base}$) = 11,414.0, Early AUC = 1.117, Late AUC = 0.400, and 6s PIPR = 0.0956 (~9.56% constriction), providing the first quantitative benchmarks for the blue duty-cycle study.

---

## 3. Experimental Design & Rationale (Week 4 Protocols)

### 3.1. Phantom Array Slower Frequency Protocol (Executed June 10, 2026)
This protocol investigates the visual thresholds and electrophysiological signatures of the Phantom Array Effect under slower, highly perceptible temporal light modulations.

*   **Slower Frequency Selection (0, 80, 160, 300, 500, 1000 Hz):**
    *   *Saccadic Visual Thresholds:* Traditional high-frequency flicker (e.g., above 1000 Hz) is completely fused by the human visual system under steady fixation. However, during rapid eye movements (saccades), the spatial displacement of light on the retina can break this temporal fusion, giving rise to the Phantom Array Effect (PAE)—the perception of discrete, duplicated spatial patterns. Slower frequencies (especially 80 Hz and 160 Hz) are highly prone to triggering this effect because they sit closer to the eye's temporal integration limits. Recording up to 1000 Hz enables us to map the precise threshold curve where the visual cortex transitions from perisaccadic breakthrough back to complete visual suppression.
*   **Green LED Background Conditions (With/Without):**
    *   *Chromatic Retinal Modulation:* Recording with and without a steady green LED background allows us to study how ambient chromatic light interacts with the occipital cortical representation (specifically the 40–100 Hz high-gamma band in the Oz channel). Green background light is hypothesized to stabilize baseline photoreceptor activity and alter the contrast threshold of the visual pathways, potentially modulating the intensity and perisaccadic breakthrough of the phantom array perception.
*   **Lambda Variant Visual Stimulation:**
    *   *Saccadic-Linked Potentials:* The Lambda variant introduces specialized temporal frequency modulations linked to specific saccade profiles. This helps us isolate the visual "Lambda wave" (a positive post-saccadic potential generated in the visual cortex in response to the shift of a patterned image across the retina) and evaluate how temporal light modulation alters these automatic cortical potentials.

### 3.2. Blue Duty Cycle Pupil Protocol (Executed June 11, 2026)
This protocol investigates the light-response and temporal integration characteristics of intrinsically photosensitive retinal ganglion cells (ipRGCs) under blue flickering light using the Pupillary Light Reflex (PLR) as a physiological marker.

*   **Visual Stimulation Parameters:** Blue flickering light modulated at a frequency of **1 Hz** with a luminance of **50 cd/m²** tested at three distinct duty cycles: **25%, 50%, and 75%** (delivered in 25% equal steps).
    *   *Temporal Summation Analysis:* This setup is designed to evaluate how the pupil's constriction rate and Post-Illumination Pupillary Response (PIPR) scale relative to the light energy exposure time. This allows us to statistically model the temporal summation dynamics of the ipRGC pathway and evaluate if the response behaves linearly or exhibits saturation (plateauing) between 50% and 75%.
*   **Environmental and Physical Setup:**
    *   *Twilight Adaptation (Mesopic Adaptation):* Standardized at exactly **15 minutes** prior to stimulation to stabilize baseline light adaptation without inducing sleepiness-induced miosis.
    *   *Ambient Room Brightness:* Regulated at a background illumination of **16.1 lux** inside the shielded recording room to stabilize baseline pupil size, temper retinal sensitivity, and prevent discomfort glare.
    *   *Physical Distance & Visual Angle:* Fixed viewing distance of exactly **57.3 cm** from the monitor screen to the participant's eyes, making calculations mathematically convenient ($1\text{ cm} \approx 1^\circ$).

---

## 4. Standardized EyeLink 1000 Plus Optimization Protocol (Executed June 11, 2026)
To guarantee low-noise, reproducible pupil and gaze records during the physical runs, the following procedures have been standardized:

*   **5-Point Grid Calibration:** Configured with randomized target order, a **1000 ms auto-trigger pace**, and a manual trigger delay of **0.5 to 1.0 second** to allow post-saccadic micro-oscillations to settle.
*   **Strict Validation Cut-offs:** Average Error < 0.5° and Maximum Error < 1.0°. Immediate recalibration is performed if results return "FAIR" or "POOR".
*   **Pupil Center Shift Mitigation:** Calibration screen background RGB values are programmed to match the actual experiment background RGB values exactly.
*   **Camera Tuning:** Standard Pupil-CR tracking in Centroid mode. Pupil thresholds maintained between **75 and 115** and Corneal Reflection (CR) thresholds kept below **240**.

---

## 5. Summary of Week 4 Experimental Parameters

### 5.1. Slower Frequency Phantom Array Experiment (Executed June 10, 2026)

| Parameter | Setting / Value | Physiological / Technical Rationale |
|:---|:---|:---|
| **Stimulus Frequency** | 0 (DC control), 80, 160, 300, 500, and 1000 Hz | Target visual thresholds close to saccadic temporal integration limits |
| **Stimulus Intensity** | Standard visual patterns, with and without Green LED | Evaluate chromatic background modulation of visual cortex pathways |
| **Stimulus Modality** | Saccadic displacement + experimental Lambda variant | Assess perisaccadic visual breakthrough and saccadic-linked potentials |
| **Adaptation Period** | Standard pre-run room adaptation | Rest and stabilize the baseline occipital cortex state before recording |
| **Ambient Background** | Fixed ambient dim light environment | Standardize recording room baseline and prevent contrast sensitivity drift |
| **Viewing Distance** | 57.3 cm | Mathematically convenient visual angle scaling ($1\text{ cm} \approx 1^\circ$) |
| **Sampling Rate** | 1000 Hz (EEG TOKAI Orb) | Capture millisecond-level EEG visual cortical potentials (Oz channel) |
| **EEG Montage** | Occipital Queen's Square (PO7, O1, Oz, O2, PO8) | High spatial-temporal isolation of primary visual cortex activity |
| **Calibration Mode** | Saccadic tracking task calibration | Ensure high spatial accuracy of rapid ocular displacement tracking |

### 5.2. Blue Duty Cycle Pupil Experiment (Executed June 11, 2026)

| Parameter | Setting / Value | Physiological / Technical Rationale |
|:---|:---|:---|
| **Stimulus Frequency** | 1 Hz flicker | Capture transient PLR and steady-state PIPR kinetics |
| **Stimulus Intensity** | 50 cd/m² (Blue LED / Display) | Prevent discomfort glare and associated blink-induced data loss |
| **Stimulus Modality** | 25%, 50%, and 75% Duty Cycles | Evaluate non-linear temporal summation and ipRGC pathway saturation |
| **Adaptation Period** | 15 minutes (Mesopic Twilight adaptation) | Balance retinal light adaptation with prevention of sleepiness-induced miosis |
| **Ambient Background** | 16.1 lux | Prevent sleepiness, stabilize baseline pupil size, and temper retinal sensitivity |
| **Viewing Distance** | 57.3 cm | Mathematically convenient visual angle scaling ($1\text{ cm} \approx 1^\circ$) |
| **Sampling Rate** | 1000 Hz (EyeLink 1000 Plus) | High-resolution capture of pupillary constriction and recovery slopes |
| **Tracking System** | EyeLink 1000 Plus (Pupil-CR Centroid mode) | Ensure lowest noise floor for stable pupillary tracking |
| **Calibration Mode** | 5-Point Grid Calibration (Avg < 0.5°, Max < 1.0°) | High clinical-grade spatial verification cutoffs |

---

## 6. Planned Deliverables for Week 4
1.  **Slower Frequency PAE Analysis (Completed June 10):** Successfully completed EEG recordings for 0, 80, 160, 300, 500, and 1000 Hz (with/without Green LED + Lambda variant) for subject Takahira. The next step is to run ERSP time-frequency analyses to extract occipital gamma-band features across these conditions.
2.  **Pupil Study Script Deployment (Completed June 10):** Preprocessor pipeline (`eyelink-1000Hz.ipynb`), artifact rejection algorithms (`eda.ipynb`), and standard protocol (`blue_duty_cycle_pupil_protocol.md`) are fully deployed.
3.  **Saccade Detection & Dataset Verification (Completed June 11):** Ran the automated EOG saccade detection script (`detect_saccades.py`) on subject Takahira's slower-frequency EEG dataset and generated seamless MATLAB/EEGLAB trial events (`add_saccade_events.m`).
4.  **Pupil Pilot Recording & Interactive Pipeline Deployment (Completed June 11):** Successfully executed physical pilot recordings on the EyeLink 1000 Plus under the 25%, 50%, and 75% blue duty cycle conditions, and delivered the interactive Python-based parser (`parse_asc.py`), Google Colab notebook (`colab_parsing_and_interpolation.ipynb`), and bilingual step-by-step documentation (`docs/en/google_colab_setup.md` / `docs/jp/Google_Colab_セットアップガイド.md`).
5.  **Statistical Evaluation & Feature Extraction Pipeline (Completed June 13):** Released a fully automated statistical evaluation notebook (`statistical_evaluation.ipynb`) to compute baseline pupil sizes, normalized constriction, 6s PIPR, and early/late AUC values. Validated the engine on real physical datasets, producing multi-panel diagnostic plots and exporting standard `.xlsx` and `.csv` summary reports for statistical comparisons.
6.  **Integrated Pupillary-Cortical Modeling (Ongoing):** Combine the completed slower-frequency EEG datasets with the pupil pilot datasets to model perisaccadic cortical suppression and pupil temporal integration kinetics.
