from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image, ImageDraw
import os
import random

app = Flask(__name__)
CORS(app)

# Функция для сохранения изображений на сервере
def save_image(img):
    img_name = f"random_{random.randint(1, 1000)}.png"
    img_path = os.path.join("static", img_name)
    img.save(img_path)
    return f"http://127.0.0.1:5000/{img_path}"

# Функция для генерации случайного изображения
def create_random_image():
    img = Image.new('RGB', (100, 100), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), "Random Image", fill=(255, 255, 255))
    return img

@app.route('/analyse')
def analyse():
    # Получение параметров x и y из запроса
    x = float(request.args.get('x', 0))  # Если x не указан, по умолчанию 0
    y = float(request.args.get('y', 0))  # Если y не указан, по умолчанию 0

    # Вычисление суммы
    result = x + y

    # Генерация двух изображений
    images = [save_image(create_random_image()) for _ in range(2)]

    # Возвращение результата и URL изображений
    return jsonify({"result": result, "images": images})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
