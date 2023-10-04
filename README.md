# Generative AI Grant Drafting Tool

This repository contains a generative AI grant drafting tool that assists users in drafting grant applications for the National Institutes of Health (NIH). The tool consists of three different parts, each serving a specific function in the grant writing process.

## Features

1. **Search and Compare Tool**: This tool interfaces with NIH-RePORTER, a database of NIH-funded research projects, to provide users with a curated list of successfully funded grants related to the idea provided. Users can search for specific keywords or topics and compare the outcomes of different projects to gain insights and inspiration for their own grant applications.

2. **Specific Aims Page Drafter**: The specific aims page is a crucial component of a grant application that outlines the objectives and expected outcomes of the proposed research. This feature accepts specific aims input from the user and uses generative AI techniques to generate a draft summary page for the grant application. It helps users articulate their research goals effectively.

3. **Sub-Section Drafting Tool**: Writing various sections of a grant application can be time-consuming and challenging. This tool provides a streamlined approach to drafting key sections such as significance, innovation, approach, rigor, and preliminary data. Users can input their ideas, and the generative AI assists in generating well-structured drafts that adhere to NIH guidelines and best practices.

## Getting Started

To use this generative AI grant drafting tool, follow these steps:

1. Clone the repository:

```
git clone https://github.com/UABPeriopAI/Grant_Guide.git
```

2. Install the necessary dependencies. Make sure you have Python 3 installed.
```
pip install -r requirements.txt
```

3. Run the tool by executing the appropriate scripts for each of the three features. See the documentation within each directory for detailed instructions.

## Running the application 
### Directly from source code
Run the application with the following command:
```
streamlit run streamlit/Grant_Guide_app.py
```

In this case, use `.streamlit/secrets.toml` for secrets

#### TODO
- [ ] specify a data folder location in `.devcontainer/devcontainer.json`


## Contributing

We welcome contributions to enhance and improve the generative AI grant drafting tool. If you'd like to contribute, please follow these guidelines:

- Fork the repository and create a new branch for your feature or bug fix.
- Make your changes and ensure they adhere to the project's coding style.
- Write tests for your code and ensure they pass.
- Open a pull request and provide a detailed explanation of your changes.

## License

This project is licensed under a [GPL License](https://www.gnu.org/licenses/gpl-3.0.en.html)

## Acknowledgements

We would like to acknowledge the following resources and libraries that have contributed to the development of this grant drafting tool:

[NIH-RePORTER](https://projectreporter.nih.gov)
[OpenAI GPT](https://openai.com)

## Contact
 Please feel free to contact us regarding the repo at rmelvin@uabmc.edu and/or ryangodwin@uabmc.edu 
 
## Disclaimer
**_NOTE:_** The NIH has [expressed concern](https://grants.nih.gov/faqs#/use-of-generative-ai-in-peer-review.htm?anchor=56922) that generative AI increases the likelihood of academic misconduct.
*You* are ultimately responsible for any content you use.