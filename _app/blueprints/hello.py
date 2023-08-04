from flask import Blueprint

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.route("/")
def hello_world() -> str:
    return "<p>Hello World!</p>"
