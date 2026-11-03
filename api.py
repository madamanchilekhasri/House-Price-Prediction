from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from src.predict import predict_price
from src.data import CITIES, LOCALITIES

app = FastAPI(title="House Price Prediction API", version="1.0.0",
              description="Demo API; predictions use synthetic sample data.")

class HouseInput(BaseModel):
    city: str = "Hyderabad"
    locality: str = "Gachibowli"
    area_sqft: int = Field(1200, ge=250, le=20000)
    bedrooms: int = Field(3, ge=1, le=10)
    bathrooms: int = Field(2, ge=1, le=10)
    balconies: int = Field(1, ge=0, le=10)
    floor: int = Field(3, ge=0, le=100)
    property_age: int = Field(5, ge=0, le=150)
    parking: int = Field(1, ge=0, le=10)
    furnishing: str = "Semi-furnished"
    gated_community: int = Field(1, ge=0, le=1)
    near_metro: int = Field(0, ge=0, le=1)

@app.get("/")
def home():
    return {"message": "House Price Prediction API", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(house: HouseInput):
    try:
        price = predict_price(house.model_dump())
        return {"predicted_price_inr": round(price, 2), "price_lakh": round(price / 100000, 2),
                "note": "Demo estimate from synthetic data; not a market valuation."}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
