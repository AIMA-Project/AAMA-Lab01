#!/bin/bash

# Build the Docker image from the repository.
sudo docker build -t lab01-image .

# Run bash in the Docker container to give access to a terminal.
sudo docker run --name lab01 -it lab01-image
