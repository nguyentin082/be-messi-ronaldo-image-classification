from flask import Flask, request, jsonify
from flask_cors import CORS
import util
from get_image_from_b64 import get_img_from_b64_text
import matplotlib
from dotenv import load_dotenv
import os
from load_model import load_classification_model
matplotlib.use('Agg')  # Sử dụng backend không GUI


# Tải biến môi trường từ .env
load_dotenv()
allowed_origins = os.getenv("ALLOWED_ORIGINS")

app = Flask(__name__)

# Kích hoạt CORS đúng cách
CORS(app, supports_credentials=True, origins=[allowed_origins])

@app.route('/', methods=['GET'])
def hello():
    return 'hi'

@app.route('/classify-image', methods=['POST'])
def classify_image():
    image_data = request.form['image_data']
    image = get_img_from_b64_text(image_data)
    response = jsonify(util.classify_img(image))
    return response

if __name__ == '__main__':
    load_classification_model()
    app.run(port=5000)