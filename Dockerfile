FROM python:3.12.4-slim-bookworm

ENV SHELL_USER=python
ENV USER_HOME=/home/$SHELL_USER

RUN apt update && apt upgrade -y && apt autoremove -y
RUN adduser --system --home $USER_HOME --shell /bin/bash --disabled-password $SHELL_USER

USER $SHELL_USER

WORKDIR /work
COPY . .

ENV PATH=$PATH:$USER_HOME/.local/bin

# install python packages
RUN pip install --upgrade pip setuptools && pip install poetry
RUN poetry install --sync --no-root

# start server
ENTRYPOINT ["poetry", "run"]
CMD ["gunicorn", "--bind", "0.0.0.0:8080"]
