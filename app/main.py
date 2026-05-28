from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def read_root():
    return jsonify({"Hello": "World"})


@app.get("/health")
def read_health():
    return jsonify({"status": "healthy"})


@app.get("/metrics")
def read_metrics():
    return jsonify({"metrics": "some metrics data"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)