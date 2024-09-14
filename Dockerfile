# Import the latest Python docker image
FROM python:latest

# Set setup to run in bash terminal
SHELL ["/bin/bash", "-c"]

# Install a few text editors
RUN apt update
RUN apt install nano vim wget -y

# Create new user for lab
RUN useradd -ms /bin/bash aama
WORKDIR /home/aama

# Download assignment PE file
RUN wget https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.5.4/npp.8.5.4.Installer.x64.exe -O "ExamplePE.exe"

# Move lab code over to container
COPY resources/* /home/aama/
RUN chown -R aama:aama /home/aama

# Perform user-level setup tasks
USER aama
RUN pip3 install -r requirements.txt

# Tell Docker to open a terminal in bash instead of Python interpreter
CMD ["/bin/bash"]
