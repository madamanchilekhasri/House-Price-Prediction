# Grafana starter notes
1. Start Prometheus and Grafana in your environment.
2. Add Prometheus as a Grafana data source.
3. Create panels for API request count, request latency, error rate, and prediction distribution.
4. The starter API does not expose Prometheus metrics yet; add `prometheus-fastapi-instrumentator` to expose `/metrics` before expecting application panels.
