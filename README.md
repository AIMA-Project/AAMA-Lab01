# AI-Assisted Malware Analysis Lab 01: Feature Extraction and Data Encoding
This lab seeks to introduce students machine learning concepts of feature extraction and data encoding. This is
accomplished through the use of Python and the LIEF library.

There are two methods for installation:
<ol>
    <li>Standard installation on a bare-metal system.</li>
    <li>Creation of a docker image that contains the needed environment.</li>
</ol>

Instructions for both methods can be found below.

## Preinstallation
This lab requires a portable executable (PE) file compiled for Windows to be added by the user. Almost any .exe file
from the last 20 years should be sufficient. However, if you do this, the grading script must be modified to accomodate
the new executable.

Alternatively, you can download the executable related to this lab
[here](https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.5.4/npp.8.5.4.Installer.x64.exe) and
put it into the "Lab01a" directory under the name "ExamplePE.exe".

## Standard Installation
This method of installation requires Git and Python 3 to be installed on the user's computer. These instructions are
primarily tailored towards Linux, but there should be very little tweaking needed to use them for a Windows environment.

```
$ git clone https://github.com/AIMA-Project/AAMA-Lab01
$ cd AAMA-Lab01
$ python3 -m venv venv
$ source /venv/bin/activate
$ pip install -r requirements.txt
```

## Docker Installation
This method of installation requires Docker to be installed and running on the user's computer. These instructions
should work for both Linux and Windows operating systems, but there may need to be some tweaking. It should be noted
that installation is done in 2 parts: 1st on the computer running Docker, and then within the Docker image itself.

**Part 1: Download Repository**
```
$ git clone https://github.com/AIMA-Project/AAMA-Lab01
$ cd AAMA-Lab01
$ chmod +x setup.sh
$ ./setup.sh
```

After running the above set of commands, your terminal should be running inside a Docker container. From here, the
second part of installation can be done.

**Part 2: Setup Docker Image**

The below set of commands finish setup inside the Docker container by setting up the Python environment.
```
$ cd /home
$ chmod +x setup.sh
$ ./setup.sh
$ source venv/bin/activate
```
