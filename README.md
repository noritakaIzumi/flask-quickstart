# flask-quickstart

https://flask.palletsprojects.com/en/2.3.x/quickstart/

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
pip install poetry
poetry install --sync --no-root
```

## Preview server

```shell
poe start
```

Open http://127.0.0.1:5000 in your browser.

`poe debug` start the app in debug mode.

## For developers

After developing, execute lint/format.

```shell
poe run format
poe run lint # if errors are present, fix them and retry
```

## Roadmap

- [x] A Minimal Application
- [x] Debug Mode
- [x] HTML Escaping
- [x] Routing
    - [x] Variable Rules
    - [x] Unique URLs / Redirection Behavior
    - [x] URL Building
    - [x] HTTP Methods
- [ ] Static Files
- [ ] Rendering Templates
- [ ] Accessing Request Data
    - [ ] Context Locals
    - [ ] The Request Object
    - [ ] File Uploads
    - [ ] Cookies
- [ ] Redirects and Errors
- [ ] About Responses
    - [ ] APIs with JSON
- [ ] Sessions
- [ ] Message Flashing
- [ ] Logging
- [ ] Hooking in WSGI Middleware
- [ ] Using Flask Extensions
- [ ] Deploying to a Web Server
