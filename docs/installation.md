# Installation Guide

This document explains how to install and run the UCS Test Analyzer on your system.

---

## 1. Requirements

To use this project, you need:

- Python 3.8 or newer
- pip (Python package manager)
- Git (optional, for cloning the repository)

---

## 2. Download the Project

### Option A — Clone from GitHub (recommended)

```bash
git clone https://github.com/<your-username>/ucs-test-analyzer.git
cd ucs-test-analyzer

```

### Option B — Download ZIP

1. Go to the repository page
2. Click Code → Download ZIP
3. Extract the ZIP file
4. Open a terminal inside the extracted folder

## 3. Create a Virtual Environment

Creating a virtual environment keeps dependencies isolated.

- Windows

```bash
python -m venv venv
venv\Scripts\activate
```

- macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Install Dependencies

All required packages are listed in requirements.txt.

```bash
pip install -r requirements.txt

```

This installs:

- pandas
- numpy
- matplotlib

## 5. Verify Installation

Run:

```bash
python main.py --help
```

You should see the command‑line help message.
If yes, the installation is complete.

## 6. Next Steps

Proceed to the Usage Guide to learn how to run the analyzer on your UCS data.
