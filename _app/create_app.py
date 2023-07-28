from typing import Optional

from _app.blueprints.hello import bp_hello
from flask import Flask


def create_app(app_name: Optional[str] = None) -> Flask:
    if app_name is None:
        app_name = __name__
    app = Flask(app_name)
    app.register_blueprint(bp_hello)
    return app
