from flask import Blueprint, Response, current_app, make_response, render_template, request

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.get("/get_cookie")
def get_cookie() -> str:
    username = request.cookies.get("username")
    return render_template("get_cookie.html", username=username)


@bp.get("/set_cookie")
def set_cookie() -> Response:
    response: Response = make_response(render_template("set_cookie.html"))
    is_https = bool(current_app.config.get("IS_HTTPS"))
    response.set_cookie("username", "nori", httponly=True, secure=is_https)
    return response
