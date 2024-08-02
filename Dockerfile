FROM python:3.11.6-bookworm

RUN apt update && apt upgrade -y && apt autoremove -y

WORKDIR /work
COPY . .
SHELL ["/bin/bash", "-c"]

# create and active venv
RUN python -m venv .venv && \
    . .venv/bin/activate

# install python packages
RUN pip install --upgrade pip setuptools && \
    pip install poetry && \
    poetry install --sync --no-root

# start server
ENTRYPOINT [".venv/bin/gunicorn"]
CMD ["--bind", "0.0.0.0:8080"]
