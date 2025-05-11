# Flask Web App with MySQL Integration

This project demonstrates key Flask concepts with a practical hands-on web application connected to a MySQL database.

## Features Covered

- Flask Setup & Routing
- URL Building
- HTTP Methods (GET & POST)
- HTML Templates (Jinja2)
- Request Body Handling
- JSON Data Handling
- Connecting Flask to MySQL
- Web Forms and Dynamic Data Rendering

## Folder Structure

```
flask_app/
│
├── app.py               # Main Flask application
├── templates/           # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── student.html
│   └── students.html
└── static/              # Static files (currently empty)
```

## Setup Instructions

1. **Install Required Packages**

```bash
pip install flask mysql-connector-python
```

2. **Create MySQL Database and Table**

```sql
CREATE DATABASE school;

USE school;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
```

3. **Edit Database Credentials in `app.py`**

Replace:
```python
user='root',
password='yourpassword'
```
with your MySQL login details.

4. **Run the Flask Application**

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Pages

- `/` – Home page
- `/about` – URL building example
- `/login` – HTML form (GET/POST)
- `/template` – Template rendering
- `/json` – JSON request handling (POST)
- `/student` – Add student form connected to MySQL
- `/students` – Display students from MySQL table

---

© 2025 Flask Tutorial
