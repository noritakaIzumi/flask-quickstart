#!/bin/bash

set -e

# config
PYTHON_VERSION="3.11.6"

# update apt packages
sudo apt update

# install app
python -m venv .venv && \
    . .venv/bin/activate
pip install --upgrade pip setuptools && \
    pip install poetry && \
    poetry install --sync --no-root
