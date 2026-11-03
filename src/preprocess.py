from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from src.data import FEATURES

CATEGORICAL = ["city", "locality", "furnishing"]
NUMERIC = [c for c in FEATURES if c not in CATEGORICAL]

def build_model():
    numeric_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])
    categorical_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])
    prep = ColumnTransformer([
        ("numeric", numeric_pipe, NUMERIC),
        ("categorical", categorical_pipe, CATEGORICAL)
    ])
    model = RandomForestRegressor(
        n_estimators=180, max_depth=18, min_samples_leaf=2,
        random_state=42, n_jobs=-1
    )
    return Pipeline([("preprocess", prep), ("model", model)])
