from typing import Optional

from flask import Flask

from blueprints import hello


def create_app(app_name: Optional[str] = None) -> Flask:
    if app_name is None:
        app_name = __name__
    app = Flask(app_name)

    # register blueprints
    app.register_blueprint(hello.bp)

    return app
