# Sử dụng Python 3.9
FROM python:3.9

WORKDIR /app
# Cài đặt thư viện OpenGL cần thiết cho OpenCV
RUN apt-get update && apt-get install -y libgl1-mesa-glx
COPY requirements.txt ./
# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

EXPOSE 5000
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "main:app"]