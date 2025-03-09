# Sử dụng Python 3.10 làm base image
FROM python:3.10

# Đặt biến môi trường tránh tạo file pyc và đảm bảo stdout không bị buffer
# ENV PYTHONUNBUFFERED 1

# Tạo thư mục làm việc trong container
WORKDIR /app

# Sao chép file requirements.txt vào container và cài đặt dependencies
COPY requirements.txt .

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Mở port 8000 cho Django
EXPOSE 8000

# Lệnh mặc định để chạy Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

