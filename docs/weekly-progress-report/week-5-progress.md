# Weekly Progress Report (Week 5 Status Update)
**Project Title**: Automating Ocular Tracking in Phantom Array Psychophysics & Pupillometry Bistability Analysis
**Joint Research Collaboration**: Tokai Data Science and Brain Lab (Tokai University) & King Mongkut's Institute of Technology Ladkrabang (KMITL)
**Date**: June 17, 2026 (Wednesday Progress Report)
**Prepared by**: Jirayu Kaewsing & Research Assistant Team

---

## 1. Executive Summary
This progress report documents the key technical developments, experimental standardizations, and computational refinements accomplished during Week 5 (June 14 – June 17, 2026) of the collaborative internship. This week’s progress successfully addresses two major pillars of the joint research program: the formal consolidation of physical experimental protocols and the advanced generalization of statistical evaluation pipelines.

First, the experimental framework for the pupillometry studies was formally standardized through the finalization and check-in of a highly rigorous, simplified clinical-grade guide, the "EyeLink 1000 Plus Pupillometry Study: Simplified Experiment Protocol" (`pupil-experiment-protocol.md`), alongside a corresponding Japanese simplified version in MS Word format (`docs/jp/実験手順(簡易版).docx`). This protocol codifies a step-by-step checklist of physical materials, participant chin-rest alignment, 15-minute mesopic twilight adaptation, tracking thresholds, 5-point grid calibration limits, and trial sequence timing to eliminate inter-session measurement variance and guarantee cross-site experimental replication.

Second, the statistical evaluation architecture in `statistical_evaluation.ipynb` was significantly upgraded and generalized. To transition from a rigid static analysis to a flexible, reproducible modeling engine, a dedicated global configuration block was introduced, abstracting baseline window lengths, early/late Area Under the Curve (AUC) bounds, and Post-Illumination Pupillary Response (PIPR) sampling times. Additionally, the analytical engine was expanded to compute and export a dual-metric feature suite consisting of both **Normalized Constriction** and **Raw Physical Constriction** metrics. This enables researchers to perform dual-layer statistical evaluations: normalized AUC/PIPR to isolate intrinsic photoreceptor sensitivities across individuals, and raw physical AUC/PIPR to quantify absolute pupil diameter limits and system tracking dynamics. These updates represent a critical step toward high-throughput, standardized modeling of intrinsically photosensitive retinal ganglion cell (ipRGC) and melanopsin-driven pupillary kinetics.

---

## 2. Progress Details

### Week 5 (June 14 – June 17, 2026): Protocol Standardization & Dual-Metric Analytics Refinement

*   **Finalization of the Standardized EyeLink 1000 Plus Protocol (June 17, 2026)**:
    *   **Academic and Operational Guidelines**: Completed and deployed the dual-language physical testing protocol. The English version (`docs/en/pupil-experiment-protocol.md`) and the simplified Japanese version (`docs/jp/実験手順(簡易版).docx`) establish a clinical baseline for pupillometry runs.
    *   **Calibration Constraints**: Codified a rigid 5-point calibration grid on the EyeLink 1000 Plus, enforcing strict validation thresholds where the average validation error must be less than 0.5° and the maximum error must be less than 1.0°. Calibration screen luminance profiles are matched to the experiment background to eliminate pupillary baseline shifts during transit.
    *   **Experimental Timeline Synchronization**: Standardized the recording trial timeline to include 3 seconds of pre-stimulus baseline (BL) recording, 5 seconds of active blue flickering light stimulation (1 Hz, 50 cd/m², 25%/50%/75% duty cycles), and 60 seconds of post-stimulus recovery to fully capture the sustained Post-Illumination Pupillary Response (PIPR) and isolate ipRGC-driven melanopsin kinetics.
    *   **Post-Run Pipeline Standardization**: Outlined the operational steps for converting raw binary EDF logs into ASCII (ASC) format via the Visual EDF2ASC converter, complete with repository and Teams file sharing conventions.

*   **Engineering of Jupyter Analysis Configuration Block (June 17, 2026)**:
    *   **Decoupled Parameterization**: Integrated an explicit configuration section in `statistical_evaluation.ipynb` to abstract hardcoded parameters into global variables. These include:
        *   `BASELINE_DURATION_SEC = 1.5` (length of pre-stimulus baseline window)
        *   `EARLY_AUC_DURATION_SEC = 6.0` (time window immediately post-stimulus offset to capture early recovery)
        *   `LATE_AUC_START_SEC = 6.0` and `LATE_AUC_END_SEC = 12.0` (sustained window post-stimulus offset for late ipRGC decay)
        *   `PIPR_TIME_SEC = 6.0` (time point for PIPR magnitude quantification)
    *   **Dynamic UI and Analytical Scaling**: Modified all downstream calculation masks, integration algorithms, and visualization shaded intervals to scale dynamically with these configuration variables. Changes in the configuration block instantly cascade through the code, adjusting the plotting borders, shading regions, text overlay metrics, and exported CSV/Excel tables without manual script edits.

