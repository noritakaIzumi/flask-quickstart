from flask import Blueprint
from markupsafe import escape

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.route("/html_escaping/<name>")
def html_escaping(name: str) -> str:
    return f"Hello, {escape(name)}"
