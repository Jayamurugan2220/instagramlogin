from flask import Flask, request, render_template, jsonify, redirect, url_for
import os

app = Flask(__name__)

# Ensure the data file exists
DATA_FILE = "user_data.txt"
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        file.write("Username,Password\n")

FORGOT_PASS_FILE = "forgot_password_requests.txt"
if not os.path.exists(FORGOT_PASS_FILE):
    with open(FORGOT_PASS_FILE, "w") as file:
        file.write("Email\n")

@app.route('/', methods=['GET'])
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Save login attempt to file
    with open(DATA_FILE, "a") as file:
        file.write(f"{username},{password}\n")

    # Dummy authentication (replace with real authentication later)
    if username == "admin" and password == "admin123":
        return jsonify({"message": "Login successful!", "redirect": url_for('dashboard')}), 200
    else:
        return jsonify({"message": "Incorrect credentials"}), 401

@app.route('/forgot-password', methods=['GET'])
def forgot_password():
    return render_template('forgotpass.html')

@app.route('/forgot-password', methods=['POST'])
def forgot_password_post():
    data = request.get_json()
    email = data.get('email')

    # Save email request to file
    with open(FORGOT_PASS_FILE, "a") as file:
        file.write(f"{email}\n")

    return jsonify({"message": "Password reset link sent to your email!"}), 200

@app.route('/dashboard')
def dashboard():
    return "<h1>Welcome to the Dashboard!</h1> <p>Dashboard content coming soon...</p>"

if __name__ == '__main__':
    app.run(debug=True)
