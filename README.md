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
  + Uncomment lines 16-18 in ```.devcontainer/devcontainer.json``` and change the source folder location to a existing WSL file path
  ++ That is, change  "source=./data" to source=local/wsl/file/path
  ++The default (./data will work as that file is containted in the repository, but it's better practice to store data in a location other than the code repository)

5. Deploy the Docker container
   + in VS Code press f1 an type "Rebuild"  a drop down menu will provide options and select "Dev Containers: Rebuild Container"
   + You may have to start the docker service with ```sudo service docker start```

6. At this point you can run the application as described in the next section, "Running the Application"  However, to use the generative AI functionality, you will have to add your own LLM enpoint and setup a secrets file as describe in steps 7 and 8.  A bring your own key version will be available in the next release.

7. Connect your LLM endpoint 
  + The LLM enpoint configuration can be found in Grant_Guide/Grant_Guide_config/config.py and the variables that require updating include the EMBEDDINGS and CHAT.
    ++ For example,
    ```CHAT = ChatOpenAI(
    openai_api_base="https://mockgpt.wiremockapi.cloud/v1",
    openai_api_key="sk-aqrgjxkpilpc1wlpjeg0gfsc9zxjh3zr",
    model="gpt-4",
    )```

8. Setup a sectrets.toml file in the streamlit folder (i.e., ```.streamlit/secrets.toml```.)
   The secrets has supportive code to properly handle sensitive information like passwords and access keys. The fields our tool uses and that will need to be populated for the tool to work with minimal modification include:
```
openai_api_key = ""
gpt4_api_key = ""
```

## Running the Application 
### Directly from source code
Run the application with the following command:
```
streamlit run streamlit/Grant_Guide_app.py
```

In this case, use `.streamlit/secrets.toml` for secrets

#### TODO
- [ ] specify a data folder location in `.devcontainer/devcontainer.json`
- [ ] add LLM end-point (e.g., ChatGPT API), including necessary API Key (config.py)

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
