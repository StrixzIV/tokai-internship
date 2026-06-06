# Weekly Progress Report (Week 4 Plan & Setup)
**Project Title**: Automating Ocular Tracking in Phantom Array Psychophysics & Pupillometry Bistability Analysis
**Joint Research Collaboration**: Tokai Data Science and Brain Lab (Tokai University) & King Mongkut's Institute of Technology Ladkrabang (KMITL)
**Date**: June 13, 2026 (Projected / Planned)
**Prepared by**: Jirayu Kaewsing & Research Assistant Team

---

## 1. Executive Summary
This report outlines the planned experimental design, physiological rationales, and EyeLink 1000 Plus calibration protocols established for execution during Week 4 (June 8 – June 13, 2026) of the collaborative internship. Following the successful completion of the primary neurophysiological goals of the Phantom Array Effect (PAE) study in Week 3, the project is transitioning to the **Blue Duty Cycle Pupil Study**.

The primary focus of Week 4 is to investigate the light-response and temporal integration characteristics of intrinsically photosensitive retinal ganglion cells (ipRGCs) under blue flickering light using the Pupillary Light Reflex (PLR) as a physiological marker. To prepare for this phase, we have translated and compiled a comprehensive English translation of the Japanese experimental protocol under `docs/en/blue_duty_cycle_pupil_protocol.md` and established strict mathematical and physical criteria to ensure high-fidelity, continuous ocular data collection.

---

## 2. Experimental Design & Rationale (Week 4 Objectives)

### 2.1. Visual Stimulation Parameters
*   **Stimulus Properties:** Blue flickering light modulated at a frequency of **1 Hz** with a luminance of **50 cd/m²** (irradiance values to be logged during subsequent physical measurements).
*   **Duty Cycle Conditions:** The stimulation will be tested at three distinct duty cycles: **25%, 50%, and 75%** (delivered in 25% equal steps).
    *   *Temporal Summation Analysis:* This setup is designed to evaluate how the pupil's constriction rate and Post-Illumination Pupillary Response (PIPR) scale relative to the light energy exposure time. This allows us to statistically model the temporal summation dynamics of the ipRGC pathway and evaluate if the response behaves linearly or exhibits saturation (plateauing) between 50% and 75%.
    *   *Data Quality Control:* The moderate 50 cd/m² intensity and slow 1 Hz flicker are optimized to prevent discomfort glare. Minimizing glare prevents participants from squinting or blinking, which is essential to secure continuous, high-fidelity pupillometry recordings.

### 2.2. Environmental and Physical Setup
*   **Twilight Adaptation (Mesopic Adaptation):** Standardized at exactly **15 minutes** prior to stimulation.
    *   *Arousal vs. Dark Adaptation:* While 30 minutes of dark adaptation is standard, 15 minutes is selected to prevent participant drowsiness. Complete darkness induces a drop in alertness leading to sleepiness-induced miosis (pupil noise), whereas 15 minutes is the strict physiological minimum to stabilize baseline light adaptation without inducing sleepiness.
*   **Ambient Room Brightness:** Regulated at a background illumination of **16.1 lux** inside the shielded recording room.
    *   *Prevention of Baseline Drift:* A background of 16.1 lux keeps participants awake, stabilizing the baseline pupil size (Kardon et al., 2009).
    *   *Blink Avoidance:* Exposing a fully dark-adapted eye to blue light causes intense discomfort glare and triggers missing data frames due to blinks. Background light slightly tempers retinal sensitivity, securing high-precision recordings (Kelbsch et al., 2019).
    *   *Ecological Validity:* Standard smartphone and display usage in dim rooms matches this 16.1 lux ambient environment, making the findings highly applicable to real-world display engineering.
*   **Physical Distance & Visual Angle:** Fixed viewing distance of exactly **57.3 cm** from the monitor screen to the participant's eyes.
    *   *Mathematical Convenience:* At a distance of 57.3 cm, 1 cm on the screen equals exactly 1° of visual angle ($1\text{ cm} \approx 1^\circ$), simplifying visual angle calculations.

