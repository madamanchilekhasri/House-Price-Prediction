# House Price Prediction with MLOps (Beginner-Friendly)

A small, runnable house-price prediction project with a web form. Select property details such as area (sq.ft), locality, bedrooms, bathrooms, balconies, parking, floor, property age, and furnishing to get an estimated price in Indian rupees.

> **Important:** The included dataset is synthetic/demo data so the project runs immediately. Predictions are for learning and demonstration only, not real property valuations. Replace `data/house_prices.csv` with a reliable local dataset before using it for real decisions.

## Fastest way to run (Windows / VS Code)

1. Install Python 3.10 or 3.11.
2. Extract this ZIP.
3. Open the extracted `house_price_prediction_mlops` folder in VS Code.
4. Open Terminal → New Terminal and run:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks activation, use Command Prompt in VS Code, or run `.venv\Scripts\python.exe -m pip install -r requirements.txt` and `.venv\Scripts\python.exe -m streamlit run app.py`.

The app opens in your browser. The first run creates a demo dataset and trains a model automatically. No separate training step is needed.

## Quick run without Streamlit (optional)

```bash
pip install -r requirements.txt
python train.py
```

## 10 project modules

1. **Data generation/loading** — `src/data.py`
2. **Data preprocessing** — `src/preprocess.py`
3. **Exploratory analysis** — `notebooks/01_exploration.ipynb` and charts in the app
4. **Model training/evaluation** — `train.py` (Random Forest; XGBoost optional)
5. **Interactive prediction UI** — `app.py`
6. **REST prediction API** — `api.py` (FastAPI)
7. **Experiment tracking** — `src/tracking.py` (MLflow optional)
8. **Data/model versioning** — `dvc.yaml`, `.dvc/config.example`
9. **Testing and automation** — `tests/`, `.github/workflows/ci.yml`
10. **Container, monitoring, and cloud deployment templates** — `Dockerfile`, `docker-compose.yml`, `k8s/`, `helm/`, `monitoring/`, `terraform/`

## Input features

- City, locality/area
- Built-up area in square feet
- Bedrooms, bathrooms, balconies
- Floor number
- Property age
- Parking spaces
- Furnishing level
- Gated community
- Nearby metro

## Optional MLOps tools

The core app uses Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Streamlit, and FastAPI. Optional integrations are provided for XGBoost, MLflow, DVC, Evidently, Docker, Kubernetes/Helm, Prometheus/Grafana, AWS, Terraform, Git, GitHub and Jupyter.

You do **not** need to install Kubernetes, AWS, Terraform, MLflow, DVC, or Evidently to run the beginner app. Those are deployment/extension templates.

### Optional API

```bash
uvicorn api:app --reload
```

Open `http://127.0.0.1:8000/docs`.

### Run tests

```bash
pytest -q
```

### Train and track a model (optional)

```bash
python train.py
mlflow ui
```

### DVC (optional)

```bash
dvc init
dvc repro
```

### Docker (optional)

```bash
docker build -t house-price-predictor .
docker run -p 8501:8501 house-price-predictor
```

## Project structure

```text
house_price_prediction_mlops/
├── app.py
├── api.py
├── train.py
├── requirements.txt
├── data/
├── models/
├── src/
├── tests/
├── notebooks/
├── monitoring/
├── k8s/
├── helm/
├── terraform/
└── .github/workflows/
```

## Notes

- Prices are in INR and shown in lakhs/crores for readability.
- The demo data is generated from a simple formula with noise, so metrics only validate the example workflow.
- Locality price factors are illustrative. Replace them with verified data for your target city.
