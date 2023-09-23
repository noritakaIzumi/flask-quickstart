from typing import List, Optional

from flask import Blueprint, current_app, render_template, url_for
from werkzeug.routing import Rule

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


def has_no_empty_params(rule: Rule) -> bool:
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


class Link:
    def __init__(self, href: str, text: Optional[str]) -> None:
        self.href = href
        self.text = text


@bp.get("/sitemap")
def sitemap() -> str:
    # ref: https://stackoverflow.com/questions/13317536/get-list-of-all-routes-defined-in-the-flask-app
    links: List[Link] = []
    for rule in current_app.url_map.iter_rules():
        methods = rule.methods or set()
        if "GET" in methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append(Link(url, rule.endpoint))
    return render_template("parts/sitemap.j2", links=links)
