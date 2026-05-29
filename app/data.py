import pandas as pd

DATASET = None

# Function to load a CSV file and return the DataFrame.
def load_csv(file):
    global DATASET
    df = pd.read_csv(file)
    DATASET = df
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict()
    }

# Function in order to load a CSV file into the global DATA variable. It reads the CSV file using pandas and stores it in DATA. The function returns a dictionary containing the number of rows, the list of column names, and the data types of each column in the loaded dataset.
def load_csv_and_get_info(file) -> dict:
    df = pd.read_csv(file)
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict()
    }

# Function in order to get statistics about the loaded dataset. If no dataset has been loaded, it returns None. Otherwise, it returns a description of the dataset in the form of a dictionary.
def get_stats():
    if DATASET is None:
        return None
    return DATASET.describe().to_dict()