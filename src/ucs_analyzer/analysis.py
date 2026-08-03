import numpy as np
import pandas as pd
from dataclasses import dataclass


@dataclass
class UcsResults:
    ucs_mpa: float
    youngs_modulus_mpa: float
    peak_strain: float


def compute_ucs_and_modulus(df: pd.DataFrame) -> UcsResults:
    """
    Compute UCS and Young's modulus from stress-strain data.

    - UCS: maximum stress
    - Young's modulus: linear fit on initial elastic region
    """
    stress = df["stress"].values
    strain = df["strain"].values

    # UCS and peak strain
    max_idx = np.argmax(stress)
    ucs_mpa = float(stress[max_idx])
    peak_strain = float(strain[max_idx])

    # Elastic region: first 30% of data (simple assumption)
    n = len(df)
    elastic_end = max(3, int(0.3 * n))  # at least 3 points
    elastic_strain = strain[:elastic_end]
    elastic_stress = stress[:elastic_end]

    # Linear regression: stress = E * strain + b
    coeffs = np.polyfit(elastic_strain, elastic_stress, 1)
    youngs_modulus_mpa = float(coeffs[0])

    return UcsResults(
        ucs_mpa=ucs_mpa,
        youngs_modulus_mpa=youngs_modulus_mpa,
        peak_strain=peak_strain,
    )
