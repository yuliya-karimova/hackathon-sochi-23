from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

@app.route('/analyse')
def analyse():
    # Получение параметров x и y из запроса
    x = float(request.args.get('x', 0))  # Если x не указан, по умолчанию 0
    y = float(request.args.get('y', 0))  # Если y не указан, по умолчанию 0

    # Вычисление суммы
    result = x + y

    # Возвращение результата
    return str(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

CORS(app)
