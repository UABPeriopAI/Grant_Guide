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
def ingest_grant_csv():
    """
    The `ingest` function preprocesses data
    """
    grant_data.ingest_grant_csv(
        path=grant_helper_config.GRANT_CSV,
        embeddings=grant_helper_config.EMBEDDINGS,
        out=grant_helper_config.GRANT_VECTORSTORE,
    )


@app.command()
def generate_grant_guide(
    query: str,
):
    """
    The function generates a response to a user query

    Args:
      query (str): The user's query or input text that will be used to generate a response.

    """
    docs = grant_generate.search_grant_guide_vectorstore(
        query,
        embeddings=grant_helper_config.EMBEDDINGS,
        store=grant_helper_config.GRANT_VECTORSTORE,
    )
    result = grant_generate.get_grant_guide_response(
        query,
        docs,
        chat=grant_helper_config.CHAT,
        chat_prompt=grant_guide_prompts.grant_guide_chat_prompt,
    )
    return result.content


if __name__ == "__main__":
    app()  # pragma: no cover, live app
