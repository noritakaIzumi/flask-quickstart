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
