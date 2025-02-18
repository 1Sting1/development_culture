import pytest
from testing_mocks.src.server import app, users
from io import BytesIO


@pytest.fixture
def client():

    with app.test_client() as client:
        users.clear()
        yield client


def test_register_user(client):

    response = client.post('/register', json={"username": "testuser"})
    assert response.status_code == 201
    data = response.get_json()
    assert "успешно зарегистрирован" in data["message"]
    assert "testuser" in users


def test_register_existing_user(client):

    client.post('/register', json={"username": "testuser"})
    response = client.post('/register', json={"username": "testuser"})
    assert response.status_code == 400


def test_upload_csv(client):

    client.post('/register', json={"username": "testuser"})
    csv_content = "Name,Age,City\nJohn,30,New York\nAlice,25,Chicago"
    data = {
        'username': 'testuser',
        'file': (BytesIO(csv_content.encode('utf-8')), 'data.csv')
    }
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    resp_json = response.get_json()
    assert "Загружено 2 записей" in resp_json["message"]

    response = client.get('/user_data/testuser')
    records = response.get_json()
    assert len(records) == 2


def test_list_users(client):
    client.post('/register', json={"username": "user1"})
    client.post('/register', json={"username": "user2"})
    response = client.get('/users')
    users_list = response.get_json()
    assert "user1" in users_list and "user2" in users_list


def test_get_all_data(client):
    client.post('/register', json={"username": "user1"})
    client.post('/register', json={"username": "user2"})
    csv1 = "Name,Age,City\nJohn,30,New York"
    csv2 = "Name,Age,City\nAlice,25,Chicago"
    client.post('/upload', data={
        'username': 'user1',
        'file': (BytesIO(csv1.encode('utf-8')), 'data1.csv')
    }, content_type='multipart/form-data')
    client.post('/upload', data={
        'username': 'user2',
        'file': (BytesIO(csv2.encode('utf-8')), 'data2.csv')
    }, content_type='multipart/form-data')

    response = client.get('/data')
    all_data = response.get_json()
    assert len(all_data) == 2
