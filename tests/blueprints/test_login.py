from flask.testing import FlaskClient
from werkzeug.test import TestResponse


class TestLogin:
    def test_login__get__no_errors(self, client: FlaskClient) -> None:
        response: TestResponse = client.get("/login")
        assert response.text == "login form"

    def test_login__post__valid_login(self, client: FlaskClient) -> None:
        response: TestResponse = client.post(
            "/login",
            data={
                "username": "nori",
                "password": "password",
            },
        )
        assert response.text == "Hello, nori!"

    def test_login__post__invalid_login__wrong_password(self, client: FlaskClient) -> None:
        response: TestResponse = client.post(
            "/login",
            data={
                "username": "nori",
                "password": "password_",
            },
        )
        assert response.text == "Invalid username/password"

    def test_login__post__invalid_login__user_not_exists(self, client: FlaskClient) -> None:
        response: TestResponse = client.post(
            "/login",
            data={
                "username": "outsider",
                "password": "password",
            },
        )
        assert response.text == "Invalid username/password"

    def test_login__post__invalid_login__no_info_provided(self, client: FlaskClient) -> None:
        response: TestResponse = client.post("/login", data={})
        assert response.text == "Invalid username/password"
