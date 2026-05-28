from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

# This test checks the /data/stats endpoint when no dataset has been uploaded. 
# It sends a GET request to the endpoint and asserts that the response status code is 404, indicating that no dataset is available for statistics.
def test_stats_dataset():
    response = client.get("/data/stats")
    assert response.status_code == 404

# This test checks the /ai/ask endpoint when no dataset has been uploaded. 
# It sends a POST request with a question in the request body and asserts that the response status code is 404, indicating that no dataset is available for processing the question. 
# It also checks that the error message in the response body is "No dataset uploaded".
def test_ask_without_dataset():

    response = client.post(
        "/ai/ask",
        json={
            "question": "What is average score?"
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "No dataset uploaded"

# This test checks the /data/upload endpoint when an invalid file is uploaded. 
# It sends a POST request with a file that is not a CSV and asserts that the response status code is 400
#  indicating that the file format is not acceptable for upload.
def test_upload_invalid_file():

    response = client.post(
        "/data/upload",
        files={
            "file": ("bad.txt", b"not csv")
        }
    )

    assert response.status_code == 400