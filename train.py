from pathlib import Path
import json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from src.data import get_training_data, FEATURES, TARGET
from src.preprocess import build_model
from src.tracking import log_with_mlflow

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "models" / "house_price_model.joblib"
METRICS_PATH = ROOT / "models" / "metrics.json"

def train():
    df = get_training_data()
    X, y = df[FEATURES], df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = build_model()
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    metrics = {
        "mae_inr": float(mean_absolute_error(y_test, pred)),
        "rmse_inr": float(mean_squared_error(y_test, pred) ** 0.5),
        "r2": float(r2_score(y_test, pred)),
        "rows": int(len(df))
    }
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    METRICS_PATH.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print("Model saved to:", MODEL_PATH)
    print(json.dumps(metrics, indent=2))
    print(log_with_mlflow({"model": "RandomForestRegressor"}, metrics, model))
    return model, metrics

if __name__ == "__main__":
    train()
