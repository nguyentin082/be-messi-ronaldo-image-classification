import os

import cv2
import numpy as np

from convert_image_to_b64 import get_b64_from_img
from get_cropped_image import get_cropped_image_if_has_2_eyes

from wavelet import w2d
from load_model import load_classification_model
import global_variables


def classify_img(img):
    cropped_images = get_cropped_image_if_has_2_eyes(img)
    result = []

    for idx, image in enumerate(cropped_images):
        # Scale raw image
        scaled_raw_image = cv2.resize(image, (32, 32))
        # Wavelet transform
        haar_image = w2d(image, 'db1', 5)
        # Scale and Resize
        scaled_haar_image = cv2.resize(haar_image, (32, 32)).astype(np.float32)
        # Combined image
        combined_image = np.concatenate((scaled_raw_image.flatten(), scaled_haar_image.flatten()))

        # Check model loading
        if global_variables.__model is None:
            print("Lỗi: Mô hình chưa được load!")
            return []

        # Predict by loaded model
        y_pred = global_variables.__model.predict(combined_image.reshape(1, -1))
        y_pred_proba = global_variables.__model.predict_proba(combined_image.reshape(1, -1))

        # Lấy tên class dự đoán từ dictionary
        predicted_class = next((k for k, v in global_variables.__dict.items() if v == y_pred[0]), None)

        print(f"Người thứ {idx + 1} được dự đoán là: {predicted_class}")
        print(f"Tỉ lệ dự đoán Messi//Ronaldo là: {y_pred_proba.tolist()}")

        result.append(
            {
                'faces_detection': get_b64_from_img(image),
                'faces_transform': get_b64_from_img(haar_image),
                'class': predicted_class,
                'class_probability': y_pred_proba.tolist()
            }
        )

    return result

if __name__ == '__main__':
    load_classification_model()
    # img = get_img_from_b64_file_path('base64_messi.txt')
    # folder_path = "./test_image/Ronaldo"
    # for img_name in os.listdir(folder_path):
    #     print(img_name)
    #     img_path = os.path.join(folder_path, img_name)
    #     img = cv2.imread(img_path)
    #     result = classify_img(img)
    #     print(result)
