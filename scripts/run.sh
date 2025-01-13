#!/bin/bash

set -e

docker build -t eoussama/breast-cancer-detection -f docker/Dockerfile .
docker run --rm -v $(pwd)/assets:/app/assets -p 8501:8501 eoussama/breast-cancer-detection