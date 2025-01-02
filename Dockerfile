FROM python:3.12.5-slim-bookworm

ENV SHELL_USER=python
ENV USER_HOME=/home/$SHELL_USER

RUN apt update && apt upgrade -y

RUN adduser --system --home $USER_HOME --shell /bin/bash --disabled-password $SHELL_USER

USER $SHELL_USER

WORKDIR /work
COPY /poetry.lock /work
COPY /pyproject.toml /work

ENV PATH=$PATH:$USER_HOME/.local/bin

# install python packages
RUN pip install --upgrade pip setuptools && pip install poetry
RUN poetry install --sync --without dev

EXPOSE 8080

COPY . .

# start server
ENTRYPOINT ["poetry", "run"]
CMD ["gunicorn", "--bind", "0.0.0.0:8080"]
