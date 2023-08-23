from flask import Blueprint

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.get("/login")
def login_get() -> str:
    return "show_the_login_form"


@bp.post("/login")
def login_post() -> str:
    return "do_the_login"
