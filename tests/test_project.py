from src.data import generate_demo_data, FEATURES, TARGET
from src.predict import predict_price

def test_demo_data_has_expected_columns():
    df = generate_demo_data(25)
    assert set(FEATURES + [TARGET]).issubset(df.columns)
    assert len(df) == 25
    assert (df[TARGET] > 0).all()

def test_prediction_is_positive():
    sample = {
        "city": "Hyderabad", "locality": "Gachibowli", "area_sqft": 1200,
        "bedrooms": 3, "bathrooms": 2, "balconies": 1, "floor": 3,
        "property_age": 5, "parking": 1, "furnishing": "Semi-furnished",
        "gated_community": 1, "near_metro": 0
    }
    assert predict_price(sample) > 0
