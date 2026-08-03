import argparse
from pathlib import Path

from src.ucs_analyzer import (
    load_ucs_data,
    compute_ucs_and_modulus,
    plot_stress_strain,
    write_report,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="UCS Test Analyzer - Stress-Strain Data"
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Path to CSV file with columns: strain, stress",
    )
    parser.add_argument(
        "--out-dir",
        "-o",
        default="outputs",
        help="Directory to save plots and report",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    input_path = args.input
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    df = load_ucs_data(input_path)
    results = compute_ucs_and_modulus(df)

    plot_path = out_dir / "stress_strain.png"
    report_path = out_dir / "report.txt"

    plot_stress_strain(df, results, output_path=str(plot_path))
    write_report(results, output_path=str(report_path))

    print("Analysis complete.")
    print(f"UCS: {results.ucs_mpa:.2f} MPa")
    print(f"Young's Modulus: {results.youngs_modulus_mpa:.2f} MPa")
    print(f"Plot saved to: {plot_path}")
    print(f"Report saved to: {report_path}")


if __name__ == "__main__":
    main()
