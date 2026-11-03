from pathlib import Path
import numpy as np
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "house_prices.csv"

CITIES = ["Hyderabad", "Bengaluru", "Chennai", "Pune", "Vijayawada"]
LOCALITIES = [
    "Gachibowli", "Kondapur", "Miyapur", "Kukatpally", "Uppal",
    "Madhapur", "Manikonda", "LB Nagar", "Whitefield", "Electronic City",
    "Anna Nagar", "OMR", "Wakad", "Hinjewadi", "Benz Circle"
]
CITY_FACTORS = {"Hyderabad": 1.00, "Bengaluru": 1.08, "Chennai": 0.92, "Pune": 0.95, "Vijayawada": 0.62}
LOCALITY_FACTORS = {
    "Gachibowli": 1.35, "Kondapur": 1.22, "Miyapur": 0.88, "Kukatpally": 0.94,
    "Uppal": 0.78, "Madhapur": 1.40, "Manikonda": 1.02, "LB Nagar": 0.80,
    "Whitefield": 1.25, "Electronic City": 0.90, "Anna Nagar": 1.20, "OMR": 1.05,
    "Wakad": 1.02, "Hinjewadi": 0.88, "Benz Circle": 1.10
}

FEATURES = [
    "city", "locality", "area_sqft", "bedrooms", "bathrooms", "balconies",
    "floor", "property_age", "parking", "furnishing", "gated_community", "near_metro"
]
TARGET = "price_inr"

def generate_demo_data(n=1800, seed=42):
    rng = np.random.default_rng(seed)
    cities = rng.choice(CITIES, n)
    localities = rng.choice(LOCALITIES, n)
    area = rng.integers(450, 3201, n)
    bedrooms = np.clip(np.round(area / 520 + rng.normal(0, 0.7, n)), 1, 6).astype(int)
    bathrooms = np.clip(bedrooms + rng.integers(-1, 2, n), 1, 6)
    balconies = rng.integers(0, 4, n)
    floor = rng.integers(0, 26, n)
    age = rng.integers(0, 31, n)
    parking = rng.integers(0, 3, n)
    furnishing = rng.choice(["Unfurnished", "Semi-furnished", "Fully furnished"], n, p=[0.4, 0.4, 0.2])
    gated = rng.integers(0, 2, n)
    metro = rng.integers(0, 2, n)
    city_factor = np.array([CITY_FACTORS[x] for x in cities])
    loc_factor = np.array([LOCALITY_FACTORS[x] for x in localities])
    furnishing_factor = np.select(
        [furnishing == "Fully furnished", furnishing == "Semi-furnished"],
        [1.12, 1.05], default=1.0
    )
    base = area * 4200 * city_factor * loc_factor * furnishing_factor
    price = (base + bedrooms * 180000 + bathrooms * 90000 + balconies * 35000
             + floor * 7000 + parking * 180000 + gated * 250000 + metro * 160000
             - age * 25000 + rng.normal(0, 450000, n))
    df = pd.DataFrame({
        "city": cities, "locality": localities, "area_sqft": area,
        "bedrooms": bedrooms, "bathrooms": bathrooms, "balconies": balconies,
        "floor": floor, "property_age": age, "parking": parking,
        "furnishing": furnishing, "gated_community": gated, "near_metro": metro,
        "price_inr": np.maximum(price, 1200000).astype(int)
    })
    return df

def ensure_dataset():
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_PATH.exists():
        generate_demo_data().to_csv(DATA_PATH, index=False)
    return pd.read_csv(DATA_PATH)

def get_training_data():
    df = ensure_dataset()
    required = FEATURES + [TARGET]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing required columns: {', '.join(missing)}")
    return df[required].dropna()
