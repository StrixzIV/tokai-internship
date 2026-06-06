# Intrinsically Photosensitive Retinal Ganglion Cells (ipRGCs) Pupillary Light Reflex Study: Light Response Characteristics to Blue Flickering Light (2026)

*Tokai Data Science and Brain Lab — Department of Human Information Science, Tokai University*  
*Joint Research Collaboration with King Mongkut's Institute of Technology Ladkrabang (KMITL)*

---

## 1. Research Topic & Experimental Overview
* **Research Goal:** To investigate the light-response and temporal integration characteristics of intrinsically photosensitive retinal ganglion cells (ipRGCs) in response to blue flickering light, utilizing the Pupillary Light Reflex (PLR) and Post-Illumination Pupillary Response (PIPR) as physiological indices.
* **Clinical and Architectural Significance:** This study serves as a foundational effort toward preventing discomfort glare, designing health-conscious temporal lighting environments, and establishing standards for high-fidelity ocular physiological data collection.

---

## 2. Experimental Conditions and Physiological Rationales

### 2.1. Visual Stimulation Parameters
* **Stimulus Light:** Blue flickering light at a frequency of **1 Hz**.
* **Stimulus Luminance:** **50 cd/m²** (Irradiance/illuminance levels to be measured and logged during subsequent calibration runs).
* **Duty Cycles:** Tested at three distinct ratios: **25%, 50%, and 75%**.
  * *Physiological Rationale:* Evaluating these three equally-spaced points (25% increments) allows us to analyze how the pupillary response changes relative to stimulus duration (light energy exposure). By plotting the duty cycle on the horizontal axis and the pupil constriction rate or PIPR on the vertical axis, we can statistically model the temporal summation dynamics (non-linearity) of ipRGCs. Specifically, this helps determine if the response scales linearly with stimulus duration or if the ipRGC pathway exhibits saturation (plateauing) between 50% and 75%.
  * *Data Quality Rationale:* The 50 cd/m² intensity and 1 Hz flicker are optimized to prevent discomfort glare. Minimizing glare prevents participants from blinking or narrowing their eyelids, which is essential for ensuring continuous, high-fidelity data acquisition without signal loss.

### 2.2. Environmental and Setup Adaptations
* **Pre-Stimulus Adaptation (Mesopic/Twilight Adaptation):** Strictly set to **15 minutes** (referencing Lab Note 20250910).
  * *Physiological Rationale:* Although a full 30-minute adaptation is theoretically ideal, a 15-minute window is chosen to balance retinal dark adaptation with participant fatigue. Excessive dark adaptation can lead to drowsiness-induced miosis (lowering baseline arousal and introducing pupillary noise), whereas 15 minutes is the strict physiological minimum required to stabilize retinal light adaptation.
* **Shielded Room Ambient Brightness:** Stabilized at **16.1 lux**.
  * *Rationale 1 (Prevention of Drowsiness-Induced Miosis):* A completely dark environment causes a drop in participant alertness, inducing drowsiness-induced miosis. Maintaining a 16.1 lux background keeps subjects awake and secures a stable baseline pupil diameter (Reference: Kardon et al., 2009).
  * *Rationale 2 (Glare Mitigation and Data Retention):* Direct blue light stimulation on a completely dark-adapted eye triggers strong discomfort glare, leading to heavy blinking and missing frames. Moderate background illumination slightly reduces retinal sensitivity, lowering subject discomfort and ensuring continuous, high-precision recordings (Reference: Kelbsch et al., 2019).
  * *Rationale 3 (Ecological Validity):* Real-world exposure to blue light in complete darkness is rare. A 16.1 lux ambient environment closely mimics natural scenarios (e.g., operating a smartphone or digital display in a dimly lit room), enhancing the ecological validity of the findings.
* **Participant-to-Stimulus View Distance:** Maintained at exactly **57.3 cm**.
  * *Mathematical Rationale:* At 57.3 cm, 1 cm of physical width on the screen corresponds to exactly 1° of visual angle ($1\text{ cm} \approx 1^\circ$), simplifying visual angle calculations and stimulus sizing.
* **Sampling Rate:** Recorded at **1000 Hz** to capture millisecond-accurate pupillary dynamics and transient PLR slopes.

