import warnings
import os
import typer
from enum import Enum
import getpass

import Grant_Guide.data as grant_data
import Grant_Guide.generate as grant_generate
import Grant_Guide.prompts as grant_guide_prompts
from llm_utils.login import AzureKeyHandler, OpenaiKeyHandler

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
    grant_data.scrape_nih_reporter()


@app.command()
def ingest_grant_csv(
    api : APIConfig = APIConfig.azure,
    embedding_config = grant_helper_config.azure_embeddings
):
    """
    The `ingest` function preprocesses data
    """
    if "OPENAI_API_KEY" not in os.environ:
        os.environ["OPENAI_API_KEY"] = getpass.getpass(prompt="API Key:")
    if api == "azure":
        key_handler = AzureKeyHandler(grant_helper_config.azure_chat_config, 
                                        embedding_config = grant_helper_config.azure_embeddings)
        
        initialized = key_handler.initialize_api_key(os.environ["OPENAI_API_KEY"], grant_helper_config.AZURE_END_POINT)

    elif api == "openai":
        key_handler = OpenaiKeyHandler(grant_helper_config.openai_chat_config, 
                                        embedding_config = grant_helper_config.openai_embeddings)
        
        initialized = key_handler.initialize_api_key(os.environ["OPENAI_API_KEY"], grant_helper_config.OPENAI_END_POINT)
    grant_data.ingest_grant_csv(
        path=grant_helper_config.GRANT_CSV,
        embeddings=embedding_config,
        out=grant_helper_config.GRANT_VECTORSTORE,
    )

@app.command()
def generate_grant_guide(
    api : APIConfig = APIConfig.azure,
    query: str ="",
    embedding_config = grant_helper_config.azure_embeddings,
    chat_config = grant_helper_config.azure_chat_config
):
    """
    The function generates a response to a user query

    Args:
      query (str): The user's query or input text that will be used to generate a response.

    """
    docs = grant_generate.search_grant_guide_vectorstore(
        query,
        embeddings=embedding_config,
        store=grant_helper_config.GRANT_VECTORSTORE,
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
