import json

from app import repo_root
from flask.testing import FlaskClient
from werkzeug.test import TestResponse


class TestLogin:
    def test_login__get__no_errors(self, client: FlaskClient) -> None:
        response: TestResponse = client.get("/login")
        assert "<h1>Login form</h1>" in response.text

    def test_login__post__valid_login(self, client: FlaskClient) -> None:
        response: TestResponse = client.post(
            "/login",
            data=json.load(open(f"{repo_root}/tests/support/test_login/valid.json")),
        )
        assert "Hello, nori!" in response.text

    def test_login__post__invalid_login__wrong_password(self, client: FlaskClient) -> None:
        response: TestResponse = client.post(
            "/login",
            data=json.load(open(f"{repo_root}/tests/support/test_login/wrong_password.json")),
        )
        assert "Invalid username/password" in response.text

    def test_login__post__invalid_login__user_not_exists(self, client: FlaskClient) -> None:
        response: TestResponse = client.post(
            "/login",
            data=json.load(open(f"{repo_root}/tests/support/test_login/outsider.json")),
        )
        assert "Invalid username/password" in response.text

    def test_login__post__invalid_login__no_info_provided(self, client: FlaskClient) -> None:
        response: TestResponse = client.post("/login", data={})
        assert "Invalid username/password" in response.text
