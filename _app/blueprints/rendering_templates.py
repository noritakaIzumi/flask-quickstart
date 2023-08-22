from typing import Optional

from flask import Blueprint, render_template

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.route("/hello/")
@bp.route("/hello/<string:name>")
def hello(name: Optional[str] = None) -> str:
    return render_template("hello.html", name=name)