---

## 3. Standardized EyeLink 1000 Plus Optimization Protocol

To guarantee low-noise, reproducible pupil and gaze records, the following procedures are set for implementation:

### 3.1. Calibration and Quality Control
*   **5-Point Grid Calibration:** Configured with randomized target order and a **1000 ms auto-trigger pace**.
*   **Trigger Timing Control:** Enforce a manual trigger delay of **0.5 to 1.0 second** (a brief pause) after the eye lands on the target before pressing ENTER. This allows post-saccadic micro-oscillations to settle, preventing grid distortion.
*   **Single-Point Recovery:** Use the **Backspace key** to re-present and re-acquire any point where a participant blinks or loses focus, protecting the participant from fatigue by avoiding complete calibration restarts.
*   **Strict Validation Cut-offs:**
    *   Enforce a strict cutoff of **Average Error < 0.5°** and **Maximum Error < 1.0°** (exceeding standard clinical limits to meet rigorous visual neuroscience requirements).
    *   If validation results in a "FAIR" or "POOR" rating, immediate recalibration must be performed.
*   **Pupil Center Shift Mitigation:** The calibration screen background RGB values must be programmed to match the actual experiment background RGB values exactly. This eliminates the Pupil Center Shift phenomenon (where shifts in pupil size shift the calculated pupil center coordinate, introducing systematic errors).

### 3.2. Camera & Threshold Tuning
*   **Tracking Mode:** Standard Pupil-Corneal Reflection (Pupil-CR) tracking utilizing a Desktop Mount with a head-stabilized chin rest.
*   **Algorithm Selection:** **Centroid mode** is selected as the default due to its extremely low noise floor. **Ellipse-Fitting mode** will only be utilized in cases of severe eyelid/eyelash occlusion.
*   **Threshold Boundaries:** Target pupil thresholds will be maintained between **75 and 115** using the Up/Down Arrow keys. Corneal Reflection (CR) thresholds will be kept below **240** using the +/- keys, ensuring stable turquoise circles without corner smearing.

---

## 4. Summary of Week 4 Experimental Parameters

| Parameter | Planned Value / Setting | Physiological / Technical Rationale |
|:---|:---|:---|
| **Stimulus Frequency** | 1 Hz (Blue LED / Display) | Capture transient PLR and steady-state PIPR kinetics |
| **Stimulus intensity** | 50 cd/m² (Luminance) | Prevents discomfort glare and associated blink-induced data loss |
| **Duty Cycles** | 25%, 50%, 75% | Evaluate non-linear temporal summation and ipRGC pathway saturation |
| **Twilight Adaptation** | 15 minutes (Mesopic) | Balance retinal light adaptation with prevention of drowsiness |
| **Ambient Background** | 16.1 lux | Prevents drowsiness-induced miosis and keeps subjects alert |
| **Viewing Distance** | 57.3 cm | Mathematically convenient visual angle scaling ($1\text{ cm} \approx 1^\circ$) |
| **Sampling Rate** | 1000 Hz | Captures millisecond-level pupillary constriction and recovery slopes |
| **Calibration Mode** | 5-Point, Pupil-CR, Centroid | Ensure highest spatial-temporal accuracy with minimal noise floor |
| **Validation Threshold** | Avg < 0.5°, Max < 1.0° | Academic-grade spatial accuracy cutoff |

---

## 5. Planned Deliverables for Week 4
1.  **Experimental Script Deployment:** Implement the 1 Hz blue flashing stimulation routine in Python/PyLink with synchronized backgrounds.
2.  **Pilot Recording & Conversion:** Execute pilot recordings on the EyeLink 1000 Plus, producing `.EDF` raw data and converting them to `.ASC` files for analysis.
3.  **Data Analysis Pipeline:** Develop Python analysis code to compute baseline pupil diameter, constriction amplitude, and Post-Illumination Pupillary Response (PIPR) parameters.
