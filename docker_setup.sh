#!/bin/bash

# Build the Docker image from the repository.
docker build -t lab01 .

# Run bash in the Docker container to give access to a terminal.
docker run -it lab01 bin/bash
