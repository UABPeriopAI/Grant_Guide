import csv

import pandas as pd
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS

import Grant_Guide_config.config as grant_guide_config


def create_vectorstore_from_csv(
    embeddings,
    path=grant_guide_config.GRANT_CSV,
    out=grant_guide_config.GRANT_VECTORSTORE,
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
    df.to_csv(grant_guide_config.DEDUP_GRANT_CSV, index=False, quoting=csv.QUOTE_ALL)
    grant_guide_csv_loader = CSVLoader(file_path=grant_guide_config.DEDUP_GRANT_CSV)
    grant_guide_documents = grant_guide_csv_loader.load()
    grant_guide_db = FAISS.from_documents(grant_guide_documents, embeddings)
    grant_guide_db.save_local(out)
