from flask import Blueprint
from markupsafe import escape

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.route("/user/<username>")
def show_user_profile(username: str) -> str:
    return f"User {escape(username)}"


@bp.route("/post/<int:post_id>")
def show_post(post_id: int) -> str:
    return f"Post {post_id}"


@bp.route("/path/<path:subpath>")
def show_subpath(subpath: str) -> str:
    return f"Subpath {escape(subpath)}"
