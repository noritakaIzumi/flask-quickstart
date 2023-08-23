from flask.testing import FlaskClient
from werkzeug.test import TestResponse


class TestSearch:
    def test_search__get__any_search_words(self, client: FlaskClient) -> None:
        response: TestResponse = client.get("/search", query_string={"q": "yahoo"})
        assert response.text == "Search word: yahoo"

    def test_search__get__no_search_words(self, client: FlaskClient) -> None:
        response: TestResponse = client.get("/search")
        assert response.text == "Please input search word"
