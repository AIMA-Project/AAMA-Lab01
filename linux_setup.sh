#!/bin/bash

wget https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.5.4/npp.8.5.4.Installer.x64.exe -O "ExamplePE.exe"
mv ./resources/* ./
rmdir resources/
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r ./requirements.txt
