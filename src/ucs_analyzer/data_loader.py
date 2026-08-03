import pandas as pd
from pathlib import Path


def load_ucs_data(csv_path: str) -> pd.DataFrame:
    """
    Load UCS test data from a CSV file.

    Expected columns:
    - strain
    - stress
    """
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {csv_path}")

    df = pd.read_csv(path)

    required_cols = {"strain", "stress"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"CSV must contain columns: {required_cols}")

    # Sort by strain just in case
    df = df.sort_values("strain").reset_index(drop=True)
    return df
