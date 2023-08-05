from flask import Blueprint

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.route('/projects/')
def projects() -> str:
    return 'The project page'


@bp.route('/about')
def about():
    return 'The about page'
