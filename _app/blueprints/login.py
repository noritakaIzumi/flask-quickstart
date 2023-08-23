from typing import Dict, Optional

from flask import Blueprint, render_template, request

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.route("/login", methods=["GET", "POST"])
def login() -> str:
    error: Optional[str] = None
    if request.method == "POST":
        form: Dict[str, str] = request.form
        if form.get("username") == "nori" and form.get("password") == "password":
            return f'Hello, {form.get("username")}!'
        error = "Invalid username/password"

    return render_template("login.html", action=request.path, error=error)
