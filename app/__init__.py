import os.path
from os.path import abspath, dirname
from typing import Any, Mapping, Optional

from blueprints import file_upload, hello, html_escaping, login, rendering_templates, search
from blueprints.routing import unique_urls_redirection_behavior, variable_rules
from flask import Flask

AppConfig = Mapping[str, Any]
repo_root = dirname(abspath(__file__))

UPLOAD_FOLDER = f"{repo_root}/uploads"


def create_app(app_name: Optional[str] = None, test_config: Optional[AppConfig] = None) -> Flask:
    if app_name is None:
        app_name = __name__
    app = Flask(
        app_name,
        static_folder=f"{repo_root}/static",
        template_folder=f"{repo_root}/templates",
        instance_path=f"{repo_root}/instance",
        instance_relative_config=True,
    )

    # config file uploads
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("_SECRET_KEY"), DATABASE=os.path.join(app.instance_path, "app.sqlite")
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
