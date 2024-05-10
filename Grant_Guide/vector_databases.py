import warnings
import os
import typer
from enum import Enum
from getpass4 import getpass

from Grant_Guide.nih_interface import scrape_nih_reporter
from Grant_Guide.ingest_grant_csv import create_vectorstore_from_csv
import Grant_Guide.generate as grant_generate
import Grant_Guide.prompts as grant_guide_prompts
import Grant_Guide_config.config as grant_guide_config

class APIConfig(str, Enum):
    azure = "azure"
    openai = "openai"

# Initialize Typer CLI app
app = typer.Typer()
warnings.filterwarnings("ignore")


@app.command()
def get_grant_csv():
    """
    The function `get_grant_csv` retrieves grant data from the NIH Reporter API, parses the results,
    writes them to a CSV file, and deduplicates the CSV file.
    """
    scrape_nih_reporter()


@app.command()
def ingest_grant_csv(
    api : APIConfig = APIConfig.azure,
):
    """
    The `ingest` function preprocesses data
    """
    if "OPENAI_API_KEY" not in os.environ:
        os.environ["OPENAI_API_KEY"] = getpass(prompt="API Key:")

    import Grant_Guide_config.api_config as api_config
    
    if api == "azure":
        embedding_config = api_config.azure_embeddings
        
    elif api == "openai":
        embedding_config = api_config.openai_embeddings
        
    create_vectorstore_from_csv(
        embeddings=embedding_config,
        path=grant_guide_config.GRANT_CSV,
        out=grant_guide_config.GRANT_VECTORSTORE,
    )

@app.command()
def generate_grant_guide(
    api : APIConfig = APIConfig.azure,
    query: str ="",
):
    """
    The function generates a response to a user query

    Args:
      query (str): The user's query or input text that will be used to generate a response.

    """

    if "OPENAI_API_KEY" not in os.environ:
        os.environ["OPENAI_API_KEY"] = getpass(prompt="API Key:")

    import Grant_Guide_config.api_config as api_config

    if api == "azure":
        embedding_config = api_config.azure_embeddings
        chat_config = api_config.azure_chat_config

    elif api == "openai":
        embedding_config = api_config.openai_embeddings
        chat_config = api_config.openai_chat_config

    docs = grant_generate.search_grant_guide_vectorstore(
        query,
        embeddings=embedding_config,
        store=grant_guide_config.GRANT_VECTORSTORE,
    )
    result = grant_generate.get_grant_guide_response(
        query,
        docs,
        chat=chat_config,
        chat_prompt=grant_guide_prompts.grant_guide_chat_prompt,
    )
    return result.content

if __name__ == "__main__":
    app()  
