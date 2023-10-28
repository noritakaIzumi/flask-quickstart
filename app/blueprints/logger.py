from string import Template

from flask import Blueprint, current_app

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.route("/logger")
def logger() -> str:
    current_app.logger.debug("A value for debugging")
    current_app.logger.warning(Template("A warning occurred ($apples apples)").safe_substitute(apples=42))
    current_app.logger.error("An error occurred")
    return ""
