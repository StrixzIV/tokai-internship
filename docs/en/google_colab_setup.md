# Google Colab Notebook Setup & Usage Guide

This documentation guides lab members through setting up and using the Google Colab notebook for parsing EyeLink `.asc` files and performing PCHIP blink interpolation.

The Colab notebook is located in the repository at:
`src/python/led-flash/colab_parsing_and_interpolation.ipynb`

---

## 1. Opening the Notebook in Google Colab

1. Open your web browser and go to [Google Colab](https://colab.research.google.com).
2. Sign in with your Google account.
3. In the pop-up dialog, select the **Upload** tab.
4. Drag and drop the `colab_parsing_and_interpolation.ipynb` file from your local repository, or click **Choose File** to browse and select it.

---

## 2. Step-by-Step Usage

The notebook is divided into four main steps. Run each cell sequentially by clicking the **Play (▶)** button on the left of each code cell.

### Step 1: Upload the EyeLink `.asc` File
- Run the code cell in **Step 1**.
- Click the **Choose Files** button that appears.
- Select the raw `.asc` file (e.g., `260611.asc`) exported from your EyeLink `.edf` file.
- The file will be uploaded into the Colab virtual environment memory.

### Step 2: Define & Run the Pipeline
- Run the code cell in **Step 2** to define the `parse_and_clean_asc` function and process the uploaded file.
- **Adjusting the Sliding Window (`SLIDING_WINDOW_SIZE`)**:
  - The default value is `200` (representing a 200 ms window at a 1000 Hz sampling rate).
  - *When to increase*: If you see the edges of blink artifacts dropping down toward zero in the plot, increase this value to `300` or higher to cover the eyelid closing/opening transitions.
  - *When to decrease*: If valid baseline pupil measurements are being cut off unnecessarily, decrease this value to `100` or `150`.
  - To change it, edit `SLIDING_WINDOW_SIZE = 200` in the cell code before running.

### Step 3: Visualize the Pupil Response
- Run the code cell in **Step 3** to plot the pupil diameter over time.
- **Verification**:
  - The **light gray line** shows the raw pupil size (with drops to `0` during blinks).
  - The **dark green line** shows the cleaned pupil size (smoothed over blinks using PCHIP interpolation).
  - The **shaded blue bands** mark the intervals when the blue LED stimulus was active (`blue_active = 1`).
  - Ensure the green line smoothly bridges the blink gaps without overshooting.

### Step 4: Export and Download
- Run the code cell in **Step 4**.
- The script will export the parsed and cleaned datasets into both CSV and Excel formats:
  - **Parsed Raw Data**: `<filename>_parsed.csv` & `<filename>_parsed.xlsx`
  - **Cleaned PCHIP Data**: `<filename>_cleaned.csv` & `<filename>_cleaned.xlsx`
- Colab will automatically trigger browser downloads to save these four files directly to your local machine.

---

## 3. Data Structure of the Output Files

The exported files contain the following columns:

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `timestamp` | Integer | Raw Eyelink recording timestamp (ms). |
| `elasped_ms` | Integer | Elapsed time in milliseconds from the start of the recording. |
| `elasped_sec` | Float | Elapsed time in seconds from the start of the recording. |
| `blue_active` | Binary (0/1) | Stimulus indicator (1 if Blue LED is active, 0 otherwise) reconstructed from Eyelink `BUTTON` events. |
| `gaze_x` | Float | Gaze horizontal coordinate (`NaN` during blinks). |
| `gaze_y` | Float | Gaze vertical coordinate (`NaN` during blinks). |
| `pupil_size` | Float | Raw pupil diameter (monocular left eye, `0.0` during blinks). |
| `cleaned_pupil_size` | Float | Cleaned pupil diameter after PCHIP blink interpolation (only in `_cleaned` files). |
