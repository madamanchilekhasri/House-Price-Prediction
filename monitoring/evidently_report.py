"""Optional data-drift report starter. Install evidently and supply real reference/current CSVs."""
def create_report(reference_csv="data/house_prices.csv", current_csv="data/current_predictions.csv"):
    import pandas as pd
    from evidently.report import Report
    from evidently.metric_preset import DataDriftPreset
    reference = pd.read_csv(reference_csv)
    current = pd.read_csv(current_csv)
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=reference, current_data=current)
    report.save_html("monitoring/data_drift_report.html")

if __name__ == "__main__":
    create_report()
