from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.get("/")
def read_root():
    return jsonify({
        "app": os.getenv("APP_NAME", "GCP DevOps Showcase App"),
        "environment": os.getenv("APP_ENV", "local"),
        "version": os.getenv("APP_VERSION", "dev")
    })


@app.get("/health")
def read_health():
    return jsonify({"status": "healthy"})


@app.get("/metrics")
def read_metrics():
    return jsonify({
        "metrics": "some metrics data",
        "app_version": os.getenv("APP_VERSION", "dev")
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)