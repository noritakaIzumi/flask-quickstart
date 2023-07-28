from flask import Blueprint

bp_hello = Blueprint("hello", __name__)


@bp_hello.route("/")
def hello_world() -> str:
    return "<p>Hello World!</p>"
