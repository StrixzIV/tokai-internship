# EyeLink 1000 Plus Pupillometry Study: Simplified Experiment Protocol (2026)

*Tokai Data Science and Brain Lab — Department of Human Information Science, Tokai University*  
*Joint Research Collaboration with King Mongkut's Institute of Technology Ladkrabang (KMITL)*

---

## 1. Required Materials

Please verify that all the following components are prepared and correctly connected:

- [ ] **EyeLink 1000 Plus Host PC** (Figure 1) & Power Cord
- [ ] **EyeLink 1000 Plus Host Monitor** (Figure 2)
- [ ] **EyeLink 1000 Plus Camera** (Desktop Mount) (Figure 3) & Power Cord
- [ ] **Display PC** (Figure 4) & Power Cord
- [ ] **Calibration Monitor** (Figure 5) *(Note: This is a separate, dedicated monitor for showing calibration targets to the subject)*
- [ ] **EyeLink 1000 Plus Host to Camera Connection Cable**
- [ ] **Wired LAN-to-USB Type-C Adapter Cable** *(For linking the Display PC to the EyeLink Host PC)*
- [ ] **Spotlight to RGB Switch Extension Cable**
- [ ] **Spotlight Power Cord**
- [ ] **RGB Switch & Power Cord**

---

## 2. Step-by-Step Experimental Procedure

### Step ①: Experimental Setup & Screen Configuration
1. **Ambient Lighting & Initial Power-on:**
   - Dim the room lights to the lowest possible level (near-complete darkness/twilight ambient).
   - Ensure **all cables are fully connected first** before powering on the EyeLink 1000 Plus Host PC (Figure 1) and the Display PC.
   - Set the screen brightness to low and **turn off Wi-Fi** on the Display PC.
   - *Caution: If all cables/cords are not fully connected prior to startup, the monitors may fail to display correctly.*
2. **Camera Positioning:**
   - Install the camera (Figure 3) such that its upper knob is horizontally aligned with the center of the calibration monitor.
   - Remove the camera lens cover (indicated by the red frame in setup references).
3. **Chin Rest Setup:**
   - Install the chin rest assembly on the desk.
   - Have the participant sit comfortably at the station.
4. **Height Adjustment:**
   - Use a measuring tape to adjust the height of the chin rest table.
   - Ensure the participant's eye level is horizontally aligned with the **top 25% line** of the monitor (indicated by masking tape).
5. **Screen Configuration Settings:**
   - Power on the EyeLink 1000 Plus. On the camera setup screen, select `Offline` -> `Exit EyeLink` to access the File Manager.
   - Click the `Configuration` icon, then select the `Screen Settings` icon.
   - Configure the screen parameters precisely as follows:
     - **Width:** `480 mm`
     - **Height:** `270 mm`
     - **Width:** `1920 pixels`
     - **Height:** `1080 pixels`
     - **Eye to Screen Distance:** Measure and input the physical distance individually for each participant.
     - **Camera to Screen Distance:** *Do not configure (leave blank / default).*
   - Click **Save** to lock in the settings.
   - Double-click the **EyeLink** icon to return to the EyeLink Host application.

### Step ②: Mesopic Adaptation (15 Minutes)
1. Ensure the calibration monitor screen is **turned off** (blank).
2. Begin the **15-minute mesopic adaptation** period for the participant.
3. While the participant is adapting, you can proceed with the camera setup (Step ③) in the dark.
4. Calibration and validation (Step ④) can be initiated **at the earliest 5 minutes** into the adaptation period to minimize waiting time (allowing adaptation to continue simultaneously).

### Step ③: Camera Setup
Once the EyeLink Camera Setup screen is loaded, execute the following configuration:
1. **Sampling Parameters:**
   - Verify that the sampling rate is set to **1000 Hz** and the tracking algorithm is set to **Centroid**.
2. **Eye-Tracking Mode Selection:**
   - Go to `Set Option` -> `Select Configuration`.
   - Select the desired mode: the top option is **Monocular (one eye)** and the second option is **Binocular (both eyes)**.
   - Press `Accept` to confirm. (Ensure **Left Monocular mode** is chosen unless otherwise specified).
3. **Pacing and Data Structure:**
   - On the top-left of the `Set Option` screen, verify the following:
     - **Calibration Type:** `5-Point Grid`
     - **Pacing Interval:** `1500 msec` (tentative)
     - **Pupil Size Data:** `DIAMETER`
4. **Camera Focus & Alignment:**
   - Return to the main Camera Setup screen (click the `Camera Setup` button).
   - Manually adjust the camera angle so that the participant's eyes are cleanly centered in the camera image.
   - Adjust the physical camera lens focus until the eye image is perfectly sharp.
5. **Threshold Adjustment:**
   - Use the left-click mouse action to position the red bounding box directly over the pupil.
   - To adjust the size of the bounding box, hold **ALT** and use the **Arrow Keys**.
   - Click the **Auto Threshold** button (or press the **'A' key**) to automatically segment the pupil.
   - Verify that the pupil is cleanly filled with a solid, stable blue overlay. Refer to the three thresholding states below:
     - *Threshold Too Low (Left):* Bounding box misses parts of the pupil, causing severe high-frequency noise.
     - *Appropriate Threshold (Center):* Clean, stable pupil overlay with zero leaks (Target: **75 to 115**).
     - *Threshold Too High (Right):* Shadows near eye corners are misidentified as part of the pupil ("corner effect").
