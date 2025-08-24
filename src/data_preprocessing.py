import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_raw_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def clean_and_encode(df: pd.DataFrame) -> pd.DataFrame:
    # Drop ID
    if "customerID" in df.columns:
        df = df.drop(columns=["customerID"])

    # fill NaN (new customers) with 0
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = df["TotalCharges"].fillna(0)

    # Label-encode target Churn: Yes->1, No->0
    if "Churn" not in df.columns:
        raise ValueError("Target column 'Churn' not found.")
    le = LabelEncoder()
    df["Churn"] = le.fit_transform(df["Churn"])

    return df

def split_X_y(df: pd.DataFrame, target: str = "Churn"):
    X = df.drop(columns=[target])
    y = df[target]
    return X, y
