# AI-Assisted Malware Analysis Lab 01: Feature Extraction and Data Encoding
This lab seeks to introduce students machine learning concepts of feature extraction and data encoding. This is
accomplished through the use of Python and the LIEF library.

There are two methods for installation:
1. Standard installation on a bare-metal system.</li>
2. Creation of a docker image that contains the needed environment.</li>

Instructions for both methods can be found below.

## Preinstallation

This lab requires a portable executable (PE) file compiled for Windows to be added by the user. Almost any .exe file
from the last 20 years should be sufficient. However, if you do this, the grading script must be modified to accomodate
the new executable.

Alternatively, you can download the executable related to this lab
[here](https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.5.4/npp.8.5.4.Installer.x64.exe) and
put it into the "Lab01a" directory under the name "ExamplePE.exe".

Instructions for installing Docker can be found on their website:
- [Windows](https://docs.docker.com/desktop/install/windows-install/)
- [Mac](https://docs.docker.com/desktop/install/mac-install/)
- [Linux](https://docs.docker.com/desktop/install/linux-install/)

Docker Desktop is not needed so long as the command line tools are installed. However, it may be useful to have a GUI
to Docker for managing containers and images.

## Standard Installation
This method of installation requires Git and Python 3 to be installed on the user's computer. These instructions are
primarily tailored towards Linux, but there should be very little tweaking needed to use them for a Windows environment.

```
$ git clone https://github.com/AIMA-Project/AAMA-Lab01
$ cd AAMA-Lab01/Lab01a
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Docker Building
**It is important to note that Linux users will have to run Docker commands as root or using the `sudo` command!**

This method of installation requires Docker to be installed and running on the user's computer. These instructions
should work for both Linux and Windows operating systems, but there may need to be some tweaking.

A pre-built image is availabe on [Docker Hub](https://hub.docker.com/r/wheelercs/aama-lab01) if you wish to skip the
building process. This image is automatically built, so it stays up to date with the repository.

Building the image can be done in two simple commands. For Linux users, these commands are found in `docker_setup.sh`,
and that script can be ran to automatically perform the image building and container creation. For Windows users, or
those who wish to run the commands manually, they are as follows:

```
$ docker build -t lab01 .
$ docker run -it lab01
```

This builds the image and gives it the name "lab01" before creating a container from that image in an interactive
terminal. To disconnect the terminal from Docker and simultaneously shutdown the container, `exit` can be typed.


## Future Access
Accessing Docker can vary depending on the IDE and operating system you use. Visual Studio Code has a number of plugins
that make accessing a Docker container fairly straightforward.

Without any plugins or GUI, accessing an already existing container requires first starting it in the background, then
attaching a terminal session to it.

```
$ docker start <container-name>
$ docker attach <container-name>
```

The name of the container is randomly generated during creation when using the `run` command. To obtain the name of the
container while it is not running, use the command `docker ps -a`. To find the name of the container while it is
running, issue the command `docker image ls`. When done, the container can be shutdown with `exit`.
