import os
from html import unescape
from io import BytesIO

from app import UPLOAD_FOLDER
from bs4 import BeautifulSoup
from flask.testing import FlaskClient
from werkzeug.datastructures import FileStorage
from werkzeug.test import TestResponse
from werkzeug.utils import secure_filename


class TestFileUpload:
    def test_upload_file__get_method_shows_form(self, client: FlaskClient) -> None:
        """ファイルをアップロードする input box とアップロードボタンが存在する"""
        response: TestResponse = client.get("/upload")
        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
        form = soup.find("form")
        assert form is not None, "フォームが存在しません"
        assert form.find("input", {"type": "file"}) is not None, "input box が存在しません"
        assert form.find(["input", "button"], {"type": "submit"}) is not None, "submit ボタンが存在しません"

    def test_upload_file__post__files_not_in_request(self, client: FlaskClient) -> None:
        data: dict = {}
        response: TestResponse = client.post("/upload", data=data, follow_redirects=True)
        assert "No file part" in response.text

    def test_upload_file__post__filename_is_empty(self, client: FlaskClient) -> None:
        data = {"file": FileStorage(filename="", stream=None)}
        response: TestResponse = client.post("/upload", data=data, follow_redirects=True)
        assert "No selected file" in response.text

    def test_upload_file__post__file_is_not_allowed_to_upload(self, client: FlaskClient) -> None:
        data = {"file": FileStorage(filename="sample.md", stream=BytesIO(b"# hello world"))}
        response: TestResponse = client.post("/upload", data=data, follow_redirects=True)
        assert '"sample.md" is not allowed to upload' in unescape(response.text)

    def test_upload_file__post__succeed_to_upload_file(self, client: FlaskClient) -> None:
        filename = "sample.txt"
        data = {"file": FileStorage(filename=filename, stream=BytesIO(b"hello world"))}
        response: TestResponse = client.post("/upload", data=data, follow_redirects=True)
        assert "Upload completed" in response.text
        upload_filepath = f"{UPLOAD_FOLDER}/{secure_filename(filename)}"
        with open(upload_filepath, "r") as f:
            assert f.read() == "hello world"
        os.remove(upload_filepath)

    def test_upload_file__post__filename_is_sanitized(self, client: FlaskClient) -> None:
        filename = "新規 テキスト ドキュメント.txt"
        data = {"file": FileStorage(filename=filename, stream=BytesIO(b"hello world"))}
        response: TestResponse = client.post("/upload", data=data, follow_redirects=True)
        assert "Upload completed" in response.text
        upload_filepath = f"{UPLOAD_FOLDER}/{secure_filename(filename)}"
        with open(upload_filepath, "r") as f:
            assert f.read() == "hello world"
        os.remove(upload_filepath)
