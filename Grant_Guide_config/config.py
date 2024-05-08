# config.py
from pathlib import Path

# Development Directories
BASE_DIR = Path(__file__).parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR, "config")
LOGS_DIR = Path(BASE_DIR, "logs")

# Data Directories
DATA_DIR = Path("/data")

# DATA Files
GRANT_CSV = Path(DATA_DIR, "past_grants.csv")
DEDUP_GRANT_CSV = Path(DATA_DIR, "past_grants.csv")
# Assets
ASSETS_DIR = Path(BASE_DIR, "assets")
GRANT_VECTORSTORE = Path(ASSETS_DIR, "grant_guide-faiss")

# NIH Reporter Field Limits
# Define field length limits
# TODO What can be broken out into json files?
FIELD_LENGTH_LIMITS = {
    "contact_pi_name": 100,
    "org_name": 200,
    "project_title": 300,
    "abstract_text": 5000,
    "phr_text": 5000,
}

DEPARTMENTS = [
    "Anesthesiology",
    "Microbiology/Immun/Virology",
    "Neurosciences",
    "Dentistry",
    "Radiology",
    "Physiology",
    "Surgery",
]


CSV_CONFIG = {
    "filename": Path(GRANT_CSV),
    "headers": [
        "Contact PI",
        "Organization Name",
        "Project Title",
        "Project Abstract",
        "Public Health Relevance Statement",
    ],
}

#NIH Interface configuration
REQUEST_CONFIG = {
    "url": "https://api.reporter.nih.gov/v2/projects/search",
    "headers": {"accept": "application/json", "Content-Type": "application/json"},
}

REQUEST_TIMEOUT = 5