from html import unescape

import pytest
from app import create_app, repo_root
from app.blueprints import hello
from app.blueprints.routing import variable_rules
from app.blueprints.routing.unique_urls_redirection_behavior import about
from app.helpers.url import get_endpoint_name
from flask import request, url_for
from flask.testing import FlaskClient
from markupsafe import escape, soft_str
from tests.support.json_helper import json_is_valid
from werkzeug.test import TestResponse

_app = create_app()


class TestApp:
    def test_app__hello(self, client: FlaskClient) -> None:
        response: TestResponse = client.get("/")
        assert response.status_code == 200
        assert b"<p>Hello World!</p>" in response.data

    def test_app__html_escaping(self, client: FlaskClient) -> None:
        response: TestResponse = client.get("/html_escaping/<<<<<<")
        assert response.status_code == 200
        assert response.text == f'Hello, {escape("<<<<<<")}'

    # noinspection SpellCheckingInspection
    @pytest.mark.parametrize(
        "path, response_text",
        (
            pytest.param("/user/nori", "User nori", id="show the user profile for that user"),
            pytest.param("/user/<br>", "User <br>", id="show the user profile for that user: escape"),
            pytest.param("/post/123", "Post 123", id="show the post with the given id, the id is an integer"),
            pytest.param("/path/dir1/dir2/file", "Subpath dir1/dir2/file", id="show the subpath after /path/"),
            pytest.param("/path/<h1>title</h1>", "Subpath <h1>title</h1>", id="show the subpath after /path/: escape"),
        ),
    )
    def test_app__variable_rules(self, client: FlaskClient, path: str, response_text: str) -> None:
        response: TestResponse = client.get(path)
        assert response.status_code == 200
        assert unescape(response.text) == response_text

    @pytest.mark.parametrize("path", (pytest.param("/post/str", id="str to int placeholder"),))
    def test_app__variable_rules__404(self, client: FlaskClient, path: str) -> None:
        response: TestResponse = client.get(path)
        assert response.status_code == 404

    @pytest.mark.parametrize(
        "path, status_code",
        (
            pytest.param("/projects/", 200, id="endpoint has trailing slash: redirect"),
            pytest.param("/projects", 200, id="endpoint has trailing slash"),
            pytest.param("/about", 200, id="endpoint has no trailing slash"),
            pytest.param("/about/", 404, id="endpoint has no trailing slash: 404"),
        ),
    )
    def test_app__unique_urls_redirection_behavior(self, client: FlaskClient, path: str, status_code: int) -> None:
        response: TestResponse = client.get(path, follow_redirects=True)
        assert response.status_code == status_code

    def test_app__url_building(self, client: FlaskClient) -> None:
        with _app.test_request_context():
            assert url_for(get_endpoint_name(hello.hello_world)) == "/"
            assert url_for(get_endpoint_name(about)) == "/about"
            assert url_for(get_endpoint_name(about), next="/") == "/about?next=/"
            assert (
                url_for(get_endpoint_name(variable_rules.show_user_profile), username="John Doe") == "/user/John%20Doe"
            )

    def test_app__static_files(self) -> None:
        with _app.test_request_context():
            assert url_for("static", filename="style.css") == "/static/style.css"

    def test_app__rendering_templates(self, client: FlaskClient) -> None:
        response: TestResponse = client.get("/hello/")
        assert "Hello, World!" in response.text

    def test_app__rendering_templates_markup(self) -> None:
        from markupsafe import Markup

        assert (
            soft_str(Markup("<strong>Hello %s!</strong>") % "<blink>hacker</blink>")
            == "<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>"
        )
        assert soft_str(escape("<blink>hacker</blink>")) == "&lt;blink&gt;hacker&lt;/blink&gt;"
        assert Markup("<em>Marked up</em> &raquo; HTML").striptags() == "Marked up » HTML"

    def test_app__accessing_request_data__context_locals(self) -> None:
        with _app.test_request_context("/hello", method="POST"):
            assert request.path == "/hello"
            assert request.method == "POST"

    def test_app__redirects_and_errors(self, client: FlaskClient) -> None:
        response: TestResponse = client.get("/redirect_1", follow_redirects=True)
        assert response.status_code == 401
        assert response.request.path == "/redirect_2"
        assert len(response.history) == 1

    def test_app__redirects_and_errors__handing_404_errors(self, client: FlaskClient) -> None:
        response: TestResponse = client.get("/blahblah")
        assert response.status_code == 404
        assert "Page Not Found" in response.text
        assert response.headers.get("X-Something") == "A value"

    def test_app__api_with_json__case1(self, client: FlaskClient) -> None:
        response: TestResponse = client.get("/me")
        assert response.status_code == 200
        assert response.is_json
        assert json_is_valid(instance=response.json, schema_filepath=f"{repo_root}/tests/json/user.schema.json")

    def test_app__api_with_json__case2(self, client: FlaskClient) -> None:
        response: TestResponse = client.get("/users")
        assert response.status_code == 200
        assert response.is_json
        assert json_is_valid(instance=response.json, schema_filepath=f"{repo_root}/tests/json/users.schema.json")
