---
trigger: always_on
---

## Project Overview

This project investigates the **phantom array effect** — a visual illusion where a subject perceives additional copies of an LED stimulus due to saccadic eye movement — using EEG and EOG physiological recordings. The core goal is to **automate saccade detection and labeling** (currently done manually) by porting a MATLAB/EEGLAB workflow into Python using `mne-python`.

---

## Experimental Setup

### Stimulus Configuration

| Component | Description |
| --- | --- |
| **Green LED** | Center target; driven by a function generator. The target frequency is often recorded in the filename. |
| **Red LED (Left)** | Flanking LED; activates **inverse** to right Red LED |
| **Red LED (Right)** | Flanking LED; activates **inverse** to left Red LED |

The two Red LEDs always alternate (left ON → right OFF, then right ON → left OFF), creating a left-right switching stimulus pattern. The Green LED runs continuously at the target frequency throughout.

### Recording Conditions (per session)

Two conditions are recorded per subject, each lasting approximately **1 minute 10 seconds**:

1. **Green-only condition**: Only the Green LED is active at the target frequency. Subject fixates on it.
2. **Red+Green condition**: Both Red LEDs (alternating left/right) and the Green LED are active simultaneously. Subject tracks the active Red LED. At some point during this condition, the subject perceives the **phantom array effect** on the Green LED.

### Subject Task

The subject is instructed to **keep their gaze on whichever Red LED is currently active** (i.e., perform saccades following the left-right switching). This produces measurable saccadic eye movement captured in the EOG channel.

*Note: There is no target number of saccades to reach. The subject simply continues tracking the LED for the full duration of the recording.*

---

## Physiological Recordings

* **EEG**: 8-channel recording focused on occipital and frontal regions (`'PO7'`, `'O1'`, `'Oz'`, `'O2'`, `'PO8'`, `'F3'`, `'Fz'`, `'F4'`)
* **EOG**: Electro-oculogram for eye movement tracking (channel name exactly `'EOG'`) — this is the **primary channel** for saccade detection

**Stimulus Timing & Triggers:** There is no independent hardware trigger signal embedded in the EEG recording. The timing of the visual stimulus is inferred directly from the physical eye movements (saccades) captured by the EOG channel.

Both are recorded simultaneously and stored together in EEGLAB `.set`/`.fdt` format.

---

## File Format Specification

### Input Format (from recording hardware/EEGLAB export)

```text
<OriginalFileName>.set
<OriginalFileName>.fdt

```

*Note: The original filename typically contains an identifier for the Green LED switching frequency selected from the connected function generator (e.g., `80` for 80Hz, `4kHz`, etc.).*

Examples:

* `80O.set` / `80O.fdt`
* `4kHz_Part1.set` / `4kHz_Part1.fdt`

### Output Format (renamed for per-subject storage)

```text
<subject_name>-<OriginalFileName>.set
<subject_name>-<OriginalFileName>.fdt

```

Examples:

* `yamashita-80O.set` / `yamashita-80O.fdt`
* `S01-4kHz_Part1.set` / `S01-4kHz_Part1.fdt`

---

## Target Python Workflow (mne-python port)

### Goals

* Load EEGLAB `.set`/`.fdt` files using `mne.io.read_raw_eeglab()`
* Isolate and analyze the EOG channel.
* Implement **automated saccade detection** with aggressive noise-rejection quality gates.
* Export labeled saccade timestamps in ms (Δt from recording start) to `.csv` and/or legacy MATLAB scripts.
* Match or exceed the quality of the manually-validated MATLAB labels.

### Saccade Detection Approach (EOG-based)

Saccades appear in EOG as **sharp, high-amplitude deflections**. Detection pipeline:

1. **Bandpass filter** EOG channel (0.5–30 Hz) to remove DC drift and high-freq noise.
2. **Differentiate** the signal to find rapid slope changes (velocity).
3. **Threshold detection** using a baseline Z-score to find candidate peaks.
4. **Quality Gates** (Morphological and Statistical) to reject false positives caused by subject deviation or noise.

---

## Visual Ground Truth & Noise Rejection Criteria

Based on manual validation, saccade candidates must be rigorously filtered to separate genuine tracking movements from chaotic noise (e.g., subject losing task compliance). Each detected velocity peak must pass **all** of the following checks:

### 1. Single-Peak Velocity Shape

* **Visual:** Real saccades have a single sharp, near-vertical deflection.
* **Rule:** In a window of ±100 ms around the candidate peak, there must be **only one dominant velocity peak**. Secondary peaks exceeding 40% of the primary peak height trigger rejection.

### 2. Post-Saccade Fixation Stability

* **Visual:** Valid saccades are followed by a flat/quiet EOG baseline for at least 200–400 ms. Noisy regions drift continuously.
* **Rule:** In the 200 ms window **after** the velocity peak, the EOG signal variance must fall below a dynamic stability threshold (1.5 × global standard deviation).

### 3. Waveform Monotonicity of the Ramp

* **Visual:** After the sharp onset, the EOG should show a monotonic (smooth) return toward baseline. Deviations show multi-peak, irregular deflections.
* **Rule:** Compute sign changes in the derivative during the 300 ms post-peak window; more than 4 sign reversals triggers rejection.

### 4. Velocity Outlier Check (Global)

* **Visual:** Genuine saccades cluster in a consistent velocity range. Head movements create massive spikes.
* **Rule:** Compute the 25th and 75th **percentile** of all candidate peak velocities to establish an Interquartile Range (IQR). Candidates with peak velocity > Median + 3 × IQR are rejected as artifact spikes.

---