from flask.testing import FlaskClient
from werkzeug.test import TestResponse


class TestApp:
    def test_app(self, client: FlaskClient) -> None:
        response: TestResponse = client.get("/")
        assert response.status_code == 200
        assert b"<p>Hello World!</p>" in response.data
