# Local Environment Setup & Usage Guide

Welcome to the Tokai University Human Information Science Lab (Takao Laboratory) research repository. This guide is designed to help the next researcher set up their local Python environment and understand how to run the data analysis pipelines.

This repository hosts two primary research projects under `src/python/`:
1. **`led-flash`**: Pupillometry analysis for the blue/green flashing light experiment (melanopsin bistability).
2. **`phantom-array-experiment`**: EEG/EOG saccade detection and labeling for the phantom array effect study using `mne-python`.

---

## 1. Prerequisites

Before setting up the environment, ensure you have the following installed on your machine:
- **Python 3.8 or higher** (Python 3.10+ recommended). You can verify your version by running:
  ```bash
  python3 --version
  ```
- **Git** (to clone and manage the repository).

---

## 2. Automated Virtual Environment Setup

To simplify dependency management and avoid package conflicts, we use a virtual environment (`.venv`) and a single consolidated `requirements.txt` file at the root of the repository.

We provide an automated setup script that works across macOS, Linux, and Windows.

### UNIX (macOS and Linux)
Open your terminal, navigate to the repository root, and run:
```bash
./setup_venv.sh
```
*Note: If you get a permission error, run `chmod +x setup_venv.sh` first.*

### Windows
Open Command Prompt (cmd) or PowerShell, navigate to the repository root, and run:
```cmd
setup_venv.bat
```

### Direct Python Execution (Any OS)
If you prefer, you can run the python installer script directly:
```bash
python setup_venv.py
```

### What the Script Does:
1. Verifies that Python 3.8+ is installed.
2. Creates a virtual environment in the `.venv` directory.
3. Upgrades `pip` and `setuptools` to their latest versions.
4. Installs all packages specified in the global `requirements.txt`.

---

## 3. Manual Virtual Environment Setup (Alternative)

If you prefer to set up the environment manually without using the scripts:

1. **Create the virtual environment:**
   ```bash
   python -m venv .venv
   ```
2. **Activate the environment:**
   - **macOS/Linux**: `source .venv/bin/activate`
   - **Windows CMD**: `.venv\Scripts\activate.bat`
   - **Windows PowerShell**: `.\.venv\Scripts\Activate.ps1`
3. **Upgrade core package tools:**
   ```bash
   pip install --upgrade pip setuptools
   ```
4. **Install all packages:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 4. Environment Activation & Verification

After setup, you must activate the virtual environment **every time** you open a new terminal window to work on the repository.

### Activation Commands:
- **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```
- **Windows CMD**:
  ```cmd
  .venv\Scripts\activate.bat
  ```
- **Windows PowerShell**:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```

Once activated, your terminal prompt will show `(.venv)` at the beginning.

### Verification:
Verify the installation of core research libraries:
```bash
python -c "import mne, pandas, numpy, scipy, matplotlib, japanize_matplotlib, pymatreader; print('All libraries imported successfully!')"
```

---

## 5. Running the Data Analysis

To run and edit the Jupyter notebooks (`.ipynb`), activate the virtual environment and start the Jupyter Notebook server:
```bash
jupyter notebook
```
This will open the Jupyter interface in your default web browser.

### Key Notebooks & Scripts

#### 1. Pupillometry Analysis (`src/python/led-flash/`)
- **[parse_asc.py](file:///Users/jikaewsi/Documents/code_and_scripts/tokai-internship/src/python/led-flash/parse_asc.py)**: Python script to parse EyeLink `.asc` files, extract pupil size data, and reconstruct blue LED stimulus periods.
- **[colab_parsing_and_interpolation.ipynb](file:///Users/jikaewsi/Documents/code_and_scripts/tokai-internship/src/python/led-flash/colab_parsing_and_interpolation.ipynb)**: An interactive pipeline for uploading raw EyeLink data, performing PCHIP blink interpolation, visualizing raw vs. cleaned data, and exporting clean CSV files.
- **[statistical_evaluation.ipynb](file:///Users/jikaewsi/Documents/code_and_scripts/tokai-internship/src/python/led-flash/statistical_evaluation.ipynb)**: Implements statistical metrics (baseline pupil diameter, normalized constriction rate, early/late AUC, and 6s PIPR) and generates publication-ready plots.

#### 2. EEG/EOG Saccade Detection (`src/python/phantom-array-experiment/`)
- **[detect_saccades.py](file:///Users/jikaewsi/Documents/code_and_scripts/tokai-internship/src/python/phantom-array-experiment/detect_saccades.py)**: Python implementation of the EOG-based saccade detection pipeline (bandpass filtering, differentiation, peak finding, and morphological noise-rejection quality gates).
- **[visualize_saccades.ipynb](file:///Users/jikaewsi/Documents/code_and_scripts/tokai-internship/src/python/phantom-array-experiment/visualize_saccades.ipynb)**: Visualizes detected saccades overlaid on raw EOG signals to inspect the detection quality.
- **[ssvep.ipynb](file:///Users/jikaewsi/Documents/code_and_scripts/tokai-internship/src/python/phantom-array-experiment/ssvep.ipynb)**: Contains the main EEG signal processing, spectrum calculations, and SSVEP (Steady-State Visually Evoked Potential) analysis.

---

## 6. Troubleshooting Notes

### 3D Visualization in MNE-Python
The `phantom-array-experiment` uses packages like `mne-qt-browser`, `pyqt6`, `pyvista`, and `vtk` for advanced interactive plots (e.g. 3D sensor layout, head models). 
- If you run into OpenGL or display errors (especially on virtual environments, headless Linux servers, or remote SSH connections), you can fall back to standard 2D matplotlib plotting in MNE:
  ```python
  import mne
  mne.viz.set_browser_backend('matplotlib')
  ```

### Japanese Font Rendering
`japanize-matplotlib` is installed to ensure Japanese characters render properly in matplotlib charts. It is automatically imported in the notebooks. If you add new notebooks, make sure to include `import japanize_matplotlib` before plotting text in Japanese.
