#!/bin/bash

set -e

# update apt packages
sudo apt update

# install app
python -m venv .venv && \
    . .venv/bin/activate
pip install --upgrade pip setuptools && \
    pip install poetry && \
    poetry install --sync --no-root