*   **Deployment of Dual-Metric Statistical Engine (June 17, 2026)**:
    *   **Raw Constriction Integration**: Upgraded the preprocessing and calculation loop to compute raw physical pupil constriction ($A_{raw\_constriction} = A_{base} - A_t$) in addition to the traditional normalized constriction ($A_{normalized\_constriction} = \frac{A_{base} - A_t}{A_{base}}$).
    *   **Dual-Layer Feature Suite Extraction**: Refined `calculate_pupil_metrics` to compute six core statistical parameters from each processed CSV dataset:
        1.  *Baseline Pupil Size ($A_{base}$)*: pre-stimulus median diameter.
        2.  *Normalized Early AUC*: trapezoidal area under the normalized constriction curve from $T_{offset}$ to $T_{offset} + EARLY\_AUC\_DURATION\_SEC$.
        3.  *Raw Early AUC*: trapezoidal area under the raw constriction curve over the same early recovery window.
        4.  *Normalized Late AUC*: trapezoidal integration of normalized constriction over the late decay window ($T_{offset} + LATE\_AUC\_START\_SEC$ to $T_{offset} + LATE\_AUC\_END\_SEC$).
        5.  *Raw Late AUC*: trapezoidal integration of raw physical constriction over the late decay window.
        6.  *Normalized PIPR*: normalized constriction value at exactly $T_{offset} + PIPR\_TIME\_SEC$ seconds.
        7.  *Raw PIPR*: raw pupil constriction in tracking units at exactly $T_{offset} + PIPR\_TIME\_SEC$ seconds.
    *   **Expanded Visualization and Tabular Export**: Modified the plotting engine to generate three diagnostic panels, with Panel 3 dynamically displaying the full dual-metric text overlay (combining Normalized and Raw parameters side-by-side). Rewrote the file exporting sequence to map relative paths to `../../../out` (with fallback to `./out`), outputting expanded tables `260611_metrics.csv` and `260611_metrics.xlsx` that support comprehensive downstream statistical modeling across subjects.

---

## 3. Technical & Methodological Advancements

### 3.1. Standardized Pupillometry Experimental Protocol
The experimental protocol finalized in Week 5 provides a unified framework to systematically control experimental variables that confound pupillary measurements.

```
       +-----------------------------------------------------------------+
       |  1. Ambient Environment Setup (Twilight adaptation, 16.1 lux)    |
       +-------------------------------+---------------------------------+
                                       |
                                       v
       +-----------------------------------------------------------------+
       |  2. Chin-Rest & Height Alignment (Eye level at top 25% of monitor) |
       +-------------------------------+---------------------------------+
                                       |
                                       v
       +-----------------------------------------------------------------+
       |  3. Mesopic Adaptation Phase (15 minutes total duration)        |
       +-------------------------------+---------------------------------+
                                       | (After 5 mins of adaptation)
                                       v
       +-----------------------------------------------------------------+
       |  4. Camera Tuning & Calibration (5-point grid validation)       |
       |     * Avg Error < 0.5°, Max Error < 1.0°                        |
       |     * Pupil threshold: 75-115, CR threshold: <= 240             |
       +-------------------------------+---------------------------------+
                                       | (After 15 mins total adaptation)
                                       v
       +-----------------------------------------------------------------+
       |  5. Pupil Recording Session (3s Baseline -> 5s Light -> 60s PIPR)|
       +-----------------------------------------------------------------+
```

The strict physical controls defined in this protocol are critical for isolating melanopsin-driven pupil bistability from transient sympathetic arousal or light-reflex noise. In particular:
*   **The 15-Minute Mesopic Adaptation** allows rods and cones to settle to a stable, reproducible state of adaptation under controlled room ambient lighting of 16.1 lux, preventing sleepiness-induced miosis while standardizing baseline pupil diameter.
*   **Grid Validation Cutoffs** (< 0.5° average, < 1.0° max error) ensure that small, involuntary ocular movements (micro-saccades and tremors) do not translate into physical tracking distortions or false pupil diameter changes due to geometric perspective errors.
*   **Equalizing Calibration and Stimulus Backgrounds** prevents a transient pupil light reflex from occurring during the immediate transition from calibration screens to experimental trials, which would otherwise skew pre-stimulus baseline values ($A_{base}$).

### 3.2. Dynamic Dual-Metric Statistical Analysis
In mathematical modeling of pupillary dynamics, analyzing both normalized and raw physical constriction scales is highly informative. The mathematical formulation implemented in `statistical_evaluation.ipynb` is structured as follows:

1.  **Baseline Determination ($A_{base}$)**:
    $$A_{base} = \text{median}\left(\{A_t \mid t \in [T_{onset} - D_{base}, T_{onset}]\}\right)$$
    where $D_{base}$ is defined by `BASELINE_DURATION_SEC` (default 1.5 seconds).

