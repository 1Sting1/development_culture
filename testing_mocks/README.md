#  Система управления пользователями и загрузки CSV

Этот проект представляет собой простую систему регистрации пользователей и загрузки CSV-файлов с использованием Flask в качестве backend и клиентского Python-приложения для взаимодействия.

---

## 📂 Структура проекта

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

---

## 🚀 Установка и запуск

### 🔹 1. Клонирование репозитория

```sh
git clone <repo_url>
cd project_root
```

### 🔹 2. Установка зависимостей

Создайте виртуальное окружение и установите зависимости:

```sh
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 🔹 3. Запуск сервера через Docker

```sh
docker-compose up --build
```

### 🔹 4. Запуск клиента

```sh
python src/client.py
```

---

## 🌐 API эндпоинты

| Метод | Эндпоинт | Описание |
|--------|----------|-----------|
| `POST` | `/register` | Регистрация пользователя (JSON `{ "username": "testuser" }`) |
| `POST` | `/upload` | Загрузка CSV-файла (Form `username`, файл: CSV) |
| `GET`  | `/users` | Получение списка пользователей |
| `GET`  | `/user_data/<username>` | Получение данных конкретного пользователя |
| `GET`  | `/data` | Получение всех загруженных данных |

---

## 🔹 Примеры использования

### 🔹 Регистрация пользователя

```sh
$ python src/client.py
Меню:
1. Зарегистрировать пользователя
Выберите опцию: 1
Введите имя пользователя: testuser
Пользователь 'testuser' успешно зарегистрирован.
```

### 🔹 Загрузка CSV-файла

```sh
$ python src/client.py
Меню:
2. Загрузить CSV файл
Введите имя пользователя: testuser
Введите путь к CSV файлу: data/data.csv
Загружено 2 записи для пользователя 'testuser'.
```

### 🔹 Просмотр списка пользователей

```sh
$ python src/client.py
Меню:
3. Показать список пользователей
Список пользователей:
- testuser
```

### 🔹 Получение данных пользователя

```sh
$ python src/client.py
Меню:
4. Показать данные пользователя
Введите имя пользователя: testuser
Данные пользователя testuser:
{'Name': 'John', 'Age': '30', 'City': 'New York'}
{'Name': 'Alice', 'Age': '25', 'City': 'Chicago'}
```

### 🔹 Получение всех данных

```sh
$ python src/client.py
Меню:
5. Показать все данные
Все загруженные данные:
{'Name': 'John', 'Age': '30', 'City': 'New York'}
{'Name': 'Alice', 'Age': '25', 'City': 'Chicago'}
```

---

## 🛠 Запуск тестов

Для запуска тестов используйте команду:

```sh
pytest tests/
```

'
