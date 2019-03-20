from flask_boilerplate import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

# Index Page Test
def test_index(client):
    response = client.get('/')
    assert response.data == b'This is a flask-boilerplate project, not to be used in production'

# Hello Page Test
def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello World!'

    response = client.get('/hello?name=Jim')
    assert response.data == b'Hello Jim!'

# Number Page Test
def test_number(client):
    response = client.get('/number/1')
    assert response.data == b'Number: 1'

    response = client.get('/number/2')
    assert response.data == b'Number: 2'

    response = client.get('/number/apple')
    assert response.status_code == 404
