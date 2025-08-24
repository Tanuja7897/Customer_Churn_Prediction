import os
from sklearn.model_selection import train_test_split
from .pipeline import build_preprocessor, build_model_pipeline
from .model import save_model

def train_model(X, y, model_save_path: str, test_size, random_state, stratify, model_params):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y if stratify else None
    )

    preprocessor = build_preprocessor(X_train)
    model_pipeline = build_model_pipeline(preprocessor, model_params=model_params)

    model_pipeline.fit(X_train, y_train)

    os.makedirs(os.path.dirname(model_save_path), exist_ok=True)
    save_model(model_pipeline, model_save_path)

    return model_pipeline, (X_test, y_test)
