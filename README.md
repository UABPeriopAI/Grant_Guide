# Generative AI Grant Drafting Tool

This repository contains a generative AI grant drafting tool that assists users in drafting grant applications for the National Institutes of Health (NIH). The tool consists of three different parts, each serving a specific function in the grant writing process.

## Features

1. **Search and Compare Tool**: This tool interfaces with NIH-RePORTER, a database of NIH-funded research projects, to provide users with a curated list of successfully funded grants related to the idea provided. Users can search for specific keywords or topics and compare the outcomes of different projects to gain insights and inspiration for their own grant applications.

2. **Specific Aims Page Drafter**: The specific aims page is a crucial component of a grant application that outlines the objectives and expected outcomes of the proposed research. This feature accepts specific aims input from the user and uses generative AI techniques to generate a draft summary page for the grant application. It helps users articulate their research goals effectively.

3. **Sub-Section Drafting Tool**: Writing various sections of a grant application can be time-consuming and challenging. This tool provides a streamlined approach to drafting key sections such as significance, innovation, approach, rigor, and preliminary data. Users can input their ideas, and the generative AI assists in generating well-structured drafts that adhere to NIH guidelines and best practices.

## Setting up the Environment
The application was built and tested in a Windwos Subsystem for Linux 2 (WSL2) environment.  The software should work in either a WSL2 or Linux environment. If you are using a Linux environment, skip the installation steps for WSL2 (the next 2 subsections.)

### Install WSL2 on Windwos
 1. Inside Windows Features, make sure "Virtual Machine Platform" and "Hyper-V" are enabled.
 2. Restart
 3. In an elevated powershell prompt, run wsl --install
 4. Restart again
 5. Back in an elevated powershell prompt, confirm WSL and Ubuntu installation with wsl -l -v. You should see Ubuntu listed with version 2.
 6. If not, run wsl --set-default-version 2 followed by wsl --update

*Note-* You may need to launch Ubuntu from the start menu between steps 3 and 4 to get WSL to see the installation (which happens by default with step 2).
If Ubuntu does not automatically install, it can also be installed from the Windows Store (preferably the most recent LTS version).

### Install Git inside WSL2
To prevent constantly entering git credentials, you should install the latest 64-bit version of git for Windows:
https://github.com/git-for-windows/git/releases 
Default options are fine. Though, there may be edge cases where choosing the non-default option of having windows manage certificates will be less of a headache because UAB HSIS issues custom certificates.

Git should already be installed in WSL Ubuntu (by default). If not, you can install it with
```
sudo apt-get install git
```
You will want to use the Windows git credential manager even in WSL so that you do not have to repeatedly enter git credentials.

Once you have confirmed installation of git on both Windows and Ubuntu, run
```
git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/bin/git-credential-manager.exe"
```
You should also take this opportunity to run (and fill in)
```
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
```
In each project with a containerized development environment, you will likely need to run these once without the --global flag.

If you have strange errors with git in WSL, this troubleshooting post is helfpul:
https://stackoverflow.com/questions/72472443/git-credential-manager-not-found-on-wsl2 

### Install Docker
**Do the following inside (wsl) Ubuntu:**

### Ensures not older packages are installed
```
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

#### Ensure pre-requisites are installed
```
 sudo apt-get update
 sudo apt-get install ca-certificates curl gnupg
```

#### Adds docker apt key
```
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

#### Adds docker apt repository
```
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

#### Refreshes apt repos
```
sudo apt-get update
```

#### Installs Docker CE
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

#### Ensures docker group exists
```
sudo groupadd docker
```

#### Ensures you are part of it
```
sudo usermod -aG docker $USER
```

Now, close your shell and open another for taking the group changes into account

#### Systemd
Make sure your `/etc/wsl.conf` in Ubuntu contains
```
[boot]
systemd=true
```
Then, restart WSL by opening powershell and running `wsl --shutdown`, waiting 8 seconds, then opening another Ubuntu shell.

# Confirm Installation
First, run
```
docker version
```
You should get *no* permissions errors if things went well.

You can then try
```
docker run hello-world
```

#### References and more information:
https://docs.docker.com/engine/install/ubuntu/ (seems to be updated)

https://dev.to/felipecrs/simply-run-docker-on-wsl2-3o8 (not being updated, but original way we setup docker-cd in Ubuntu)


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
