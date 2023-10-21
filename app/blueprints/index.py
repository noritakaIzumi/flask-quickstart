from flask import Blueprint, render_template, session

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.route("/")
def hello_world() -> str:
    username = session.get("username") if "username" in session else None
    return render_template("index.html", username=username)
