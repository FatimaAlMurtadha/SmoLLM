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