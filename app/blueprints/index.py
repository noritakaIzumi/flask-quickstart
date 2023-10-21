from flask import Blueprint, render_template

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.route("/")
def hello_world() -> str:
    return render_template("index.html")
