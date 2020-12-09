from flask import Flask, render_template,request, make_response,flash, redirect, url_for, send_from_directory, session, Response
import cv2 
import pytesseract
from werkzeug.utils import secure_filename
import os
import io
import sys
import json
import base64
import numpy as np
from base64 import decodestring
from PIL import Image
import utils_ocr.clean_text as clean

# textDummy = "hello world 3423#$%@$ 324#$#2e34ertvfhnf2gr hello world"
# print("not cleaned : " + textDummy)
# print("cleaned : " + clean.clean_text(textDummy))

UPLOAD_FOLDER = os.getcwd() + "/UploadFiles"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# CREATE FLASK application
application = Flask(__name__)
application.secret_key = "super secret key"
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

application.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 2
# application.run(host='0.0.0.0')

def ocr(data):
    image = Image.open(io.BytesIO(base64.b64decode(data["photo"])))
    image_np = np.array(image)
    print(": Image conversion Succeeded :")
    # print(image)
    custom_config = r'--oem 3 --psm 6'
    text = '00 km'
    print(" Request to OCR ")
    try:
        text = pytesseract.image_to_string(image_np, config=custom_config)
    
    except:
        print(" tesseract returned error ")

    print(" Response from OCR ")
    return text

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/ocr', methods=['POST'])
def ExtractTextFromOcr():
    data = json.loads(request.data)
    print(": Request received :")
    result = ocr(data)
    print(": OCR Response received :")

    result = clean.clean_text(result)
    dist = clean.extract_distance(result)
    print(dist)    
    print(result)    
    if(len(dist) > 0):
        return Response(dist[0], status=200 , mimetype='applicationlication/text')
    else:
        return Response("Upload a valid Screenshot", status=400 ,mimetype='applicationlication/json')



if __name__ == "__main__":
    application.debug = True
    application.run(ssl_context=('cert.pem', 'key.pem'))
