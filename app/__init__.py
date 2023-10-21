import os.path
import tomllib
from logging.config import dictConfig
from os.path import abspath, dirname
from typing import Any, Mapping, Optional

import schema
from flask import Flask

from .blueprints import (
    api_with_json,
    cookies,
    file_upload,
    html_escaping,
    index,
    login,
    redirects_and_errors,
    rendering_templates,
    search,
    sitemap,
)
from .blueprints.routing import unique_urls_redirection_behavior, variable_rules

AppConfig = Mapping[str, Any]
app_path = dirname(abspath(__file__))
repo_root = dirname(app_path)
UPLOAD_FOLDER = f"{app_path}/uploads"


def configure_logging() -> None:
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                }
            },
            "handlers": {
                "wsgi": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://flask.logging.wsgi_errors_stream",
                    "formatter": "default",
                }
            },
            "root": {"level": "INFO", "handlers": ["wsgi"]},
        }
    )


def get_app_env_from_toml(file: str) -> dict:
    app_env: dict
    with open(file, "rb") as f:
        app_env = tomllib.load(f)

    try:
        app_env = schema.Schema({"SECRET_KEY": str, "FORM_PASSWORD": str, "IS_HTTPS": bool}).validate(app_env)
    except schema.SchemaError as e:
        raise Exception(f"app env schema error occurred\n{e}")

    return app_env


def create_app(app_name: Optional[str] = None, test_config: Optional[AppConfig] = None) -> Flask:
    app_env = get_app_env_from_toml(f"{repo_root}/app_env.toml")

    configure_logging()

    if app_name is None:
        app_name = __name__
    app = Flask(
        app_name,
        static_folder=f"{app_path}/static",
        template_folder=f"{app_path}/templates",
        instance_path=f"{app_path}/instance",
        instance_relative_config=True,
    )

    app.config.from_mapping(
        **app_env,
        UPLOAD_FOLDER=UPLOAD_FOLDER,
        DATABASE=os.path.join(app.instance_path, "app.sqlite"),
    )
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # register blueprints
    app.register_blueprint(index.bp)
    app.register_blueprint(html_escaping.bp)
    app.register_blueprint(variable_rules.bp)
    app.register_blueprint(unique_urls_redirection_behavior.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(rendering_templates.bp)
    app.register_blueprint(search.bp)
    app.register_blueprint(file_upload.bp)
    app.register_blueprint(cookies.bp)
    app.register_blueprint(sitemap.bp)
    app.register_blueprint(redirects_and_errors.bp)
    app.register_blueprint(api_with_json.bp)

    return app
