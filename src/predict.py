import pandas as pd
from .model import load_model

def predict_new_data(new_rows: pd.DataFrame, model_path: str):
    """
    new_rows: DataFrame with the SAME raw feature columns used in training (no 'Churn').
    model_path: where the trained pipeline was saved.
    """
    model = load_model(model_path)
    preds = model.predict(new_rows)
    return preds
