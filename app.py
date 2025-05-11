from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='school'
)
cursor = conn.cursor()

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/about')
def about():
    home_url = url_for('home')
    return f"This is the About page. Go back to <a href='{home_url}'>Home</a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return f"Hello, {user}"
    return render_template('login.html')

@app.route('/template')
def template_example():
    return render_template('index.html', title='Welcome', message='Flask with Templates')

@app.route('/json', methods=['POST'])
def json_example():
    data = request.get_json()
    return f"Hello {data['name']}"

@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cursor.execute("INSERT INTO students (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        return "Student Added Successfully"
    return render_template('student.html')

@app.route('/students')
def students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    return render_template('students.html', students=data)

if __name__ == '__main__':
    app.run(debug=True)