6. **Range Targets & Corneal Reflection (CR):**
   - Confirm the Corneal Reflection (CR) is identified as a stable, sharp turquoise dot.
   - Adjust the CR threshold using the **'+' and '-' keys** if needed (ensure the CR threshold **does not exceed 240**).
7. **Tracking Range Verification:**
   - Perform a quick manual sweep: ask the participant to look at the four extreme edges (cross directions) of the calibration screen. Ensure the tracking indicators (blue pupil overlay and turquoise CR dot) remain stable and are not lost at any edge.

### Step ④: Calibration & Validation
*Note: The Python script running on the Display PC can be force-terminated at any point by pressing `Ctrl + C`.*

1. **Preparing the Python Script:**
   - ***Ensure the calibration monitor remains turned off initially.***
   - After 5 minutes of mesopic adaptation, open the folder named `2026瞳孔実験データフォルダ` (2026 Pupil Experiment Data Folder) on the Display PC desktop.
   - Verify that the experimental script `EyeLink1000Plus_PyLink_瞳孔2026実験用.py` is present, and copy its filename.
2. **Launching the Script:**
   - Right-click in any empty area within the folder and select **"Open in Terminal"**.
   - In the terminal, type `python ` and paste the filename (Ctrl+V), then press **Enter**.
   - *Note: Ensure there is a half-width space between `python` and the script name.*
3. **Screen Activation:**
   - When the program initializes, press **Enter** to advance.
   - **Wait until the screen displays a gray background with a white circle in the center, and only then turn on the calibration monitor.**
   - *Crucial: Use an physical light-blocking board to shield the participant's eyes from the monitor's light until the screen output is fully stabilized.*
4. **Calibration (5-Point Grid):**
   - Press the **'C' key** to initiate calibration.
   - Wait 1 second for the participant to orient, then press **'A'** to run the calibration in **Auto Mode**.
   - *Verbal Instruction to Participant:* "Please gaze directly and steadily at the tiny black dot in the center of the white target."
5. **Validation:**
   - Once the calibration cycle completes, press the **'V' key** to launch validation.
   - Press **'A'** to run validation, timing it with the participant's fixation.
   - *Quality Control Thresholds:* Inspect the bottom of the screen. Ensure the **Average Error is < 0.5°** and the **Maximum Error is < 1.0°**. 
   - *Recalibration Rule:* If the results display "Error" or exceed these thresholds, do not accept the run. Press the **'C' key** to recalibrate from scratch.

### Step ⑤: Pupil Response Recording
1. **Setting up the Optical Apparatus:**
   - Gently slide/move the calibration monitor out of the way.
   - Place the glass plate assembly and the book stand onto the platform.
   - *Caution: Do not unplug the USB/LAN conversion cables from the Display PC, and ensure you do not touch, bump, or move the camera during this transition.*
   - Align the red dot in the center of the glass plate to form a straight line using a set square (triangle ruler).
   - Align the book stand precisely with the **yellow tape** marked on the table surface.
2. **Initiating the Recording:**
   - Press **Enter** on the keyboard to start recording.
   - The automated stimulation protocol will run:
     - **Baseline (BL):** 3 seconds of pre-stimulus baseline recording.
     - **Light Stimulation:** 5 seconds of active blue flickering light stimulation.
     - **Post-Stimulus Recovery:** 60 seconds of post-illumination recording (to capture PIPR).
3. **Terminating the Recording:**
   - Press **Enter** again to stop and save the trial recording.
4. **File Naming Convention:**
   - Rename the output EDF file immediately after the recording using the following strict format:
     - **Format:** `[YYYYMMDD].[participant_name]_B[stimulation_duration]ms.edf`
     - **Example:** `20260613.takao_B250ms.edf`
5. **Sequence Repetition:**
   - Repeat the cycle of **Step ④ Calibration/Validation** and **Step ⑤ Recording** for each experimental condition.
   - *Optimization:* Calibration and validation may be skipped if the participant has remained completely still and there is zero head drift.
   - *Rest Intervals:* During rest breaks, you can verify pupil recovery by running the pupil diameter check program.
6. **Host Shutdown:**
   - If shutting down the system immediately after all recordings are finished, go to the Host PC and select `Offline` -> `Shutdown Host`.

---

## 3. Data Conversion & Export (EDF to ASC)

After completing the experimental sessions, convert the raw binary EDF logs into analysis-ready text-based ASC files:

1. **Launch Conversion Software:**
   - On the Display PC desktop, open the application **"Visual EDF2ASC"**.
2. **Import EDF Files:**
   - Click on `Add EDF Files to Convert`.
   - Browse and select all the `.edf` files recorded during the session, then click `Add`.
3. **Execute Conversion:**
   - Click the **"Convert to ASC"** button.
   - Wait until the message **"Conversion Complete"** is displayed in the bottom-left corner of the interface.
   - The converted `.asc` files will be saved automatically in the same source folder as the raw `.edf` data.
4. **Upload to Collaboration Space:**
   - Upload the finalized `.asc` data files to the designated folder on **Microsoft Teams** for joint analysis.

---

## 4. Post-Experiment Cleanup

Please restore the laboratory environment to its standard state:

1. Move the chin-rest stand and the spotlight apparatus back to their designated rear positions.
2. Carefully take down and store the calibration monitor, optical diffuser, book stand, and camera.
3. Place the EyeLink camera back into its protective cardboard box, wrapping it carefully with the provided bubble wrap/packing materials and securing the box lid.
