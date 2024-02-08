# Import the latest Python docker image
FROM python:latest

# Move lab code over to container during building
COPY Lab01a/FeatureExtraction.py /home/
COPY Lab01a/UnitTestGradeScript.py /home/
COPY Lab01a/ExamplePE.exe /home/
COPY Lab01a/setup.sh /home/
COPY requirements.txt /home/
