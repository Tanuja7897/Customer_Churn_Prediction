import joblib

def save_model(model, path: str):
    joblib.dump(model, path)
    print(f"Model saved to {path}")

def load_model(path: str):
    return joblib.load(path)
