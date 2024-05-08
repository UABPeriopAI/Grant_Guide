import csv
import json
import sys
from datetime import datetime

import pandas as pd
import requests
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS

import Grant_Guide_config.config as grant_helper_config

# very large fields for abstract and phr
csv.field_size_limit(sys.maxsize)


def sanitize_field(field, field_name):
    max_length = grant_helper_config.FIELD_LENGTH_LIMITS.get(
        field_name, 5000
    )  # default to 5000 if no specific limit is set
    if field is not None and len(field) <= max_length:
        # Replace double quotes with single quotes
        field = field.replace('"', "'")
        # Replace commas with semicolons
        # field = field.replace(',', ';')
        # Replace newlines with spaces
        field = field.replace("\n", " ")
    else:
        field = ""
    return field


def scrape_nih_reporter(fiscals_years=5, departments=grant_helper_config.DEPARTMENTS, limit=500):
    # Define the headers
    csv_headers = [
        "Contact PI",
        "Organization Name",
        "Project Title",
        "Project Abstract",
        "Public Health Relevance Statement",
    ]

    # Open the CSV file for writing
    with open(grant_helper_config.CSV_CONFIG["filename"], "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        # Write the headers
        writer.writerow(csv_headers)

        # Get the current year
        current_year = datetime.now().year
        for department in departments:
            offset = 0
            while offset <= 14999:  # api limit
                # Define the payload
                payload = {
                    "criteria": {
                        "fiscal_years": list(
                            range(current_year - (fiscals_years - 1), current_year)
                        ),
                        "dept_types": [department],
                        "award_type": "1",
                        "use_relevance": True,
                        "include_active_projects": True,
                    },
                    "include_fields": [
                        "ContactPiName",
                        "Organization",
                        "ProjectTitle",
                        "AbstractText",
                        "PhrText",
                    ],
                    "offset": offset,
                    "limit": limit,
                }

                # Convert the payload to JSON format
                payload_json = json.dumps(payload)

                # Make the request
                response = requests.post(
                    grant_helper_config.REQUEST_CONFIG["url"],
                    headers=grant_helper_config.REQUEST_CONFIG["headers"],
                    data=payload_json,
                    timeout=grant_helper_config.REQUEST_TIMEOUT,
                )
                data = response.json()

                # If no results, break the loop
                if (
                    isinstance(data, list)
                    and len(data) == 1
                    and "exceeded total records count" in data[0]
                ):
                    break

                # Loop through each result
                for result in data["results"]:
                    # Use try-except block for each attribute

                    try:
                        pi = sanitize_field(result.get("contact_pi_name"), "contact_pi_name")
                    except AttributeError:
                        pi = ""

                    try:
                        org_name = sanitize_field(
                            result["organization"].get("org_name"), "org_name"
                        )
                    except AttributeError:
                        org_name = ""

                    try:
                        title = sanitize_field(result.get("project_title"), "project_title")
                    except AttributeError:
                        title = ""

                    try:
                        abstract = sanitize_field(result.get("abstract_text"), "abstract_text")
                        if abstract is not None:
                            abstract = abstract.replace("\n", " ")
                    except AttributeError:
                        abstract = ""

                    try:
                        phr = sanitize_field(result.get("phr_text"), "phr_text")
                        if phr is not None:
                            phr = phr.replace("\n", " ")
                    except AttributeError:
                        phr = ""

                    # Write the row
                    writer.writerow([pi, org_name, title, abstract, phr])

                # Increase the offset by limit
                offset += limit


def ingest_grant_csv(
    embeddings,
    path=grant_helper_config.GRANT_CSV,
    out=grant_helper_config.GRANT_VECTORSTORE,
):
    """
    This function ingests a CSV file, converts it into a document format, creates a FAISS index using
    embeddings, and saves the index to a local file.

    Args:
      path: The path to the CSV file that contains the data to be ingested.
      embeddings: The embeddings parameter is a path to a file containing pre-trained word embeddings.
    These embeddings are used to convert the text data in the CSV file into numerical vectors that can
    be used for similarity search.
      out: The `out` parameter is the output path where the vector store generated from the CSV
    file will be saved.
    """

    # Read the CSV file using pandas
    df = pd.read_csv(path, na_values=[""])

    # Drop duplicate rows
    df = df.drop_duplicates()
    df = df.dropna(how="any")

    # Write the deduplicated data back to the CSV file
    df.to_csv(grant_helper_config.DEDUP_GRANT_CSV, index=False, quoting=csv.QUOTE_ALL)
    grant_guide_csv_loader = CSVLoader(file_path=grant_helper_config.DEDUP_GRANT_CSV)
    grant_guide_documents = grant_guide_csv_loader.load()
    grant_guide_db = FAISS.from_documents(grant_guide_documents, embeddings)
    grant_guide_db.save_local(out)
