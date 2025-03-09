# 📌 Project: Todo-List

## 📑 MỤC LỤC
1. [Thông tin thành viên](#👥-thông-tin-thành-viên)
2. [Giới thiệu](#📖-giới-thiệu)
3. [Hướng dẫn cài đặt và chạy ứng dụng](#🚀-hướng-dẫn-cài-đặt-và-chạy-ứng-dụng)
   - [Clone repository](#1️⃣-clone-repository)
   - [Di chuyển vào thư mục dự án](#2️⃣-di-chuyển-vào-thư-mục-dự-án)
   - [Tạo môi trường ảo](#3️⃣-tạo-môi-trường-ảo-venv)
   - [Kích hoạt môi trường ảo](#4️⃣-kích-hoạt-môi-trường-ảo)
   - [Cài đặt dependencies](#5️⃣-cài-đặt-dependencies)
   - [Thiết lập database](#6️⃣-thiết-lập-database)
   - [Chạy ứng dụng](#7️⃣-chạy-ứng-dụng)
4. [Công nghệ sử dụng](#📌-công-nghệ-sử-dụng)


---

## 👥 Thông tin thành viên
- **Nguyễn Thị Viên** - `22003025`
- **Đường Chí Trung** - `22655141`

---

## 📖 Giới thiệu
**Todo-List** là một ứng dụng web đơn giản giúp bạn quản lý công việc hàng ngày. Người dùng có thể tạo danh sách việc cần làm, chỉnh sửa, đánh dấu hoàn thành hoặc xóa công việc.

---

## 🚀 Hướng dẫn cài đặt và chạy ứng dụng

### 1️⃣ **Clone repository**
Mở terminal hoặc command prompt và chạy lệnh:
```sh
 git clone https://github.com/VienVien123/django-tiny-app.git
```

### 2️⃣ **Di chuyển vào thư mục dự án**
```sh
 cd TODO_LIST
```

### 3️⃣ **Tạo môi trường ảo (`venv`)**
```sh
 python -m venv venv
```

### 4️⃣ **Kích hoạt môi trường ảo**
- **Windows:**
  ```sh
  .venv/Scripts/Activate.ps1
  ```
- **Mac/Linux:**
  ```sh
  source venv/bin/activate
  ```

### 5️⃣ **Cài đặt dependencies**
```sh
 pip install -r requirements.txt
```

### 6️⃣ **Thiết lập database**
```sh
 python manage.py makemigrations
 python manage.py migrate
```

### 7️⃣ **Chạy ứng dụng**
```sh
 python manage.py runserver
```

Sau đó, mở trình duyệt và truy cập **[http://127.0.0.1:8000](http://127.0.0.1:8000)** để sử dụng ứng dụng.

---
### Note
1. docker compose up --build
2. docker compose up --build -d

## 📌 Công nghệ sử dụng
- **Python** (Django Framework)
- **HTML, CSS, JavaScript**
- **SQLite** (Database mặc định)

---

