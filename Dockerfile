FROM python:3.12.4-slim-bookworm

RUN apt update && apt upgrade -y && apt autoremove -y

WORKDIR /work
COPY . .

# install python packages
RUN pip install --upgrade pip setuptools && \
    pip install poetry && \
    poetry install --sync --no-root

# start server
ENTRYPOINT ["poetry", "run"]
CMD ["gunicorn", "--bind", "0.0.0.0:8080"]
