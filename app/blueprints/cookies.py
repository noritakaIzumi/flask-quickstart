import json

from flask import Blueprint, Response, make_response, render_template, request

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.get("/get_cookie")
def get_cookie() -> str:
    username = request.cookies.get("username")
    return f"username: {json.dumps(username)}"


@bp.get("/set_cookie")
def set_cookie() -> Response:
    response: Response = make_response(render_template("set_cookie.html"))
    response.set_cookie("username", "nori")
    return response
