from _app.factories.create_app import create_app

app = create_app(__name__)


@app.route("/")
def hello_world() -> str:
    return "<p>Hello World!</p>"


if __name__ == "__main__":
    app.run()
