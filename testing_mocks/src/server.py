from flask import Flask, request, jsonify, abort
from csv_parser import parse_csv
from io import BytesIO

app = Flask(__name__)
users = {}


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'username' not in data:
        abort(400, description="Отсутствует 'username' в JSON.")
    username = data['username']
    if username in users:
        abort(400, description="Пользователь уже существует.")
    users[username] = []
    return jsonify({"message": f"Пользователь '{username}' успешно зарегистрирован."}), 201


@app.route('/upload', methods=['POST'])
def upload():
    username = request.form.get('username')
    if not username:
        abort(400, description="Отсутствует параметр 'username' в форме.")
    if username not in users:
        abort(404, description="Пользователь не найден.")
    if 'file' not in request.files:
        abort(400, description="Файл не передан.")

    file = request.files['file']
    try:
        csv_content = file.read().decode('utf-8')
    except Exception:
        abort(400, description="Неверная кодировка файла.")

    records = parse_csv(csv_content)
    users[username].extend(records)
    return jsonify({"message": f"Загружено {len(records)} записей для пользователя '{username}'."}), 200


@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(list(users.keys()))


@app.route('/user_data/<username>', methods=['GET'])
def user_data(username):
    if username not in users:
        abort(404, description="Пользователь не найден.")
    return jsonify(users[username])


@app.route('/data', methods=['GET'])
def all_data():
    all_records = []
    for recs in users.values():
        all_records.extend(recs)
    return jsonify(all_records)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
