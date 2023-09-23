# flask-quickstart

<https://flask.palletsprojects.com/en/2.3.x/quickstart/>

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
pip install --upgrade pip
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
- [ ] Accessing Request Data
  - [x] Context Locals
  - [x] The Request Object
  - [x] File Uploads
    - [x] add tests
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
- [x] linter/fomatter
- [x] security check: *.py
