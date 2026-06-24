# Tokai-KMITL Collaborative Research Internship (May 18 – June 24, 2026)
**Automating Ocular Tracking in Phantom Array Psychophysics & Pupillometry Bistability Analysis**

A joint research program between the **Tokai Data Science and Brain Lab** (Department of Human Information Science, Tokai University, Japan) and **King Mongkut's Institute of Technology Ladkrabang** (KMITL, Thailand).

---

## Language / 言語
- [English Version](#english-version)
- [日本語版 (Japanese Version)](#日本語版-japanese-version)

---

# English Version

## 📌 Executive Summary
This repository contains the computational pipelines, experimental protocols, and analysis workflows developed during the 6-week research internship. The project focuses on two primary areas of ocular and neurophysiological research:
1. **Ocular Tracking & EEG/EOG in Phantom Array Psychophysics**: Automating the detection of saccades to analyze perisaccadic occipital gamma-band (40–100 Hz) spectral activations during flickering visual stimuli.
2. **Melanopsin Bistability & Pupillometry Analysis**: Standardizing EyeLink 1000 Plus experimental runs, replacing legacy VBA tools with a Python/Colab preprocessing pipeline, and extracting parameterized statistical metrics of pupil constriction to study ipRGC kinetics.

For detailed weekly updates, see the [Weekly Progress Reports](docs/weekly-progress-report/).

---

## 📁 Repository Directory Structure

```directory
tokai-internship/
├── requirements.txt         # Consolidated Python dependencies
├── setup_venv.py            # Python installer script for virtual environments
├── setup_venv.sh            # UNIX shell wrapper for environment setup
├── setup_venv.bat           # Windows Command Prompt wrapper for environment setup
├── data/                    # Raw EEG/EOG .set/.fdt files and pupil recordings (git-ignored)
├── out/                     # Generated statistical metrics, Excel sheets, and plots (git-ignored)
├── docs/                    # Experimental protocols, setup guides, and reports
│   ├── en/                  # English documentation
│   │   ├── pupil-experiment-protocol.md       # Standard EyeLink 1000 Plus trial protocol
│   │   ├── blue_duty_cycle_pupil_protocol.md  # Physiological overview of duty cycle study
│   │   ├── saccade_detection.md               # Saccade detection pipeline details
│   │   ├── local_setup_guide.md               # Local Python environment guide
│   │   └── google_colab_setup.md              # Google Colab notebook usage guide
│   ├── jp/                  # Japanese documentation (Japanese localized guides)
│   │   ├── ローカル環境セットアップガイド.md
│   │   ├── Google_Colab_セットアップガイド.md
│   │   ├── saccade_detection.md
│   │   └── 実験手順(簡易版).docx               # Microsoft Word simplified experimental protocol
│   └── weekly-progress-report/                # Weekly progress reports (Weeks 1 to 5)
└── src/                     # Source code files
    ├── matlab/              # MATLAB utilities for importing events into EEGLAB
    │   └── clear_annotation.m
    └── python/              # Primary computational pipelines
        ├── led-flash/       # Pupillometry analysis tools
        │   ├── parse_asc.py                      # Command-line EyeLink ASC file parser
        │   ├── colab_parsing_and_interpolation.ipynb # Google Colab blink cleanup pipeline
        │   └── statistical_evaluation.ipynb      # Parameterized pupillary feature extractor
        └── phantom-array-experiment/ # EEG/EOG saccade tools
            ├── detect_saccades.py                # EOG velocity-based saccade detector
            ├── add_saccade_events.m              # Generated EEGLAB event-insertion script
            ├── visualize_saccades.ipynb          # Visual validation of saccades
            └── ssvep.ipynb                       # Occipital EEG spectral & SSVEP analysis
```

---

## 👁️ Project 1: Phantom Array Experiment (PAE)
* **Background**: Investigates the *phantom array effect*—a visual illusion where subjects perceive duplicated copies of an LED stimulus due to rapid eye movements (saccades) breaking temporal fusion.
* **Saccade Detection**: Implements an automated EOG velocity-based detector in [detect_saccades.py](src/python/phantom-array-experiment/detect_saccades.py) using `mne-python`. It filters out noise using 6 morphological/statistical quality gates and exports a MATLAB script ([add_saccade_events.m](src/python/phantom-array-experiment/add_saccade_events.m)) to load events into EEGLAB.
* **Neurophysiological Findings**: Isolated a distinct perisaccadic spectral signature of the PAE in the high-gamma band (40–100 Hz) on the occipital Oz channel during 80 Hz and 160 Hz flickering stimuli.
* **Detailed Documentation**: See [docs/en/saccade_detection.md](docs/en/saccade_detection.md) and [src/python/phantom-array-experiment/](src/python/phantom-array-experiment/).

---

## ⚡ Project 2: Melanopsin Bistability & Pupillometry
* **Background**: Investigates intrinsically photosensitive retinal ganglion cell (ipRGC) kinetics, focusing on the bistability of melanopsin under blue/green LED pairings and temporal integration under varying blue light duty cycles (25%, 50%, 75%).
* **Ocular Preprocessing**: Implements EyeLink ASC parser ([parse_asc.py](src/python/led-flash/parse_asc.py)) and a Google Colab notebook ([colab_parsing_and_interpolation.ipynb](src/python/led-flash/colab_parsing_and_interpolation.ipynb)) for PCHIP blink interpolation, boundary edge-stabilization, and calibration gating.
* **Dual-Metric Evaluation**: Features a parameterized configuration block in [statistical_evaluation.ipynb](src/python/led-flash/statistical_evaluation.ipynb) to compute both Normalized and Raw physical pupil constriction metrics (Baseline size, Early/Late AUC, and 6s PIPR).
* **Detailed Documentation**: See [docs/en/pupil-experiment-protocol.md](docs/en/pupil-experiment-protocol.md), [docs/en/blue_duty_cycle_pupil_protocol.md](docs/en/blue_duty_cycle_pupil_protocol.md), and [src/python/led-flash/](src/python/led-flash/).

---

## 🛠️ Environment Setup & Installation
The repository features an automated installer script that compiles Python dependencies in [requirements.txt](requirements.txt).
* **UNIX (macOS / Linux)**: Run `./setup_venv.sh`
* **Windows**: Run `setup_venv.bat`
* **For detailed setup instructions**: See the [Local Setup Guide](docs/en/local_setup_guide.md) or [Google Colab Setup Guide](docs/en/google_colab_setup.md).

---

# 日本語版 (Japanese Version)

## 📌 総括（エグゼクティブ・サマリー）
本リポジトリは、6週間にわたる共同研究インターンシップにおいて開発されたデータ解析パイプライン、実験プロトコル、および自動化ワークフローを含んでいます。本プログラムは以下の2つの主要テーマを対象としています。
1. **ファントムアレイ精神物理学実験における眼球運動測定とEEG/EOG解析**: 点滅光刺激下におけるサッケード（急速眼球運動）の自動検出、および周サッケード期における一次視覚野（Ozチャンネル）の高周波ガンマ帯域（40-100 Hz）の活性化を解析しました。
2. **メラノプシン・バイスタビリティと瞳孔径解析**: EyeLink 1000 Plusを用いた実験手順を標準化し、従来のVBAツールからPython/Colabによる前処理パイプラインへ移行。パラメータ化された統計評価エンジンを構築し、ipRGC（内在性光受容網膜神経節細胞）の特性を評価しました。

週次の進捗詳細については、[週次進捗報告書](docs/weekly-progress-report/)をご参照ください。

---

## 📁 リポジトリ・ディレクトリ構造
本プロジェクトの全体構成は、上記の [Repository Directory Structure](#directory-structure) をご参照ください。日本語localizedドキュメントは [docs/jp/](docs/jp/) 配下に格納されています。

---

## 👁️ プロジェクト 1: ファントムアレイ実験 (PAE)
* **概要**: 急速眼球運動（サッケード）中に点滅光の空間的残像が複数知覚される「ファントムアレイ効果」について、脳の視覚抑制をバイパスする仕組みを解明する実験。
* **サッケード検出**: EOG（眼電図）を対象とした自動検出スクリプト（[detect_saccades.py](src/python/phantom-array-experiment/detect_saccades.py)）をPythonで構築。6つのノイズ判定ゲート群により筋肉のノイズや瞬きを排除し、検出されたイベントをEEGLABにインポートするMATLABスクリプト（[add_saccade_events.m](src/python/phantom-array-experiment/add_saccade_events.m)）を出力します。
* **神経生理学的知見**: 80 Hzおよび160 Hzの点滅刺激において、サッケード前後の一次視覚野で特異的なガンマ帯域（40-100 Hz）の活性化（脳内周サッケード抑制の突破現象）を同定しました。
* **詳細情報**: [docs/jp/saccade_detection.md](docs/jp/saccade_detection.md) および [src/python/phantom-array-experiment/](src/python/phantom-array-experiment/) をご参照ください。

---

## ⚡ プロジェクト 2: メラノプシン・バイスタビリティと瞳孔解析
* **概要**: 青色（短波長）および緑色（中波長）LED刺激ペアを用いたメラノプシンの双安定性回帰、ならびに異なる青色デューティ比（25%, 50%, 75%）におけるipRGC光エネルギー時間積分および受容経路の飽和特性の解明。
* **前処理パイプライン**: EyeLink ASCパース用の [parse_asc.py](src/python/led-flash/parse_asc.py) および、瞬きのPCHIP（エルミート）補間、端点発散防止、キャリブレーションデータ除去を実行するGoogle Colabノートブック（[colab_parsing_and_interpolation.ipynb](src/python/led-flash/colab_parsing_and_interpolation.ipynb)）を開発。
* **デュアル指標統計解析**: [statistical_evaluation.ipynb](src/python/led-flash/statistical_evaluation.ipynb) にて基準瞳孔径、標準化収縮率（Normalized）および物理的収縮量（Raw）の双方で初期/後期AUCおよび6秒PIPRを算出。
* **詳細情報**: [docs/jp/実験手順(簡易版).docx](docs/jp/実験手順(簡易版).docx)（簡易版実験マニュアル）、[docs/en/blue_duty_cycle_pupil_protocol.md](docs/en/blue_duty_cycle_pupil_protocol.md)、および [src/python/led-flash/](src/python/led-flash/) をご参照ください。

---

## 🛠️ 環境構築とインストール
本リポジトリには、[requirements.txt](requirements.txt) に記載されたパッケージ依存関係を自動構築するスクリプトが含まれています。
* **UNIX (macOS / Linux)**: `./setup_venv.sh` を実行
* **Windows**: `setup_venv.bat` を実行
* **環境構築の詳細手順**: [ローカル環境セットアップガイド](docs/jp/ローカル環境セットアップガイド.md) または [Google Colabセットアップガイド](docs/jp/Google_Colab_セットアップガイド.md) をご参照ください。

---
