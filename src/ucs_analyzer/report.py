from pathlib import Path
from .analysis import UcsResults


def write_report(results: UcsResults, output_path: str = "outputs/report.txt") -> str:
    """
    Write a simple text report with UCS and Young's modulus.
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "UCS TEST ANALYSIS REPORT",
        "========================",
        "",
        f"Uniaxial Compressive Strength (UCS): {results.ucs_mpa:.2f} MPa",
        f"Young's Modulus (E): {results.youngs_modulus_mpa:.2f} MPa",
        f"Strain at UCS: {results.peak_strain:.6f}",
        "",
        "Notes:",
        "- Young's modulus estimated from initial elastic region (first ~30% of data).",
        "- Adjust method if your lab procedure differs.",
    ]

    Path(output_path).write_text("\n".join(lines), encoding="utf-8")
    return output_path
