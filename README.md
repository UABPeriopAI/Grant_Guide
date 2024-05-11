# Generative AI Grant Drafting Tool

This repository contains a generative AI grant drafting tool that assists users in drafting grant applications for the National Institutes of Health (NIH). The tool consists of three different parts, each serving a specific function in the grant writing process.

## Features

1. **Search and Compare Tool**: This tool interfaces with NIH-RePORTER, a database of NIH-funded research projects, to provide users with a curated list of successfully funded grants related to the idea provided. Users can search for specific keywords or topics and compare the outcomes of different projects to gain insights and inspiration for their own grant applications.

2. **Specific Aims Page Drafter**: The specific aims page is a crucial component of a grant application that outlines the objectives and expected outcomes of the proposed research. This feature accepts specific aims input from the user and uses generative AI techniques to generate a draft summary page for the grant application. It helps users articulate their research goals effectively.

3. **Sub-Section Drafting Tool**: Writing various sections of a grant application can be time-consuming and challenging. This tool provides a streamlined approach to drafting key sections such as significance, innovation, approach, rigor, and preliminary data. Users can input their ideas, and the generative AI assists in generating well-structured drafts that adhere to NIH guidelines and best practices.

## Setting up the Environment
The application was built and tested in a Windwos Subsystem for Linux 2 (WSL2) environment.  The software should work in either a WSL2 or Linux environment. If you are using a Linux environment, skip the installation steps for WSL2.  While it is possible to get this tool to work without all these steps, we highly encourage users to install WSL2, Docker, and VSCode for the optimal experience using this software.

### Install WSL2 on Windwos
  Follow the instructions for [installing WSL2](https://github.com/UABPeriopAI/MLOpsTemplate/wiki/Setting-up-WSL2).

### Install Git inside WSL2
Additionally, you may want to follow the [instructions for our recommended usage of git in WSL2](https://github.com/UABPeriopAI/MLOpsTemplate/wiki/Recommended-git-Usage-in-WSL2).

### Install Docker
Follow the instructions for [installing Docker](https://github.com/UABPeriopAI/MLOpsTemplate/wiki/Setting-up-Docker) from the MLOps Template repository Wiki.

### Install VSCode
Follow the instructions for [installing VSCode](https://github.com/UABPeriopAI/MLOpsTemplate/wiki/Installing-VSCode) from the MLOps Template repository Wiki.

*Note* -  This tool is not designed to provide final drafts of grant proposal or allow researchers to not validate their research idea and study design. Drafts submitted directly from this tool without thorough revision will have a near zero chance of being funded.

## Getting Started
### Obtain and Deploy the software
Once the environment is setup, follow these steps to access this generative AI grant drafting tool:

1. Clone the repository:

```
git clone https://github.com/UABPeriopAI/Grant_Guide.git
```

2. Navigate to the directory and open VSCode with
```
code .
```

3. Make sure that the dev container extension is installed in VSCode by going to the Extensions Tab (left-most portion of the user interface

4. (optional) Link a data drive in the ```.devcontainer/devcontainer.json``` file
  ++ That is, change  "source=./data" to source=local/wsl/file/path
  ++ The default (./data will work as that file is containted in the repository, but it's better practice to store data in a location other than the code repository)

5. Deploy the Docker container
   + in VS Code press f1 and type "Rebuild"  a drop down menu will provide options and select "Dev Containers: Rebuild Container"
   + You may have to start the docker service with ```sudo service docker start```

6. Prior to running the streamlit application the user might want to extract data from NIH RePORTER and create a VectorStore for their LLM to reference. The details of what is pulled from NIH RePORTER can be adjusted in Grant_Guide_config/config.py (including, DEPARTMENTS and CSV_CONFIG.)  To create a CSV based on the contents returned by NIH RePORTER enter the following command into the terminal of VSCode ```python Grant_Guide/vector_databases.py get-grant-csv```.  There will likely be some LangChain warnings that can be disregarded. 
   
7. Now, to create the vector store from the CSV, run the following command: ```python Grant_Guide/vector_databases.py ingest-grant-csv```. This will require selecting a LLM source (either azure (default) or openai, to be set via the --api setting, for example, ```python Grant_Guide/vector_databases.py ingest-grant-csv --api openai```) API key for either Azure or OpenAI to run. Upon running, the user will be prompted for their API key.  Creation of the vectorstore will take some, be patient.

8. The web application is now ready to run. 

## Running the Application 
### Directly from source code
Run the application with the following command:
```
streamlit run streamlit/Home.py
```
Occasionally, the webpage will stall and require a refresh to fully deploy.  Once it deploys, the user will be asked to select an API key type (either Azure or OpenAI) and then need to enter their corresponding key in the text box below, as show in the figure.

<img width="538" alt="image" src="https://github.com/UABPeriopAI/Grant_Guide/assets/97175225/d6c9bf45-b797-477f-a188-66d3182534ff">

After the API key is validated the primary user interface will be available.


#### TODO
- [ ] specify a data folder location in `.devcontainer/devcontainer.json`
- [ ] Obtain LLM end-point (i.e., OpenAI or Azure), including necessary API Key.

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
