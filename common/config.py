import os
import yaml
from dotenv import load_dotenv

load_dotenv()

with open("config.yaml", "r") as f:
    CONFIG = yaml.safe_load(f)

STORAGE_CONNECTION_STRING = os.getenv(
    "AZURE_STORAGE_CONNECTION_STRING"
)

COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
COSMOS_KEY = os.getenv("COSMOS_KEY")

DOC_ENDPOINT = os.getenv(
    "DOCUMENT_INTELLIGENCE_ENDPOINT"
)

DOC_KEY = os.getenv("DOCUMENT_INTELLIGENCE_KEY")