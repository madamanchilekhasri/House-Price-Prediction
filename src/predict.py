from pathlib import Path
import joblib
import pandas as pd
from src.data import FEATURES, ensure_dataset
from src.preprocess import build_model

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "house_price_model.joblib"

def get_model():
    ensure_dataset()
    if not MODEL_PATH.exists():
        from train import train
        train()
    return joblib.load(MODEL_PATH)

def predict_price(payload):
    missing = [c for c in FEATURES if c not in payload]
    if missing:
        raise ValueError("Missing fields: " + ", ".join(missing))
    row = pd.DataFrame([{c: payload[c] for c in FEATURES}])
    model = get_model()
    return max(0, float(model.predict(row)[0]))
