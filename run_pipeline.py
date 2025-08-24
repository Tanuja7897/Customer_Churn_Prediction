import yaml
from src.data_preprocessing import load_raw_data, clean_and_encode, split_X_y
from src.train import train_model
from src.evaluate import evaluate_model

def main():
    with open("config/config.yaml", "r") as f:
        cfg = yaml.safe_load(f)

    # Load + clean
    df_raw_data = load_raw_data(cfg["data"]["raw_path"])
    df = clean_and_encode(df_raw_data)
    X, y = split_X_y(df, target="Churn")

    # Train + save
    model, (X_test, y_test) = train_model(
        X, y,
        model_save_path=cfg["model"]["save_path"], #pass location to save the model
        test_size=cfg["train"]["test_size"],
        random_state=cfg["train"]["random_state"],
        stratify=cfg["train"]["stratify"],
        model_params=cfg["model"]["params"]
    )

    # Evaluate
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