2.  **Time Series Constriction Matrices**:
    *   *Normalized Constriction*:
        $$\text{NormalizedConstriction}_t = \frac{A_{base} - A_t}{A_{base}}$$
    *   *Raw Constriction*:
        $$\text{RawConstriction}_t = A_{base} - A_t$$

3.  **Area Under the Curve (AUC) Shaded Windows**:
    The Area Under the Curve represents the cumulative temporal constriction, indicating the overall energy and sustained activation of the pupillary constriction response. This is computed using trapezoidal integration over designated windows:
    $$\text{AUC} = \int_{T_{start}}^{T_{end}} C_t \, dt \approx \sum_{k} \frac{C_{t_k} + C_{t_{k+1}}}{2} (t_{k+1} - t_k)$$
    *   *Early AUC Window*: Integrated from $T_{offset}$ to $T_{offset} + D_{early\_auc}$ (where $D_{early\_auc}$ is `EARLY_AUC_DURATION_SEC`, default 6.0 seconds), computed for both normalized and raw constriction series. This window captures the combination of rapid cone/rod deactivate decay and early ipRGC-mediated activation.
    *   *Late AUC Window*: Integrated from $T_{offset} + T_{late\_start}$ to $T_{offset} + T_{late\_end}$ (where $T_{late\_start}$ is `LATE_AUC_START_SEC`, default 6.0 seconds, and $T_{late\_end}$ is `LATE_AUC_END_SEC`, default 12.0 seconds). This window isolates pure, sustained melanopsin-driven ipRGC activity.

4.  **Post-Illumination Pupillary Response (PIPR)**:
    PIPR is evaluated at $T_{offset} + T_{pipr}$ (where $T_{pipr}$ is `PIPR_TIME_SEC`, default 6.0 seconds):
    $$\text{PIPR}_{Normalized} = \text{NormalizedConstriction}_{T_{offset} + T_{pipr}}$$
    $$\text{PIPR}_{Raw} = \text{RawConstriction}_{T_{offset} + T_{pipr}}$$

### 3.3. Methodological Rationale for Dual-Metric Modeling
The analytical expansion to include raw physical metrics alongside normalized metrics provides significant methodological advantages:
*   **Inter-Individual Normalization**: Normalized metrics ($\text{NormalizedConstriction}$) eliminate anatomical variations in pupil sizes, allowing direct comparison of photoreceptor and ipRGC pathway sensitivity between different human subjects.
*   **Absolute Tracking and Biomechanical Modeling**: Raw metrics ($\text{RawConstriction}$) capture the physical extent of iris sphincter muscle displacement. This is vital for biomechanics of the iris, verifying sensor noise floors across the EyeLink tracking system, and assessing absolute constriction limits (to check if subjects approach mechanical saturation under bright duty cycle stimuli).

---

## 4. Current Progress Status & Upcoming Research Objectives

The major structural and operational goals planned for the previous phase have been fully realized. The experimental protocols have been successfully documented, bilingual training instructions are integrated, and the preprocessing and statistical pipelines are fully automated and parameterized.

### 4.1. Current Progress Checklist
- [x] **Pupillometry Study Protocol Standardization**: Completed the detailed, simplified experimental protocol in both English (`docs/en/pupil-experiment-protocol.md`) and Japanese (`docs/jp/実験手順(簡易版).docx`).
- [x] **Analytical Parameterization**: Engineered a global parameter configuration block in the statistical notebook to support flexible, adjustable time windows.
- [x] **Dual-Metric Analytical Suite**: Upgraded the computational engine to simultaneously extract both Normalized and Raw physical features (Baseline, Early AUC, Late AUC, and PIPR at customizable timeframes) to enable parallel biomechanical and physiological modeling.
- [x] **Tabular Feature Exporters**: Enhanced saving routines to output multi-metric summary tables directly into the centralized `out/` folder structure, fully verified through relative directory alignment.

### 4.2. Upcoming Research Objectives (Week 5–6)
1.  **Batch Processing of Duty-Cycle Datasets**: Utilize the finalized protocol to complete additional experimental recording runs across multiple participants. Process these new datasets in batch using the parameterized Colab and local statistical pipelines to verify individual responses under 25%, 50%, and 75% blue duty cycles.
2.  **Non-Linear Temporal Summation Modeling**: Conduct statistical modeling (e.g., repeated-measures ANOVA or non-linear curve fitting) on the extracted Early and Late AUC metrics to assess if ipRGC-mediated pupillary constriction scales linearly with duty-cycle light energy exposure or exhibits plateauing behaviors due to melanopsin pathway saturation.
3.  **Cross-Subject Visual Threshold Integrations**: Continue integrating the occipital EEG data (from the slower-frequency Phantom Array sessions) with the pupillary dynamics to map perisaccadic visual suppression thresholds against pupillary light-adaptation levels, building an integrated visual-autonomic model.
