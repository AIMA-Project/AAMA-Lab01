# AI-Assisted Malware Analysis Lab 01: Feature Extraction and Data Encoding
This lab seeks to introduce students machine learning concepts of feature extraction and data encoding. This is
accomplished through the use of Python and the LIEF library.

There are two methods for installation:
1. Standard installation on a bare-metal system.</li>
2. Creation of a docker image that contains the needed environment.</li>

Instructions for both methods can be found below.

For those already familiar with Docker, but who do not want to go through the process of building the image themselves,
a pre-built image can be found on [Docker Hub](https://hub.docker.com/r/wheelercs/aama-lab01). This image is
automatically built and deployed whenever a push is made to the project repository, thus, it is always kept up to date
with the most recent version of the lab.

## Preinstallation

This lab requires a portable executable (PE) file compiled for Windows to be added by the user. Almost any .exe file
from the last 20 years should be sufficient. However, if you do this, the grading script must be modified to accomodate
the new executable.

Alternatively, you can download the executable related to this lab
[here](https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.5.4/npp.8.5.4.Installer.x64.exe) and
put it into the "Lab01a" directory under the name "ExamplePE.exe".

If you wish to use a container for the lab, instructions for installing Docker can be found on their website:
- [Windows](https://docs.docker.com/desktop/install/windows-install/)
- [Mac](https://docs.docker.com/desktop/install/mac-install/)
- [Linux](https://docs.docker.com/desktop/install/linux-install/)

Docker Desktop is not needed so long as the command line tools are installed. However, it may be useful having a GUI for
managing containers and images.

## Standard Installation
A standard installation of the project on a system without using Docker requires Python 3, with Git also being highly
recommended. The general set of steps needed for installation are as follows:
1. Clone the repository to your machine.
2. Open the "Lab01a" directory of repo in a terminal.
3. Initialize the virtual environment for Python.
4. Install the needed packages into the virual environment.

### Windows
```
$ git clone https://github.com/AIMA-Project/AAMA-Lab01
$ cd AAMA-Lab01/Lab01a
$ py -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Linux
```
$ git clone https://github.com/AIMA-Project/AAMA-Lab01
$ cd AAMA-Lab01/Lab01a
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Docker Building
This method of installation requires Docker to be installed and running on the user's computer. These instructions
should work for both Linux and Windows operating systems, but there may be some slight deviations for your system.

**It is important to note that Linux users will have to run Docker commands as root or using the `sudo` command! You can
follow the [official directions](https://docs.docker.com/engine/install/linux-postinstall/) for how to bypass this, but
it highly recommended that you do not.**

Building the image can be done in two simple commands. Alternatively, these commands can be ran on Windows or Linux with
"docker_setup.ps1" and "docker_setup.sh" respectively.

```
$ docker build -t lab01-image .
$ docker run --name lab01 -it lab01-image
```

These commands perform two operations in succession:
1. Builds a static base image called "lab01-image" from which instances of the lab (called containers) can be created.
2. Creates a container instance of the lab and gives it the name "lab01."

If you need to redeploy the container from the image at any point, you must first delete the current instance of the
lab container. The command `docker container rm lab01` can be used to delete the current instance of the lab01
container. **You will lose any data stored in the container when you perform this command!**

If you need to rebuild the entire image from scratch, you can first delete the current image stored on your machine with
`docker image rm lab01-image`, then use the above commands to build and reploy the new version.

## Future Access
Accessing Docker can vary depending on the IDE and operating system you use. Visual Studio Code has a number of plugins
that make accessing a Docker container fairly straightforward.

Without any plugins or GUI, accessing an already existing container requires first starting it in the background, then
attaching a terminal session to it.

```
$ docker start lab01
$ docker attach lab01
```
