import pytest
from unittest.mock import patch
from src import client


class FakeResponse:
    def __init__(self, status_code, json_data, text=""):
        self.status_code = status_code
        self._json = json_data
        self.text = text

    def json(self):
        return self._json


@patch('src.client.requests.post')
def test_register_user_success(mock_post, monkeypatch):

    monkeypatch.setattr('builtins.input', lambda prompt='': 'testuser')
    fake_resp = FakeResponse(201, {"message": "Пользователь 'testuser' успешно зарегистрирован."})
    mock_post.return_value = fake_resp

    from io import StringIO
    from contextlib import redirect_stdout
    f = StringIO()
    with redirect_stdout(f):
        client.register_user()
    output = f.getvalue()
    assert "успешно зарегистрирован" in output


@patch('src.client.requests.post')
def test_upload_csv_file_not_found(mock_post, monkeypatch):

    monkeypatch.setattr('builtins.input', lambda prompt='': 'nonexistent.csv' if 'путь к CSV' in prompt else 'testuser')

    from io import StringIO
    from contextlib import redirect_stdout
    f = StringIO()
    with redirect_stdout(f):
        client.upload_csv()
    output = f.getvalue()
    assert "Файл не найден" in output


@patch('src.client.requests.get')
def test_list_users(mock_get):

    fake_resp = FakeResponse(200, ["user1", "user2"])
    mock_get.return_value = fake_resp

    from io import StringIO
    from contextlib import redirect_stdout
    f = StringIO()
    with redirect_stdout(f):
        client.list_users()
    output = f.getvalue()
    assert "user1" in output and "user2" in output


@patch('src.client.requests.get')
def test_get_user_data_not_found(mock_get, monkeypatch):

    monkeypatch.setattr('builtins.input', lambda prompt='': 'unknown_user')
    fake_resp = FakeResponse(404, {}, "User not found")
    mock_get.return_value = fake_resp

    from io import StringIO
    from contextlib import redirect_stdout
    f = StringIO()
    with redirect_stdout(f):
        client.get_user_data()
    output = f.getvalue()
    assert "Ошибка получения данных" in output
