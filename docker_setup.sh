#!/bin/bash

docker build -t lab01 .
docker run -it lab01 bin/bash
