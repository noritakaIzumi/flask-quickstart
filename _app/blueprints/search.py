from typing import Optional

from flask import Blueprint, render_template, request

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.get("/search")
def search() -> str:
    params = request.args
    keyword: Optional[str] = params.get("q")

    error: Optional[str] = None
    if keyword is None:
        error = "Please input search word"

    return render_template("search.html", keyword=keyword, error=error)
