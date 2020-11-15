from flask import Flask, render_template,request, make_response,flash, redirect, url_for, send_from_directory, session
import cv2 
import pytesseract
from werkzeug.utils import secure_filename
import os
import io
import sys
import json
import base64
from base64 import decodestring

import utils_ocr.clean_text as clean

# textDummy = "hello world 3423#$%@$ 324#$#2e34ertvfhnf2gr hello world"
# print("not cleaned : " + textDummy)
# print("cleaned : " + clean.clean_text(textDummy))

UPLOAD_FOLDER = os.getcwd() + "/UploadFiles"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# CREATE FLASK APP
app = Flask(__name__)
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.debug = True
# app.run(host='0.0.0.0')

def ocr(data):
    with open("UploadFiles/ss.jpeg", "wb") as fh:
        fh.write(base64.b64decode(data["photo"]))
    img = cv2.imread("UploadFiles/ss.jpeg")
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=custom_config)
    return text

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ocr', methods=['POST'])
def ExtractTextFromOcr():
    data = json.loads(request.data)
    result = ocr(data)
    result = clean.clean_text(result)
    dist = clean.extract_distance(result)
    print(dist)    
    print(result)    
    if(len(dist) > 0):
        return dist[0]
    else:
        return "Upload a valid Screenshot"

if __name__ == "__main__":
    app.run()
