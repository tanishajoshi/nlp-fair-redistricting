import os
import pytest
import app

@pytest.fixture(scope='module')
def test_client():
    flask_app = app.app
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()

def test_upload_test_stream(test_client):
    file_name = "fake.csv"
    with open(file_name, 'w', encoding='UTF-8') as file:
        data = {
            'csv': (file.write("a,1\nb,2\nc,3"), file_name)
        }
    response = test_client.post('/upload_static_file', data=data)
    os.remove(file_name)
    assert response.status_code == 400


def test_home_page_with_fixture(test_client):

    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Upload" in response.data
    assert b"Show Data" in response.data
    assert b"Preprocessing" in response.data
    assert b"Train" in response.data
    assert b"Data Info" in response.data
    assert b"Graphs" in response.data
    assert b"Get code" in response.data
