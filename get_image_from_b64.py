import base64
import io
import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def get_img_from_b64_file_path(b64_file_path):
    with open(b64_file_path, "r") as f:
        base64_string = f.read().strip()

    # Xử lý nếu Base64 có header
    if "," in base64_string:
        base64_string = base64_string.split(",")[1]  # Bỏ phần đầu (nếu có)

    try:
        img_data = base64.b64decode(base64_string)
        img = Image.open(io.BytesIO(img_data))

        opencv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # plt.imshow(opencv_img)
        # plt.show()
        return opencv_img
    except Exception as e:
        print("Lỗi khi giải mã ảnh từ Base64:", e)
        return None




def get_img_from_b64_text(b64_text):

    # Xử lý nếu Base64 có header
    if "," in b64_text:
        b64_text = b64_text.split(",")[1]  # Bỏ phần đầu (nếu có)

    try:
        img_data = base64.b64decode(b64_text)
        img = Image.open(io.BytesIO(img_data))

        opencv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # plt.imshow(opencv_img)
        # plt.show()
        return opencv_img
    except Exception as e:
        print("Lỗi khi giải mã ảnh từ Base64:", e)
        return None