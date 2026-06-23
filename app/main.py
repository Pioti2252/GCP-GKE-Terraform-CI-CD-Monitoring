from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)

metrics = PrometheusMetrics(app)

metrics.info(
    "app_info",
    "Application info",
    version=os.getenv("APP_VERSION", "dev"),
    environment=os.getenv("APP_ENV", "local")
)


@app.get("/")
def read_root():
    return jsonify({
        "app": os.getenv("APP_NAME", "GCP DevOps Showcase App"),
        "environment": os.getenv("APP_ENV", "local"),
        "version": os.getenv("APP_VERSION", "dev")
    })


@app.get("/health")
def read_health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)