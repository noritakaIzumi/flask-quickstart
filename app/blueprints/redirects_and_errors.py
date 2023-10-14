from typing import NoReturn

import werkzeug
from app.helpers.url import get_endpoint_name
from flask import Blueprint, abort, make_response, redirect, render_template, url_for
from flask.wrappers import Response

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.get("/redirect_1")
def redirect_1() -> werkzeug.Response:
    return redirect(url_for(get_endpoint_name(redirect_2)))


@bp.get("/redirect_2")
def redirect_2() -> NoReturn:
    abort(401)


# noinspection PyUnusedLocal
@bp.app_errorhandler(werkzeug.exceptions.NotFound)
def page_not_found(error: werkzeug.exceptions.NotFound) -> Response:
    response = make_response(render_template("not_found.html"), 404)
    response.headers["X-Something"] = "A value"
    return response