---

## 3. EyeLink 1000 Plus Calibration & Optimization Protocol

To ensure high-fidelity pupillary data, the following sequential pipeline must be strictly executed for every participant:

$$\text{Setup \& Screen Configuration} \rightarrow \text{Camera Setup} \rightarrow \text{Calibration} \rightarrow \text{Validation} \rightarrow \text{Drift Check} \rightarrow \text{Recording} \rightarrow \text{EDF to ASC}$$

### 3.1. Hardware and Screen Configuration
* **Mount Type:** Desktop Mount utilizing head-stabilized chin rest (stabilized head).
* **Screen Positioning:** 
  * The Display PC monitor must be positioned so that when the participant sits upright, their eye height aligns with the upper 25% of the screen.
  * The screen must subtend a horizontal visual angle of $\le 32^\circ$ and a vertical visual angle of $\le 25^\circ$. To keep the eyes within the tracker's optimal range, the viewing distance must be at least 1.75 times the display width.
  * The Desktop Mount must be positioned 40–70 cm from the participant (ideal: 50–55 cm) measured from the top knob of the mount to the front of the chin rest.
  * Position the mount horizontally centered with the monitor. Elevate the mount to position the illuminator as close to the bottom edge of the visible screen as possible without blocking the participant's field of view.
* **Screen Configuration Settings:** Done prior to camera setup. Exit the camera screen to the File Manager, open Configuration, and update the physical screen dimensions and viewing distance (refer to Section 8.4 of the EyeLink 1000 Plus Installation Guide).
  * *Significance in Pupillometry:* 
    1. Synchronizes gaze location with stimulus coordinates to prevent spatial-temporal mapping errors.
    2. Optimizes real-time visual angle calculations to quantify the precise relationship between retinal illuminance and pupil size.
    3. Facilitates spatial noise filtering (e.g., differentiating physical eye movements from apparent pupil size changes).

### 3.2. Camera Setup & Thresholding
* **Tracking Mode:** Pupil-Corneal Reflection (Pupil-CR) mode. Pupil-Only mode is strictly restricted to mouth-bite board setups.
* **Channel Configuration:** Monocular or binocular tracking. In binocular mode, ensure the vertical dotted guide line on the global camera view is aligned with the center of the participant's face (equally dividing the eyes) to balance illumination.
* **Pupil Thresholding Procedure:**
  1. Have the participant focus on their eye image. Press the **Auto Threshold** button (or **'A' key**) on the Host PC to automatically detect the pupil boundary.
  2. Verify that the pupil is filled with a solid, stable blue overlay without leaks. If the subject blinked during auto-thresholding, re-run the auto-threshold.
  3. Manually fine-tune the threshold using the **Up/Down Arrow keys** (Up increases blue overlay; Down decreases it). 
     * *Low Threshold Hazard:* Blue area is smaller than the actual pupil, introducing severe high-frequency noise into the diameter log.
     * *High Threshold Hazard:* Shadows at the eye corners are misidentified as the pupil ("corner effect"), distorting coordinates when the participant looks laterally.
     * *Target Range:* Pupil threshold should settle between **75 and 115**.
* **Corneal Reflection (CR) Thresholding:**
  1. Verify the CR is identified as a stable, sharp turquoise (light blue) circle.
  2. If needed, manually adjust the CR threshold using the **'+' and '-' keys** (CR threshold should not exceed 240).
  3. Have the participant trace the screen perimeter to verify the CR is not lost. Watch out for CR "smearing" at screen corners (which indicates the viewing angle is too wide; resolve by raising the mount or increasing the viewing distance).
* **Tracking Algorithm Selection:**
  * **Centroid Mode (Recommended):** Highly recommended due to its extremely low noise floor.
  * **Ellipse-Fitting Mode:** Use only if severe eyelid/eyelash occlusion is present. Ellipse mode interpolates pupil shape behind obstructions, reducing drift, but introduces a higher noise floor.

