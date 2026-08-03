# Usage Guide

This guide explains how to run the UCS Test Analyzer, what input data it requires, and what outputs it generates.

---

## 1. Basic Command

Run the analyzer from the project root:

```bash
python main.py --input <path-to-csv> --out-dir <output-folder>
```

Example:

```bash
python main.py --input examples/sample_ucs_data.csv --out-dir outputs

```

## 2. Input File Format

The input must be a CSV file containing at least:

- strain — dimensionless strain values
- stress — axial stress in MPa

Example:

```bash
strain,stress
0.0001,2.0
0.0002,4.1
0.0003,6.2
...

```

Notes:

- Data should be sorted by strain (the tool will sort if needed).
- Units must be consistent.
- Stress values should be positive and monotonic until peak stress.

## 3. Output Files

After running the tool, the output directory will contain:

1. stress_strain.png
   A plot showing:

- Stress–strain curve
- UCS point marked in red
- Axes labels and grid
- Title and legend

Useful for reports, presentations, and engineering documentation.

2. report.txt
   A text file summarizing:

- UCS (MPa)
- Young’s modulus (MPa)
- Strain at peak stress
- Notes about assumptions and methodology

This file is human‑readable and can be included in lab reports or project documentation.

## 4.Command-Line Options

| Option             | Description               | Required                |
| ------------------ | ------------------------- | ----------------------- |
| `--input` / `-i`   | Path to input CSV file    | Yes                     |
| `--out-dir` / `-o` | Directory to save outputs | No (default: `outputs`) |

## 5. Example Workflow

Step 1 — Prepare your CSV file
Place your UCS data inside examples/ or any folder you prefer.

Step 2 — Run the analyzer

```bash
python main.py --input examples/sample_ucs_data.csv --out-dir outputs
```

Step 3 — View results
Open:

- outputs/stress_strain.png
- outputs/report.txt

## 6. Troubleshooting

❗ “File not found”
Check that the CSV path is correct.

❗ “CSV must contain columns: strain, stress”
Ensure your CSV has exactly these column names.

❗ Plot not generated
Make sure matplotlib is installed:

```bash
pip install matplotlib
```
