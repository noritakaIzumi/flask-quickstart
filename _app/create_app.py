from typing import Optional

from blueprints import hello, html_escaping
from flask import Flask


def create_app(app_name: Optional[str] = None) -> Flask:
    if app_name is None:
        app_name = __name__
    app = Flask(app_name)

    # register blueprints
    app.register_blueprint(hello.bp)
    app.register_blueprint(html_escaping.bp)

    return app