### 3.3. Calibration Protocol (5-Point Grid)
* **Configuration:** Select **5-point calibration** in options. Set "Randomize target order" to **YES** and "Auto-trigger pacing" to **1000 ms**.
* **Four Rules for High-Precision Calibration:**
  1. **Enforce a Latency Delay on First Point:** When manual trigger is used, wait approximately 0.5 to 1.0 second (a brief pause) after the eye lands on the first target before hitting **ENTER**. This allows post-saccadic micro-oscillations to settle, dramatically reducing grid distortion.
  2. **Leverage the Backspace Key:** If the subject blinks or loses focus on a specific point during automatic pacing, immediately press **Backspace** to re-present and re-acquire that single point, avoiding a complete restart and preventing subject fatigue.
  3. **Manually Inspect the Calibration Grid:** Do not blindly accept the system's green "GOOD" status. The experimenter must visually verify that the 5 points form a clean, non-distorted geometric shape. Recalibrate immediately if any points are skewed or crowded.
  4. **Provide Precise Verbal Instructions:** Instruct participants to "Stare directly at the tiny white dot inside the center of the target" rather than "look at the target." This locks their fovea and stabilizes pupil coordinates.

### 3.4. Validation Protocol (Validation)
* **Three Strict Quality Cut-offs:**
  1. **Rely on Quantitative Error Values, Not Labeled Ratings:** A green "GOOD" rating is a generic threshold. For rigorous physiological research, enforce a strict academic standard: **Average Error < 0.5°** and **Maximum Error < 1.0°**. Recalibrate if the Average Error exceeds 0.5°, even if labeled "GOOD".
  2. **Differentiate Systematic and Accidental Errors:**
     * *Accidental Error (Single outlier point):* Usually caused by a blink or a transient loss of focus. Do not modify the hardware setup; simply re-run the validation (**'V' key**) or retry that single point using **Backspace**.
     * *Systematic Error (Symmetric shift or broad drift):* Indicates the chin rest moved, the camera was bumped, or the subject's posture changed. Do not repeat validation; immediately re-run calibration (**'C' key**) from the beginning.
  3. **Immediate Recalibration on FAIR/POOR:** If a validation yields "FAIR" (grey) or "POOR", immediately halt the trial and return to camera setup. EyeLink data offsets cannot be mathematically corrected post-hoc.
* **Crucial Ocular Data Enhancements:**
  1. **Unify Calibration and Experimental Background Luminance:** This is a vital rule to prevent the **Pupil Center Shift** phenomenon (changes in pupil size physically shift the calculated pupil center coordinate). Ensure the Python/PyLink program sets the calibration screen background RGB values to exactly match the experiment's background RGB values.
  2. **Provide Dark/Ambient Adaptation Time:** After mounting the participant, display the ambient background screen and allow **2 to 3 minutes** of adaptation before starting the calibration, letting the pupil size stabilize.
  3. **Execute a Discardable "Practice" Run:** Treat the first calibration/validation sequence as a practice run to let the participant adapt to the target pacing, then execute the official run.

### 3.5. Drift Checking and Correction
* **Interpretation in Pupil-CR Mode:** In head-stabilized Pupil-CR setups, Drift Correction serves as a diagnostic "Drift Check" that reports coordinate deviation rather than applying mathematical offsets to raw data.
* **In-Trial Integration:** Call the `doDriftCorrect()` function in PyLink at the beginning of each trial. This forces central fixation control and monitors drift. If drift exceeds acceptable bounds, press **ESC** to exit and re-calibrate. Enabling true coordinate offset corrections is discouraged, as it can mask underlying physical movement issues.

---

## 4. Key Academic References
* **Kardon, R. et al. (2009).** *Intrinsically Photosensitive Retinal Ganglion Cell Behavior in Humans.* Ophthalmology, 116(3), 503-513. (Establishes background illumination guidelines to maintain arousal and prevent drowsiness-induced miosis).
* **Kelbsch, C. et al. (2019).** *Standards in Pupil Recording and Analysis in Clinical and Scientific Settings.* Journal of Ophthalmology, 2019, 1-13. (Establishes standards for preventing discomfort glare, minimizing blink-induced data loss, and optimizing thresholding).
* **EyeLink 1000 Plus User Manual (v1.0.21).** *SR Research Ltd.* (Sections 3.2 to 3.11 for thresholding, tracking mode, and 5-point calibration algorithms).
