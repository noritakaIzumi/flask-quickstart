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

## Roadmap

- [x] A Minimal Application
- [ ] Debug Mode
- [ ] HTML Escaping
- [ ] Routing
  - [ ] Variable Rules
  - [ ] Unique URLs / Redirection Behavior
  - [ ] URL Building
  - [ ] HTTP Methods
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
