from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import re
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Read env variables
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Database connection
db = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

cursor = db.cursor()

# Validation patterns
username_pattern = r'^(?=.*[^a-zA-Z0-9])[a-zA-Z0-9_.@\- ]{2,50}$'
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%?&-]).{8,}$'


# ---------------- Register API ----------------

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not re.match(username_pattern, username):
        return jsonify({"success": False, "message": "Invalid username format"})

    if not re.match(password_pattern, password):
        return jsonify({"success": False, "message": "Invalid password format"})

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user:
        return jsonify({"success": False, "message": "User already exists"})

    hashed_password = generate_password_hash(password, method="scrypt")

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, hashed_password)
    )
    db.commit()

    return jsonify({"success": True, "message": "Registration successful"})
  

# ---------------- Login API ----------------

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not re.match(username_pattern, username):
        return jsonify({"success": False, "message": "Invalid username format"})

    if not re.match(password_pattern, password):
        return jsonify({"success": False, "message": "Invalid password format"})

    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    if not user:
        return jsonify({"success": False, "message": "User not found, Try registration."})

    if check_password_hash(user[0], password):
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"})


# ---------------- Run Server ----------------

if __name__ == "__main__":
    app.run(debug=True)
