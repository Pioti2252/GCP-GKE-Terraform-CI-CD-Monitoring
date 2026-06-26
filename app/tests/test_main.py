from main import app


def test_root_endpoint():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    data = response.get_json()

    assert "app" in data
    assert "environment" in data
    assert "version" in data


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    data = response.get_json()

    assert data["status"] == "healthy"


def test_metrics_endpoint():
    client = app.test_client()

    response = client.get("/metrics")

    assert response.status_code == 200
    assert b"flask_http_request_total" in response.data
    assert b"app_info" in response.data