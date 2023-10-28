# flask-quickstart

<https://flask.palletsprojects.com/en/3.0.x/quickstart/>

## Preparing environment

Create Python venv.

```shell
python -m venv .venv
```

Then activate.

```shell
. .venv/bin/activate
```

Upgrade pip and install dependencies.

```shell
pip install --upgrade pip setuptools
pip install poetry
poetry install --sync --no-root
```

## Preview server

```shell
poe start
```

Open <http://127.0.0.1:5000> in your browser.

`poe debug` start the app in debug mode.

## For developers

Install volta (if not exists)

```shell
curl https://get.volta.sh | bash
```

Install npm packages

```shell
npm ci
```

### Testing python script

```shell
poe test
```

### E2E tests

Execute tests

```shell
npm run test
```

## Roadmap

### Quickstart

- [x] A Minimal Application
- [x] Debug Mode
- [x] HTML Escaping
- [x] Routing
  - [x] Variable Rules
  - [x] Unique URLs / Redirection Behavior
  - [x] URL Building
  - [x] HTTP Methods
- [x] Static Files
- [x] Rendering Templates
- [x] Accessing Request Data
  - [x] Context Locals
  - [x] The Request Object
  - [x] File Uploads
  - [x] Cookies
- [x] Redirects and Errors
- [x] About Responses
  - [x] APIs with JSON
- [x] Sessions
- [x] Message Flashing
- [x] Logging
- [x] Hooking in WSGI Middleware
- [ ] Using Flask Extensions
- [ ] Deploying to a Web Server

### Tutorial

- [x] Project Layout
- [x] Application Setup
- [ ] Define and Access the Database
- [ ] Blueprints and Views
- [ ] Templates
- [ ] Static Files
- [ ] Blog Blueprint
- [ ] Make the Project Installable
- [ ] Test Coverage
- [ ] Deploy to Production

### Other

- [x] pytest
- [x] e2e test via Playwright
- [x] pre-commit
- [x] linter/formatter
- [x] security check: *.py
