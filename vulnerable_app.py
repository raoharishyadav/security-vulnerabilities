import sqlite3
from flask import Flask, request
import os

app = Flask(__name__)
db_path = 'users.db'

# 1. SQL Injection
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    return "Logged in" if result else "Invalid credentials"

# 2. Command Injection
@app.route('/ping', methods=['GET'])
def ping():
    ip = request.args.get('ip')
    os.system(f"ping -c 1 {ip}")
    return "Pinged"

# 3. Hardcoded Secrets
API_KEY = "12345-SECRET-KEY-HARDCODED"

# 4. Insecure Deserialization
import pickle
@app.route('/load', methods=['POST'])
def load_data():
    data = request.data
    obj = pickle.loads(data)
    return str(obj)

# 5. XSS
@app.route('/comment', methods=['POST'])
def comment():
    comment = request.form['comment']
    return f"<h1>{comment}</h1>"
