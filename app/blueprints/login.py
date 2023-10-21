from typing import Dict, Optional

import werkzeug
from app.blueprints import index
from app.helpers.url import get_endpoint_name
from flask import Blueprint, current_app, redirect, render_template, request, session, url_for

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.route("/login", methods=["GET", "POST"])
def login() -> str:
    class Form:
        def __init__(self, request_form: Dict[str, str]) -> None:
            self.username = request_form.get("username")
            self.password = request_form.get("password")

    error: Optional[str] = None
    form: Optional[Form] = None
    if request.method == "POST":
        form = Form(request.form)
        expected_password = current_app.config["FORM_PASSWORD"]
        if form.username == "nori" and form.password == expected_password:
            session["username"] = form.username
            return f"Hello, {form.username}!"
        error = "Invalid username/password"

    return render_template("login.html", action=request.path, error=error, form=form)


@bp.get("/logout")
def logout() -> werkzeug.Response:
    session.pop("username", None)
    return redirect(url_for(get_endpoint_name(index.hello_world)))
