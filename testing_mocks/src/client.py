import requests
import sys

SERVER_URL = "http://localhost:5000"

def register_user():
    username = input("Введите имя пользователя для регистрации: ").strip()
    try:
        response = requests.post(f"{SERVER_URL}/register", json={"username": username})
    except requests.exceptions.RequestException as e:
        print("Ошибка подключения к серверу:", e)
        return

    if response.status_code == 201:
        print(response.json()["message"])
    elif response.status_code == 400 and "Пользователь уже существует" in response.text:
        print("Пользователь уже зарегистрирован.")
    else:
        print("Ошибка регистрации:", response.text)

def upload_csv():
    username = input("Введите имя пользователя: ").strip()
    file_path = input("Введите путь к CSV файлу: ").strip()
    try:
        with open(file_path, 'rb') as f:
            files = {
                'file': (f.name, f, 'text/csv')
            }
            data = {
                'username': username
            }
            try:
                response = requests.post(f"{SERVER_URL}/upload", files=files, data=data)
            except requests.exceptions.RequestException as e:
                print("Ошибка подключения к серверу:", e)
                return

            if response.status_code == 200:
                print(response.json()["message"])
            else:
                print("Ошибка загрузки:", response.text)
    except FileNotFoundError:
        print("Файл не найден")

def list_users():
    try:
        response = requests.get(f"{SERVER_URL}/users")
    except requests.exceptions.RequestException as e:
        print("Ошибка подключения к серверу:", e)
        return

    if response.status_code == 200:
        users = response.json()
        print("Список пользователей:")
        for user in users:
            print("-", user)
    else:
        print("Ошибка получения списка пользователей:", response.text)

def get_user_data():
    username = input("Введите имя пользователя: ").strip()
    try:
        response = requests.get(f"{SERVER_URL}/user_data/{username}")
    except requests.exceptions.RequestException as e:
        print("Ошибка подключения к серверу:", e)
        return

    if response.status_code == 200:
        records = response.json()
        print(f"Данные пользователя {username}:")
        for record in records:
            print(record)
    else:
        print("Ошибка получения данных:", response.text)

def get_all_data():
    try:
        response = requests.get(f"{SERVER_URL}/data")
    except requests.exceptions.RequestException as e:
        print("Ошибка подключения к серверу:", e)
        return

    if response.status_code == 200:
        records = response.json()
        print("Все загруженные данные:")
        for record in records:
            print(record)
    else:
        print("Ошибка получения данных:", response.text)

def main_menu():
    while True:
        print("\nМеню:")
        print("1. Зарегистрировать пользователя")
        print("2. Загрузить CSV файл")
        print("3. Показать список пользователей")
        print("4. Показать данные пользователя")
        print("5. Показать все данные")
        print("0. Выход")
        choice = input("Выберите опцию: ").strip()
        if choice == "1":
            register_user()
        elif choice == "2":
            upload_csv()
        elif choice == "3":
            list_users()
        elif choice == "4":
            get_user_data()
        elif choice == "5":
            get_all_data()
        elif choice == "0":
            print("Выход.")
            sys.exit(0)
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main_menu()
