from flask import Flask, request, send_file, jsonify, render_template
import os   #file
import uuid   
from encrypt import encrypt_image
from decrypt import decrypt_image

# Set base path
BASE_PATH = r"C:\Users\ASUS\Desktop\project"
UPLOAD_FOLDER = os.path.join(BASE_PATH, 'uploads')
PASSWORD_FILE = os.path.join(BASE_PATH, 'password.txt')

app = Flask(__name__)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    image = request.files['image']
    message = request.form['message']
    password = request.form['password']

    input_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}.jpg")
    output_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}.png")

    image.save(input_path)
    encrypt_image(input_path, output_path, message, password, PASSWORD_FILE)  #call function

    return send_file(output_path, mimetype='image/png')

@app.route('/decrypt', methods=['POST'])
def decrypt_route():
    image = request.files['image']
    password = request.form['password']

    input_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}.png")
    image.save(input_path)

    result = decrypt_image(input_path, password, PASSWORD_FILE)  #call 
    return jsonify({'message': result})

if __name__ == '__main__':
    app.run(debug=True)
