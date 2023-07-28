# flask-quickstart

## Preparing environment

Create venv.

```shell
python -m venv .venv
```

Then activate.

```shell
. .venv/bin/activate
```

Upgrade pip and install dependencies.

```shell
pip install --upgrade pip
pip install pip-autoremove poetry
poetry install --no-root
```

## Preview server

```shell
flask --app app run
```

Open http://127.0.0.1:5000 in your browser.
