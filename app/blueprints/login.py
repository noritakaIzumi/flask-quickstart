from typing import Dict, Optional

from flask import Blueprint, current_app, render_template, request

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
            return f"Hello, {form.username}!"
        error = "Invalid username/password"

    return render_template("login.html", action=request.path, error=error, form=form)
