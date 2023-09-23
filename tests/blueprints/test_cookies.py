from flask.testing import FlaskClient
from werkzeug.test import TestResponse


class TestCookies:
    def test_set_cookie(self, client: FlaskClient) -> None:
        client.get("/set_cookie")
        cookie = client.get_cookie("username")
        assert cookie is not None
        assert cookie.value == "nori"

        response: TestResponse = client.get("/get_cookie")
        assert 'username: "nori"' in response.text

    def test_get_cookie__some_cookies_set(self, client: FlaskClient) -> None:
        client.set_cookie("username", "somebody")
        response: TestResponse = client.get("/get_cookie")
        assert 'username: "somebody"' in response.text

    def test_get_cookie__no_cookies_set(self, client: FlaskClient) -> None:
        response: TestResponse = client.get("/get_cookie")
        assert "username: null" in response.text
