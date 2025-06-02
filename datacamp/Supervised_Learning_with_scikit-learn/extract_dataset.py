import zipfile
import os

zip_path = "datacamp-supervisedlearning-scikit-learn-datasets.zip"
extract_to = "dataset"

# Create target folder if it doesn't exist
os.makedirs(extract_to, exist_ok=True)

# Extract
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extract_to)
