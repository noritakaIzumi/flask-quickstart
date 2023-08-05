from html import unescape

import pytest
from flask.testing import FlaskClient
from markupsafe import escape
from werkzeug.test import TestResponse


class TestApp:
    def test_app__hello(self, client: FlaskClient) -> None:
        response: TestResponse = client.get("/")
        assert response.status_code == 200
        assert b"<p>Hello World!</p>" in response.data

    def test_app__html_escaping(self, client: FlaskClient) -> None:
        response: TestResponse = client.get("/html_escaping/<<<<<<")
        assert response.status_code == 200
        assert response.text == f'Hello, {escape("<<<<<<")}'

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
