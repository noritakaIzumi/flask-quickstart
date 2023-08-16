from typing import Optional

from blueprints import hello, html_escaping
from blueprints.routing import login, unique_urls_redirection_behavior, variable_rules
from flask import Flask


def create_app(app_name: Optional[str] = None) -> Flask:
    if app_name is None:
        app_name = __name__
    app = Flask(app_name)

    # register blueprints
    app.register_blueprint(hello.bp)
    app.register_blueprint(html_escaping.bp)
    app.register_blueprint(variable_rules.bp)
    app.register_blueprint(unique_urls_redirection_behavior.bp)
    app.register_blueprint(login.bp)

    return app
