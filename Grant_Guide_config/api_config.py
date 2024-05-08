from pathlib import Path
from langchain.chat_models import ChatOpenAI
from langchain_openai import AzureOpenAIEmbeddings
from langchain_openai import AzureChatOpenAI
from langchain_openai import OpenAIEmbeddings

# END points
AZURE_END_POINT = 'https://nlp-ai-svc.openai.azure.com'
OPENAI_END_POINT = 'https://api.openai.com/v1/engines'


azure_chat_config =  AzureChatOpenAI(
    azure_endpoint=AZURE_END_POINT,
    openai_api_version="2024-02-01",
    azure_deployment="ChatGPT4",
    openai_api_type="azure",
    temperature=0.5,
    model_name="gpt-4",

)

azure_embeddings = AzureOpenAIEmbeddings(
    azure_deployment="NewAda2",
    model="text-embedding-ada-002",
    azure_endpoint=AZURE_END_POINT,
    openai_api_type="azure",
    chunk_size=1,
)

openai_chat_config = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", request_timeout=300)

openai_embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002"
        )




