import os.path
import tomllib
from os.path import abspath, dirname
from typing import Any, Mapping, Optional

from flask import Flask

from .blueprints import file_upload, hello, html_escaping, login, rendering_templates, search
from .blueprints.routing import unique_urls_redirection_behavior, variable_rules

AppConfig = Mapping[str, Any]
app_path = dirname(abspath(__file__))
repo_root = dirname(app_path)
UPLOAD_FOLDER = f"{app_path}/uploads"


def create_app(app_name: Optional[str] = None, test_config: Optional[AppConfig] = None) -> Flask:
    if app_name is None:
        app_name = __name__
    app = Flask(
        app_name,
        static_folder=f"{app_path}/static",
        template_folder=f"{app_path}/templates",
        instance_path=f"{app_path}/instance",
        instance_relative_config=True,
    )

    # config file uploads
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    app.config.from_file(f"{repo_root}/app_env.toml", tomllib.load, text=False)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "app.sqlite"),
    )
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # register blueprints
    app.register_blueprint(hello.bp)
    app.register_blueprint(html_escaping.bp)
    app.register_blueprint(variable_rules.bp)
    app.register_blueprint(unique_urls_redirection_behavior.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(rendering_templates.bp)
    app.register_blueprint(search.bp)
    app.register_blueprint(file_upload.bp)

    return app
