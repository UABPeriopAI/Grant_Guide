from llm_utils.sensitive import manage_sensitive

# Database
DB_SERVER = manage_sensitive("db_server")
DB_NAME = manage_sensitive("db_name")
DB_USER = manage_sensitive("db_user")
DB_PASSWORD = manage_sensitive("db_password")

# LLM specific
OPENAI_API_KEY = manage_sensitive("openai_api_key")
GPT4_KEY = manage_sensitive("gpt4_api_key")
