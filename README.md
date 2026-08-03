# UCS Test Analyzer

A small, professional Python tool for analyzing **uniaxial compressive strength (UCS)** test data.

It reads stress–strain data from a CSV file, computes:

- Uniaxial Compressive Strength (UCS)
- Young's modulus (from the initial elastic region)
- Strain at peak stress

and generates:

- A **stress–strain plot** with UCS marked
- A **text report** summarizing key parameters

---

## Project structure

```text
ucs-test-analyzer/
├── src/ucs_analyzer/        # Core logic
│   ├── __init__.py
│   ├── data_loader.py       # CSV loading and validation
│   ├── analysis.py          # UCS & Young's modulus calculation
│   ├── plotting.py          # Stress–strain plotting
│   └── report.py            # Text report generation
├── examples/                # Sample input data
│   └── sample_ucs_data.csv
├── main.py                  # CLI entry point
├── requirements.txt         # Python dependencies
├── .gitignore
└── README.md
```

## Documentation

Full documentation is available in the `docs/` folder:

- [Overview](docs/overview.md)
- [Installation](docs/installation.md)
- [Usage](docs/usage.md)
- [Methodology](docs/methodology.md)
- [Data Format](docs/data_format.md)
- [Changelog](docs/changelog.md)
