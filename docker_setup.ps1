#!/bin/bash
# Above is needed for running on Linux

# Build the Docker image
docker build -t lab01-image . --no-cache

# Create an instance of the image and attach shell to it
docker run --name lab01 -it lab01-image

# NOTE: This script is intended to be usable on both Windows and Linux.
