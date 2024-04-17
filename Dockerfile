# Import the latest Python docker image
FROM python:latest

# Set setup to run in bash terminal
SHELL ["/bin/bash", "-c"]

# Install a few text editors
RUN apt update
RUN apt install nano vim -y

# Create new user for lab
RUN useradd -ms /bin/bash aama
USER aama
WORKDIR /home/aama

# Move lab code over to container
COPY resources/* .

# Perform user-level setup tasks
RUN python3 -m venv venv
RUN source venv/bin/activate && pip3 install -r requirements.txt

# Tell Docker to open a terminal in bash instead of Python interpreter
CMD ["/bin/bash"]
