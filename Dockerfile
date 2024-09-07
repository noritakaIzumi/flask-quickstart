FROM python:3.12.5-slim-bookworm

ENV SHELL_USER=python
ENV USER_HOME=/home/$SHELL_USER

RUN apt update && apt upgrade -y
RUN apt install -y --no-install-recommends curl build-essential
# Install latest zlib to avoid: CVE-2023-45853
RUN curl -O http://ftp.jp.debian.org/debian/pool/main/z/zlib/zlib1g_1.3.dfsg+really1.3.1-1_amd64.deb && \
    dpkg -i zlib1g_1.3.dfsg+really1.3.1-1_amd64.deb
RUN curl -O http://ftp.jp.debian.org/debian/pool/main/z/zlib/zlib1g-dev_1.3.dfsg+really1.3.1-1_amd64.deb && \
    dpkg -i zlib1g-dev_1.3.dfsg+really1.3.1-1_amd64.deb
RUN apt remove -y build-essential && \
    apt autoremove -y

RUN adduser --system --home $USER_HOME --shell /bin/bash --disabled-password $SHELL_USER

USER $SHELL_USER

WORKDIR /work
COPY . .

ENV PATH=$PATH:$USER_HOME/.local/bin

# install python packages
RUN pip install --upgrade pip setuptools && pip install poetry
RUN poetry install --sync --without dev

EXPOSE 8080

# start server
ENTRYPOINT ["poetry", "run"]
CMD ["gunicorn", "--bind", "0.0.0.0:8080"]
