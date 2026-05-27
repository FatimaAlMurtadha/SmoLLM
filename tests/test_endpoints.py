from fastapi.testclient import TestClient
from app.main import app
import io

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

# This test checks the /data/stats endpoint when no dataset has been uploaded. It sends a GET request to the endpoint and asserts that the response status code is 404, indicating that no dataset is available for statistics.
def test_stats_dataset():
    response = client.get("/data/stats")
    assert response.status_code == 404
