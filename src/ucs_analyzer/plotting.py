from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from .analysis import UcsResults


def plot_stress_strain(
    df: pd.DataFrame,
    results: UcsResults,
    output_path: str = "outputs/stress_strain.png",
) -> str:
    """
    Plot stress-strain curve and mark UCS point.
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(df["strain"], df["stress"], label="Stress-Strain", color="blue")

    # Mark UCS point
    ax.scatter(
        results.peak_strain,
        results.ucs_mpa,
        color="red",
        label=f"UCS = {results.ucs_mpa:.2f} MPa",
    )

    ax.set_xlabel("Strain (dimensionless)")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title("UCS Test - Stress-Strain Curve")
    ax.legend()
    ax.grid(True)

    fig.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)

    return output_path
