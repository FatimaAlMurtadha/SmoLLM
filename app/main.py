# FastAPI-app, endpoints
from fastapi import FastAPI, HTTPException, UploadFile, File
from app.data import load_csv, get_stats
from app.schemas import AskRequest

app = FastAPI()

# Global variable to track whether a dataset has been loaded. Initially set to False, it can be used to determine if the /data/stats endpoint should return statistics or a 404 error indicating that no dataset has been uploaded.
DATA_LOADED = False

# Endpoint to upload a CSV file. It accepts a file upload, loads the CSV data using the load_csv function, and returns the statistics of the loaded dataset. The DATA_LOADED variable is set to True after successfully loading the dataset.
@app.get("/health")
def health():
    return {"status": "OK"}

# Endpoint to upload a CSV file. It accepts a file upload, checks if the file is a CSV, and if so, loads the data using the load_csv function. The endpoint returns metadata about the loaded dataset, such as the number of rows, columns, and data types. If the uploaded file is not a CSV, it raises an HTTP 400 error.
@app.post("/data/upload")
async def upload(file: UploadFile = File(...)):
    global DATA_LOADED

    if not file.filename.endswith(".csv"):
        raise HTTPException(400, "Only CSV allowed")

    meta = load_csv(file.file)
    DATA_LOADED = True

    return meta

# Endpoint to retrieve statistics about the loaded dataset. If no dataset has been uploaded (i.e., DATA_LOADED is False), it raises an HTTP 404 error indicating that no dataset is available. If a dataset has been loaded, it returns the statistics of the dataset using the get_stats function.
@app.get("/data/stats")
def stats():
    stats = get_stats()

    if stats is None:
        raise HTTPException(404, "No dataset uploaded")

    return stats