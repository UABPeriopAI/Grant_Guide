import os
import streamlit as st
from st_pages import Page, show_pages
from llm_utils.login import AzureKeyHandler, OpenaiKeyHandler
# Set the encoding to make sure emojis display correclty
os.environ["PYTHONIOENCODING"]="utf-8"

st.set_page_config(
    page_title="Grant Guide",
    page_icon="🤖",
)
# Initalize state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


def log_in():
    api_key = st.session_state["api_key"]
    os.environ["OPENAI_API_KEY"] = api_key

    import Grant_Guide_config.api_config as api_config


    if api_key_type == "Azure":
        key_handler = AzureKeyHandler(api_config.azure_chat_config, 
                                        embedding_config = api_config.azure_embeddings)
        
        initialized = key_handler.initialize_api_key(api_key, api_config.AZURE_END_POINT)

    elif api_key_type == "OpenAI":
        key_handler = OpenaiKeyHandler(api_config.openai_chat_config, 
                                        embedding_config = api_config.openai_embeddings)
        
        initialized = key_handler.initialize_api_key(api_key, api_config.OPENAI_END_POINT)

    else:
        st.error("Select the API key type.")


    # print(initialized)
    if initialized:
        st.session_state.logged_in = True
        st.session_state.chat_config = key_handler.get_chat_function()
        st.session_state.embedding_config = key_handler.get_embedding_function()

if not st.session_state["logged_in"]:
    st.title("Bring your own key")
        
    api_key_type = st.selectbox('Select the type of your API key', ('OpenAI', 'Azure'))
    api_key = st.text_input("Enter your API key", key = "api_key", type="password", on_change=log_in)

else: 
    st.title("Home")
    st.write("Welcome!")

    show_pages(
    [
        Page("streamlit/Home.py", "Home", icon="🏠"),
        Page("streamlit/Grant_Guide_app.py", "Grant Guide", icon="💰")
    ]
)


