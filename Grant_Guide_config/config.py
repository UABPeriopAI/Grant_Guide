# config.py
from pathlib import Path

from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings

import Grant_Guide_config.app_config as grant_app_config

# Development Directories
BASE_DIR = Path(__file__).parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR, "config")
LOGS_DIR = Path(BASE_DIR, "logs")

# Data Directories
DATA_DIR = Path("/data/DATASCI")
RAW_DATA = Path(DATA_DIR, "raw")
INTERMEDIATE_DIR = Path(DATA_DIR, "intermediate")
RESULTS_DIR = Path(DATA_DIR, "results")

# DATA Files
GRANT_CSV = Path(RAW_DATA, "past_grants.csv")
DEDUP_GRANT_CSV = Path(INTERMEDIATE_DIR, "past_grants.csv")
# Assets
ASSETS_DIR = Path(BASE_DIR, "assets")
GRANT_VECTORSTORE = Path(ASSETS_DIR, "grant_guide-faiss")

# NIH Reporter Field Limits
# Define field length limits
# TODO What can be broken out into json files?
FIELD_LENGTH_LIMITS = {
    "contact_pi_name": 100,
    "org_name": 200,
    "project_title": 300,
    "abstract_text": 5000,
    "phr_text": 5000,
}

EMBEDDINGS = OpenAIEmbeddings(
       openai_api_key="youllneedtoupdatethiswithyourownkey"
       )

CHAT = ChatOpenAI(
    openai_api_base="https://mockgpt.wiremockapi.cloud/v1",
    openai_api_key="sk-aqrgjxkpilpc1wlpjeg0gfsc9zxjh3zr",
    model="gpt-4",
)


DEPARTMENTS = [
    "Anesthesiology",
    "Microbiology/Immun/Virology",
    "Neurosciences",
    "Dentistry",
    "Radiology",
    "Physiology",
    "Surgery",
]

REQUEST_CONFIG = {
    "url": "https://api.reporter.nih.gov/v2/projects/search",
    "headers": {"accept": "application/json", "Content-Type": "application/json"},
}

REQUEST_TIMEOUT = 5

CSV_CONFIG = {
    "filename": Path(GRANT_CSV),
    "headers": [
        "Contact PI",
        "Organization Name",
        "Project Title",
        "Project Abstract",
        "Public Health Relevance Statement",
    ],
}

# Research Strategy

prefilled_text = {
    "Significance": """Problem Identification: Clearly state the problem that your research project aims to address. Include its scope, magnitude, and the current state of understanding.

Relevance to Field: Explain how your research fills a gap in the existing knowledge or addresses a problem in your field.

Scientific Premise: Address the scientific premise of the proposed research, including the consideration of the strengths and weaknesses of published research or preliminary data crucial to the support of your application.

Potential Impact: Describe the potential impact your research could have on the field. Highlight how it may transform existing practices, develop new methodologies or technologies, or shed light on critical issues.

Improvement Over Current Approaches: If applicable, explain how your project improves upon or is a novel departure from existing approaches or methodologies in the field.

Benefit to Human Health: As NIH is focused on improving health, outline how your research will contribute to this mission. Even if the connection is indirect or long-term, make sure to discuss potential applications to human health.

Mitigation of Potential Risks: Briefly discuss the potential risks or challenges of your research project and how you plan to mitigate them. This can show reviewers that you have thoughtfully considered all aspects of the project.

Data Sharing and Resource Sharing: If applicable, discuss how your research might result in data, research resources or tools that could be shared with the wider research community.""",
    "Innovation": """Unique Concept or Approach: Highlight how your project introduces a new concept, challenges existing paradigms, or applies an innovative method or technique to a research problem.

Novel Methodologies: If your project utilizes novel methodologies or technologies, describe them and discuss how they benefit the proposed research. Be sure to also mention if these methodologies or technologies are unique to your lab or institution.

Innovation in Addressing a Gap: If your research is aiming to fill a significant gap in current knowledge or practice, explain this and detail how your approach is innovative compared to previous attempts to fill this gap.

Innovation Impact: Discuss how your innovative approach could potentially change the current state of research or clinical practice in your field.

Risk vs Reward: Often, innovative research comes with higher risks. Discuss the potential risks associated with your innovative approach but emphasize the high reward or impact if the project is successful.

Interdisciplinary and Translational Innovation: If applicable, highlight the interdisciplinary nature of your project and its potential to foster innovation through the integration of diverse scientific disciplines. If the project has translational potential, articulate how the research could lead to innovative clinical applications.

Innovative Use of Existing Resources: If you are using existing resources in new and innovative ways, make sure to describe this. This might include using databases or biological samples in a novel manner.""",
    "Approach": """Overview of Research Design: Provide a general outline of your study design. Describe how the scientific goals of the project will be achieved. This should be an overview of the entire approach of the project.

Specific Methods: Discuss in detail the procedures you'll employ to achieve each specific aim. Include details such as experimental design, statistical analysis, data collection methods, etc. Explain why the chosen methods are suitable for this research.

Data Analysis: Explain how you'll interpret and analyze the results of your experiments or study. Include statistical tests, techniques for reducing bias, methods for controlling variables, etc.

Expected Results: Discuss the potential outcomes you anticipate from your research. Here you should also discuss the implications of these results in terms of the overall aims of your research.

Alternative Approaches: Outline the alternative strategies you plan to employ if your initial approach does not yield the desired results. NIH reviewers often want to know that you have a backup plan in case the primary methods fail.

Potential Problems and Solutions: Identify any potential problems or pitfalls in your research plan and provide potential solutions. This shows that you have thought through your research plan and are prepared for potential issues.

Timeline: Provide a tentative timeline for the project, including key milestones and deliverables. Make sure it is realistic and fits within the funding period.

Preliminary Studies/Progress Report: If it's a new application, include preliminary studies that support the feasibility of your approach. For a renewal or revision application, provide a progress report.""",
    "Rigor": """Rigor of prior research: Identify weaknesses or gaps in the research that serves as the key support for the proposed project

Scientific rigor of the proposed research: Emphasize how the experimental design and methods proposed will achieve robust and unbiased results (via experimental design, methodology, analysis, interpretation and reporting of results)

Biological variables: Explain how relevant biological variables (ie, sex, age, weight, underlying health conditions) are factored into research design analyses, and reporting

Authentication: Describe methods to ensure the identity and validity of key biological variables and/or chemical resources""",
    "Preliminary Data": """Relevance: Begin by explaining why the preliminary data is relevant to your proposed research. Make clear connections between the preliminary results and your project's aims.

Data Description: Describe the preliminary data in enough detail for reviewers to understand what was done and what was found. This can be both quantitative (e.g., experimental results, statistical analysis) or qualitative (e.g., observations, case studies).

Methodology: Describe the methods used to generate your preliminary data, so the reviewers understand how the data were derived. These methods should be similar to or the same as the methods you propose to use in your project, further supporting their feasibility.

Results Interpretation: Interpret your results, providing a clear connection to your research question and showing how they support your hypothesis.

Figures and Tables (describe them): Use figures and tables to present your data clearly and succinctly. Make sure they are well-labeled and easy to understand, with legends that accurately describe what the figures and tables show.

Validity and Reliability: Discuss the validity and reliability of the data, as this will provide strong support for your research proposal.

Limitations: If there are any limitations in your preliminary data, state them openly and explain how you plan to address these limitations in your proposed research.

Conclusion: Summarize how the preliminary data support your proposed study's feasibility and significance, reinforcing the necessity of the proposed research.""",
}
