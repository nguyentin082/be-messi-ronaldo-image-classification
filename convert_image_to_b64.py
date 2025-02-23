import cv2
import base64


def get_b64_from_img(image):
    try:
        # Chuyển ảnh OpenCV (numpy array) sang định dạng PNG
        _, buffer = cv2.imencode('.png', image)

        # Mã hóa buffer thành base64
        b64_text = base64.b64encode(buffer).decode('utf-8')

        return b64_text
    except Exception as e:
        print("Lỗi khi chuyển ảnh sang Base64:", e)
        return None