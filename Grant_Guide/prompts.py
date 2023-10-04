"""The code you provided is importing modules and defining templates for a chat prompt related to
helping a researcher determine if their grant idea is similar to those funded in the previous fiscal
year by the NIH. It includes templates for system messages, human messages, and a chat prompt
template. The templates define the structure and content of the prompts that will be used in the
chat conversation."""
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

GRANT_SYSTEM_TEMPLATE = "Help a researcher determine if their grant idea is similar to those funded in the previous fiscal year by the NIH."


GRANT_HUMAN_TEMPLATE = """Based on a semantic search, the following projects funded in the previous fiscal year match the researcher's idea most closely.

{context}

Researcher's idea: {idea}

Determine which funded projects, if any, are similar to the researcher's idea. Format your response as follows in markdown.

## Overall assessment of similarity to funed projects: 
<narrative response>

## Similar projects
- Title: <title>
    - PI: <PI>
    - Similarities: <briefly describe similarities>

- Title: <title>
    - PI: <PI>
    - Similarities: <briefly describe similarities>
and so on...
"""


grant_guide_system_message_prompt = SystemMessagePromptTemplate.from_template(GRANT_SYSTEM_TEMPLATE)
grant_guide_human_message_prompt = HumanMessagePromptTemplate.from_template(GRANT_HUMAN_TEMPLATE)
grant_guide_chat_prompt = ChatPromptTemplate.from_messages(
    [grant_guide_system_message_prompt, grant_guide_human_message_prompt]
)


AIMS_SYSTEM_TEMPLATE = """You are an expert clinical researcher who has received continuous NIH (National Institutes of Health) funding throughout their career. You are preparing a funding application for the NIH on your next research idea."""

AIMS_HUMAN_TEMPLATE = """The specific aims of your next project you want to get funded are

{query}

Prepare the specific aims page for your grant application. Below is a guide you wrote explaining what should be in each paragraph.

The Specific Aims segment is paramount in NIH grant applications. It's where you must win over reviewers, stressing your project's importance and establishing your team's credibility. It essentially acts as a snapshot of the entire grant.

Introduction

The opening paragraph should immediately grasp the reviewers' interest by:

Opening Statement: Briefly lay out your research's importance.
Existing Knowledge: Succinctly summarize the current knowledge in the area.
Knowledge Gap: Clearly define the missing information and how your research aims to bridge it. Use typographic emphasis sparingly.
Critical Need: Highlight the urgency of the issue you're addressing and how your research proposes an evolutionary step in the domain.
Example: Viruses contribute to a significant proportion of human cancers. One such virus, HTLV-1, leads to adult T cell leukemia/lymphoma (ATLL). Its oncoprotein, Tax, affects key cellular processes but its transformation mechanism remains unclear. Our research intends to address this knowledge gap.

Second Paragraph: The Solution

Here, explain your answer to the knowledge gap:

Long-Term Goal: Highlight your overarching vision, ensuring it aligns with the funding body's mission.
Rationale: Describe the foundation for your main hypothesis.
Qualifications: Succinctly establish why your team and approach are best suited.
Hypothesis & Objectives: Clearly outline your testable hypothesis and project's primary objectives.
Example: Our solution involves developing a novel mouse model system for studying Tax's role in tumorigenesis. This aligns with findings from Lck-Tax transgenic mice. Our improved approach promises consistent wild-type and mutant Tax protein expression levels.

Aims

Detail each goal that tests your hypothesis:

Title: Choose a clear, active title for each aim.
Summary: Briefly discuss the experimental approach and expected outcomes.
Organization: Utilize headings or bullets for clarity.
Example:

Aim 1: Develop an innovative mouse model for HTLV-1 Tax tumorigenesis.
Aim 2: Investigate mutations affecting Tax functions and their implications for tumorigenesis.
Conclusion

Close with a broad perspective:

Innovation: State the uniqueness of your project.
Expected Outcomes: Detail anticipated results.
Impact: Emphasize the broader implications of your project's success.
Example: Our research offers an upgraded mouse model that addresses the current shortcomings, enhancing understanding of HTLV-1 Tax tumorigenesis. This model can be a pivotal resource for future scientific endeavors, unlocking avenues hitherto inaccessible.

Format your response as markdown using body text only, limiting to one page with room for a small figure on that page. Avoid section headers. Otherwise, phrase and format your response to be copied into a grant proposal for the NIH.

"""

aims_system_message_prompt = SystemMessagePromptTemplate.from_template(AIMS_SYSTEM_TEMPLATE)
aims_human_message_prompt = HumanMessagePromptTemplate.from_template(AIMS_HUMAN_TEMPLATE)
aims_chat_prompt = ChatPromptTemplate.from_messages(
    [aims_system_message_prompt, aims_human_message_prompt]
)

# TODO try without "brief"
SUMMARY_HUMAN_TEMPLATE = """ Use the following Specific Aims page from an NIH-style grant application to prepare a project summary/ abstract for the application.

{sa_page}

Below is a guide you wrote on preparing the Project Summary/Abstract

The purpose of the Project Summary/Abstract is to describe 
succinctly every major aspect of the proposed project. It should contain a statement of 
objectives and methods to be employed. Members of the Study Section who are not 
primary reviewers may rely heavily on the abstract to understand your application. 
Consider the significance and innovation of the research proposed when preparing the 
Project Summary. 

The Project Summary must be no longer than 30 lines of text (in 11-point font on a standard page)

The second component of the Project Summary is relevance of this research to public 
health. Use plain language that can be understood by a general, lay audience. The 
Project Summary should not contain proprietary confidential information. 

The abstract should include: 
- a brief background of the project; 
- specific aims, objectives, or hypotheses; 
- the significance of the proposed research and relevance to public health;
- the unique features and innovation of the project; 
- the methodology (action steps) to be used; 
- expected results; and 
- description of how your results will affect other research areas. 

Suggestions
- Be complete, but brief. 
- Use all the space allotted. 
- Avoid describing past accomplishments and the use of the first person.
- Write the abstract last so that it reflects the entire application. 
- Remember that the abstract will be used for purposes other than the review, 
such as to provide a brief description of the grant in annual reports, 
presentations, and dissemination to the public

Respond only with the <30-line project summary/abstract.
"""

summary_system_message_prompt = SystemMessagePromptTemplate.from_template(AIMS_SYSTEM_TEMPLATE)
summary_human_message_prompt = HumanMessagePromptTemplate.from_template(SUMMARY_HUMAN_TEMPLATE)
summary_chat_prompt = ChatPromptTemplate.from_messages(
    [summary_system_message_prompt, summary_human_message_prompt]
)

STRATEGY_SYSTEM_TEMPLATE = """You are an expert clinical researcher who has received continuous NIH (National Institutes of Health) funding throughout their career. You are preparing a funding application for the NIH on your next research idea."""


STRATEGY_HUMAN_TEMPLATE = """Using the following bullet points, prepare the {part} part of the Research Strategy section for an NIH-R-series grant in narrative, paragraph form.

Bullet points:

{bullets}

Be sure to address the following.

{part_instructions}

Respond in markdown format with narrative paragraphs. Greatly expand on the bullet points.
"""

strategy_system_message_prompt = SystemMessagePromptTemplate.from_template(STRATEGY_SYSTEM_TEMPLATE)
strategy_human_message_prompt = HumanMessagePromptTemplate.from_template(STRATEGY_HUMAN_TEMPLATE)
strategy_chat_prompt = ChatPromptTemplate.from_messages(
    [strategy_system_message_prompt, strategy_human_message_prompt]
)
