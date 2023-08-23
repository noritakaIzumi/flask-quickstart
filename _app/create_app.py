from os.path import abspath, dirname
from typing import Optional

from blueprints import hello, html_escaping, login, rendering_templates
from blueprints.routing import unique_urls_redirection_behavior, variable_rules
from flask import Flask

repo_root = dirname(dirname(abspath(__file__)))


def create_app(app_name: Optional[str] = None) -> Flask:
    if app_name is None:
        app_name = __name__
    app = Flask(app_name, static_folder=f"{repo_root}/static", template_folder=f"{repo_root}/templates")

    # register blueprints
    app.register_blueprint(hello.bp)
    app.register_blueprint(html_escaping.bp)
    app.register_blueprint(variable_rules.bp)
    app.register_blueprint(unique_urls_redirection_behavior.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(rendering_templates.bp)

    return app
