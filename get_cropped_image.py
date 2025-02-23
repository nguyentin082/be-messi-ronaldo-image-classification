import cv2
import matplotlib.pyplot as plt


def get_cropped_image_if_has_2_eyes(img):
    # Load pre-trained Haar cascades
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')

    cropped_faces = []

    if img is None:
        print("Không thể đọc ảnh.")
        return []

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6, minSize=(30, 30))

    if len(faces) == 0:
        # print("Không phát hiện khuôn mặt.")
        return []
    # elif len(faces) == 1:
    #     print("Nhận diện có 1 khuôn mặt.")
    # else:
    #     print(f"Nhận diện có {len(faces)} khuôn mặt.")

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Eye detection
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) == 0:
            # print("Khuôn mặt này không có mắt, bỏ qua.")
            continue  # Bỏ qua khuôn mặt này và kiểm tra khuôn mặt khác

        # print("Nhận diện khuôn mặt này có mắt.")
        cropped_faces.append(roi_color)
        # plt.imshow(roi_color)
        # plt.show()

    return cropped_faces  # Trả về danh sách khuôn mặt đã cắt (có thể rỗng)