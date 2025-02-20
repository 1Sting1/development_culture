# CSV Upload and User Management System

This project is a simple user registration and CSV file upload system using Flask for the backend and a Python client for interaction.

## Project Structure

```
project/
│── data/
│   └── data.csv
│── src/
│   ├── client.py
│   ├── server.py
│   └── csv_parser.py
│── tests/
│   ├── test_client.py
│   ├── test_server.py
│   └── test_csv_parser.py
│── requirements.txt
│── docker-compose.yml
│── README.md
```

## Installation

1. Clone the repository:
   ```sh
   git clone <repo_url>
   cd project_root
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Running the Server

Start the Flask server with:

```sh
python src/server.py
```

## Running the Client

Interact with the system using:

```sh
python src/client.py
```

## API Endpoints

- **Register User**: `POST /register` (JSON `{ "username": "testuser" }`)
- **Upload CSV**: `POST /upload` (Form `username`, File: CSV)
- **List Users**: `GET /users`
- **Get User Data**: `GET /user_data/<username>`
- **Get All Data**: `GET /data`

## Example Usage

### Register a User

```sh
$ python src/client.py
Меню:
1. Зарегистрировать пользователя
Выберите опцию: 1
Введите имя пользователя: testuser
Пользователь 'testuser' успешно зарегистрирован.
```

### Upload CSV

```sh
$ python src/client.py
Меню:
2. Загрузить CSV файл
Введите имя пользователя: testuser
Введите путь к CSV файлу: data/data.csv
Загружено 2 записей для пользователя 'testuser'.
```

### List Users

```sh
$ python src/client.py
Меню:
3. Показать список пользователей
Список пользователей:
- testuser
```

### Get User Data

```sh
$ python src/client.py
Меню:
4. Показать данные пользователя
Введите имя пользователя: testuser
Данные пользователя testuser:
{'Name': 'John', 'Age': '30', 'City': 'New York'}
{'Name': 'Alice', 'Age': '25', 'City': 'Chicago'}
```

### Get All Data

```sh
$ python src/client.py
Меню:
5. Показать все данные
Все загруженные данные:
{'Name': 'John', 'Age': '30', 'City': 'New York'}
{'Name': 'Alice', 'Age': '25', 'City': 'Chicago'}
```

## Running Tests

Run tests using:

```sh
pytest tests/
```

## Running with Docker

Start the project using Docker Compose:

```sh
docker-compose up --build
```

