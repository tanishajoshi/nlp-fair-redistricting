from flask import Flask

def test_home_page():
    flask_app = Flask(__name__)
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client
