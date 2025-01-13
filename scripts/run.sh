#!/bin/bash

set -e

docker build -t eoussama/breast-cancer-detection -f docker/Dockerfile .
docker run --rm -v $(pwd)/assets/mammograms:/app/assets -p 8501:8501 eoussama/otsu-webbreast-cancer-detection