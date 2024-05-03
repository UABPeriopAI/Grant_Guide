# streamlit_app.py
import datetime

from llm_utils import text_format
from llm_utils.database import get_db_connection
from llm_utils.streamlit_common import apply_uab_font, hide_streamlit_branding

import Grant_Guide.generate as grant_generate
import Grant_Guide_config.app_config as grant_helper_app_config
import Grant_Guide_config.boilerplate as Grant_boilerplate
import Grant_Guide_config.config as Grant_Guide_config
import streamlit as st

def show_grant_guide_page(vectorstore=Grant_Guide_config.GRANT_VECTORSTORE):
    # page metadata
    st.set_page_config(
        page_title="Grant Guide",
        page_icon="💰",
    )
    # hide streamlit branding
    hide_streamlit_branding()

    # set font to UAB brand standard
    apply_uab_font()

    # page content
    st.title("💰 Grant Guide 🤖")
    st.markdown(
        """
    **Get help writing NIH-style grants.**

    Brought to you by the Anesthesiology Research, Informatics, and Data Science teams.

    _Not approved for use with PHI._

    All submissions are recorded for potential review by departmental and health system personnel.

    ---
    """
    )

    tab1, tab2, tab3 = st.tabs(["Search and Compare", "Specific Aims", "Research Strategy"])

    with tab1:
        st.write(
            "Perform and AI-assisted search of the last 5 fiscal years' funded NIH grants and compare them to your idea. This search is limited to the following [NIH-RePORTER](https://reporter.nih.gov/advanced-search) departments: "
            + ", ".join(Grant_Guide_config.DEPARTMENTS)
        )
        aims = st.text_area(
            "Enter your specific aims:",
            """Aim 1: Identify novel microRNAs differentially expressed in Alzheimer's patients compared to controls.

Aim 2: Investigate the effects of identified microRNAs on neuronal cell viability and behavior in mouse models.

Aim 3: Determine the target genes and signaling pathways affected by these microRNAs.

Aim 4: Assess the therapeutic potential of modulating identified microRNAs in preclinical models.
""",
            height=300,
            key="aims_for_comparison",
        )

        if st.button("Lookup and compare"):
            with st.spinner("Thinking..."):
                submit_time = datetime.datetime.now()
                documents = grant_generate.search_grant_guide_vectorstore(
                    query=aims, 
                    embeddings=st.session_state.embedding_config,
                    store=vectorstore
                )
                result = grant_generate.get_grant_guide_response(query=aims, 
                                                                 docs=documents,
                                                                 chat=st.session_state.chat_config)
                response_time = datetime.datetime.now()
            st.markdown(result.content)

            try:
                with get_db_connection(
                    db_server=grant_helper_app_config.DB_SERVER,
                    db_name=grant_helper_app_config.DB_NAME,
                    db_user=grant_helper_app_config.DB_USER,
                    db_password=grant_helper_app_config.DB_PASSWORD,
                ) as conn:
                    # tempting to move this into llm_utils, but the query will be unique to each app.
                    cursor = conn.cursor()
                    query = """
                    INSERT INTO [dbo].[grant_comparison] (
                        specific_aims, 
                        comparison, 
                        input_time, 
                        response_time
                    ) VALUES (?, ?, ?, ?)
                    """

                    cursor.execute(query, (aims, result.content, submit_time, response_time))

                    st.success(
                        "To comply with a Health System Information Security request, submissions are recorded for potential review."
                    )
            except Exception as e:
                st.error("Something went wrong, you may have not yet setup a database for logging yet")
                st.error(e)

    with tab2:
        st.write(
            "Get an AI-generated draft of your specific aims page and project summary/abstract."
        )
        aims = st.text_area(
            "Enter your specific aims:",
            """Aim 1: Identify novel microRNAs differentially expressed in Alzheimer's patients compared to controls.

Aim 2: Investigate the effects of identified microRNAs on neuronal cell viability and behavior in mouse models.

Aim 3: Determine the target genes and signaling pathways affected by these microRNAs.

Aim 4: Assess the therapeutic potential of modulating identified microRNAs in preclinical models.""",
            height=300,
            key="aims_for_page",
        )

        if st.button("Draft specific aims page"):
            with st.spinner("Drafting. This may take a few minutes..."):
                submit_time = datetime.datetime.now()
                aims_result = grant_generate.get_aims_response(aims, chat=st.session_state.chat_config)
                response_time = datetime.datetime.now()
                summary_result = grant_generate.get_summary_response(aims_result.content, 
                                                                     chat=st.session_state.chat_config)

                output_text = (
                    Grant_boilerplate.CONTRACT
                    + "# AI-generated text \n\n"
                    + "## Specific Aims Page \n\n"
                    + aims_result.content
                    + "\n\n## Project Summary/Abstract \n\n"
                    + summary_result.content
                )

                aims_docx_data = text_format.convert_markdown_docx(output_text)

            if aims_docx_data:
                st.balloons()
                st.write("Note that once you hit download, this form will reset.")

                st.download_button(
                    label="Download aims draft",
                    data=aims_docx_data,
                    file_name="DRAFT_specific_aims_page.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",  # correct MIME type for docx
                )

            try:
                with get_db_connection(
                    db_server=grant_helper_app_config.DB_SERVER,
                    db_name=grant_helper_app_config.DB_NAME,
                    db_user=grant_helper_app_config.DB_USER,
                    db_password=grant_helper_app_config.DB_PASSWORD,
                ) as conn:
                    # tempting to move this into llm_utils, but the query will be unique to each app.
                    cursor = conn.cursor()
                    query = """
                    INSERT INTO [dbo].[aims_helper] (
                        specific_aims, 
                        aims_page, 
                        input_time, 
                        response_time
                    ) VALUES (?, ?, ?, ?)
                    """

                    cursor.execute(
                        query, (aims, summary_result.content, submit_time, response_time)
                    )

                    st.success(
                        "To comply with a Health System Information Security request, submissions are recorded for potential review."
                    )
            except Exception as e:
                st.error("Something went wrong, if the problem persists contact the developers")
                st.error(e)

    with tab3:

        st.write("Get an AI-generated draft of an element of your Research Strategy section.")

        research_strategy_part = st.selectbox(
            "Which part of the Research Strategy do you need help with?",
            list(Grant_Guide_config.prefilled_text.keys()),
        )

        # Display a text area with prefilled text based on the user's selection
        strategy_bullets = st.text_area(
            "Please address the following and replace the text in the box. **We suggest copying the instructions into a Word Doc and pasting your response when done.**",
            value=Grant_Guide_config.prefilled_text[research_strategy_part],
            height=650,
        )

        if st.button("Draft specific strategy part"):
            with st.spinner("Preparing draft. This may take a few minutes..."):
                submit_time = datetime.datetime.now()
                strategy_result = grant_generate.get_strategy_response(
                    bullet_points=strategy_bullets,
                    rs_part=research_strategy_part,
                    instructions=Grant_Guide_config.prefilled_text[research_strategy_part],
                    chat = st.session_state.chat_config
                )
                response_time = datetime.datetime.now()

                output_text = (
                    Grant_boilerplate.CONTRACT
                    + "# AI-generated text \n\n"
                    + strategy_result.content
                )

                strategy_docx_data = text_format.convert_markdown_docx(output_text)

            if strategy_docx_data:
                st.balloons()
                st.write("Note that once you hit download, this form will reset.")

                st.download_button(
                    label="Download strategy element draft",
                    data=strategy_docx_data,
                    file_name=f"DRAFT_{research_strategy_part}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",  # correct MIME type for docx
                )

            try:
                with get_db_connection(
                    db_server=grant_helper_app_config.DB_SERVER,
                    db_name=grant_helper_app_config.DB_NAME,
                    db_user=grant_helper_app_config.DB_USER,
                    db_password=grant_helper_app_config.DB_PASSWORD,
                ) as conn:
                    # tempting to move this into llm_utils, but the query will be unique to each app.
                    cursor = conn.cursor()
                    query = """
                    INSERT INTO [dbo].[strategy_helper] (
                        bullet_points, 
                        strategy_section, 
                        input_time, 
                        response_time
                    ) VALUES (?, ?, ?, ?)
                    """

                    cursor.execute(
                        query,
                        (strategy_bullets, strategy_result.content, submit_time, response_time),
                    )

                    st.success(
                        "To comply with a Health System Information Security request, submissions are recorded for potential review."
                    )
            except Exception as e:
                st.error("Something went wrong, if the problem persists contact the developers")
                st.error(e)


if __name__ == "__main__":
    show_grant_guide_page()
