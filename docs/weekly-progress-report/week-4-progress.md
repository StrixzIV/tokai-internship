# Weekly Progress Report (Week 4 Status Update)
**Project Title**: Automating Ocular Tracking in Phantom Array Psychophysics & Pupillometry Bistability Analysis
**Joint Research Collaboration**: Tokai Data Science and Brain Lab (Tokai University) & King Mongkut's Institute of Technology Ladkrabang (KMITL)
**Date**: June 10, 2026 (Wednesday Update)
**Prepared by**: Jirayu Kaewsing & Research Assistant Team

---

## 1. Executive Summary
This report outlines the experimental design, physiological rationales, active development achievements, and a critical redirection of physical lab recordings during Week 4 (June 8 – June 13, 2026) of the collaborative internship. While the initial technical focus of Week 4 has been the structural preparation and pipeline optimization for the upcoming **Blue Duty Cycle Pupil Study**, physical pupil recordings scheduled for today were postponed to tomorrow (Thursday, June 11, 2026) due to lab hardware allocation adjustments. 

In response, today's active lab session (Wednesday, June 10, 2026) was successfully dedicated to recording high-density visual EEG data from subject `Takahira` for the **Phantom Array Experiment (PAE) Slower Frequency Protocol**. By focusing on slower temporal light modulations (**0 Hz, 80 Hz, 160 Hz, 300 Hz, 500 Hz, and 1000 Hz**), this session specifically targeted the visual threshold frequencies where there is a high probability of encountering the conscious Phantom Array Effect (PAE). These trials were executed under two background chromatic conditions (**with and without a green LED** background) and included an advanced **Lambda variant** visual stimulation mode.

Concurrently, the computational foundations for the Pupil Study were completed. This includes translating and standardizing the Japanese experimental protocol into English (`docs/en/blue_duty_cycle_pupil_protocol.md`), replacing legacy Excel/VBA scripts with a robust automated Python/pandas preprocessing pipeline, and implementing a sliding-window blink mask combined with Piecewise Cubic Hermite Interpolating Polynomial (`pchip`) interpolation to ensure continuous, low-noise ocular data collection once physical pupil recording commences tomorrow.

---

## 2. Progress Details

### Week 4 (June 8 – June 13, 2026): Phantom Array Slower Frequency Recordings & Pupil Study Script Optimization

*   **Wednesday, June 10, 2026 (Lab Day 1)**:
    *   **High-Density EEG Recording (Slower Frequency PAE)**: Successfully recorded high-density visual EEG data from subject Takahira using the TOKAI Orb headband system (1000 Hz sampling rate, Queen's Square occipital montage: PO7, O1, Oz, O2, PO8). The session completed testing across a comprehensive array of slower stimulus frequencies: **0 Hz (control), 80 Hz, 160 Hz, 300 Hz, 500 Hz, and 1000 Hz**. These slower frequencies lie close to visual saccadic thresholds, offering a high likelihood of triggering the conscious Phantom Array Effect. Each frequency was tested across two background illumination profiles: **with and without green LED** background. In addition, we successfully recorded trials using the **Lambda variant** visual stimulation.

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

### 3.2. Blue Duty Cycle Pupil Protocol (Postponed to June 11, 2026)
This protocol investigates the light-response and temporal integration characteristics of intrinsically photosensitive retinal ganglion cells (ipRGCs) under blue flickering light using the Pupillary Light Reflex (PLR) as a physiological marker.

*   **Visual Stimulation Parameters:** Blue flickering light modulated at a frequency of **1 Hz** with a luminance of **50 cd/m²** tested at three distinct duty cycles: **25%, 50%, and 75%** (delivered in 25% equal steps).
    *   *Temporal Summation Analysis:* This setup is designed to evaluate how the pupil's constriction rate and Post-Illumination Pupillary Response (PIPR) scale relative to the light energy exposure time. This allows us to statistically model the temporal summation dynamics of the ipRGC pathway and evaluate if the response behaves linearly or exhibits saturation (plateauing) between 50% and 75%.
*   **Environmental and Physical Setup:**
    *   *Twilight Adaptation (Mesopic Adaptation):* Standardized at exactly **15 minutes** prior to stimulation to stabilize baseline light adaptation without inducing sleepiness-induced miosis.
    *   *Ambient Room Brightness:* Regulated at a background illumination of **16.1 lux** inside the shielded recording room to stabilize baseline pupil size, temper retinal sensitivity, and prevent discomfort glare.
    *   *Physical Distance & Visual Angle:* Fixed viewing distance of exactly **57.3 cm** from the monitor screen to the participant's eyes, making calculations mathematically convenient ($1\text{ cm} \approx 1^\circ$).

---

## 4. Standardized EyeLink 1000 Plus Optimization Protocol (For June 11 Pupil Recordings)
To guarantee low-noise, reproducible pupil and gaze records during tomorrow's physical runs, the following procedures have been standardized:

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

### 5.2. Blue Duty Cycle Pupil Experiment (Postponed to June 11, 2026)

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
3.  **Saccade Detection & Dataset Verification (Planned for June 11):** Run the automated EOG saccade detection script (`detect_saccades.py`) on subject Takahira's slower-frequency EEG dataset and perform a comprehensive verification to validate trigger alignment and spatial ocular transitions.
4.  **Pupil Pilot Recording (Planned for June 11):** Execute physical pilot recordings on the EyeLink 1000 Plus under the 25%, 50%, and 75% blue duty cycle conditions.
5.  **Integrated Pupillary-Cortical Modeling (Ongoing):** Combine the completed slower-frequency EEG datasets with tomorrow's pupillometry results to model visual perisaccadic suppression breakthroughs and retinal temporal summation.
