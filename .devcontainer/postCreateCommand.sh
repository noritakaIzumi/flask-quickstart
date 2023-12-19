#!/bin/bash

set -e

# config
PYTHON_VERSION="3.11.6"

# update apt packages
sudo apt update

# install python
sudo apt install -y \
    libbz2-dev \
    libffi-dev \
    libncurses-dev \
    libreadline-dev \
    libsqlite3-dev \
    tk-dev \
    python3-tk \
    liblzma-dev
asdf plugin add python && \
    asdf install python $PYTHON_VERSION && \
    asdf global python $PYTHON_VERSION

# install app
python -m venv .venv && \
    . .venv/bin/activate
pip install --upgrade pip setuptools && \
    pip install poetry && \
    poetry install --sync --no-root
