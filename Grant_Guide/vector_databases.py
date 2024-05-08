import warnings

import typer

import Grant_Guide.data as grant_data
import Grant_Guide.generate as grant_generate
import Grant_Guide.prompts as grant_guide_prompts
import Grant_Guide_config.app_config as grant_helper_app_config
import Grant_Guide_config.config as grant_helper_config

# Initialize Typer CLI app
app = typer.Typer()
warnings.filterwarnings("ignore")


@app.command()
def get_grant_csv():
    """
    The function `get_grant_csv` retrieves grant data from the NIH Reporter API, parses the results,
    writes them to a CSV file, and deduplicates the CSV file.
    """
    grant_data.scrape_nih_reporter()


@app.command()
def ingest_grant_csv(
    embedding_config = grant_helper_config.azure_embeddings
):
    """
    The `ingest` function preprocesses data
    """
    grant_data.ingest_grant_csv(
        path=grant_helper_config.GRANT_CSV,
        embeddings=embedding_config,
        out=grant_helper_config.GRANT_VECTORSTORE,
    )

if __name__ == "__main__":
    app()  # pragma: no cover, live app
