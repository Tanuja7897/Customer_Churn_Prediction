import pandas as pd
import numpy as np

def load_data(path: str) -> pd.DataFrame:
    """Load churn dataset"""
    return pd.read_csv(path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """cleaning: drop IDs, handle missing, convert target(Label Encodaing)"""
    if "customerID" in df.columns:
        df = df.drop("customerID", axis=1)

    df = df.fillna(0)

    if "Churn" in df.columns:
        df["Churn"] = np.where(df["Churn"] == "Yes", 1, 0)

    return df
