
from flask import Flask, render_template,request, make_response,flash, redirect, url_for, send_from_directory, session
import cv2 
import pytesseract
from werkzeug.utils import secure_filename
import os
import io
import sys
import json
from numpy import asarray 
import base64
# from flask.ext.session import Session
SESSION_TYPE = 'memcache'

# import ocr from utils 
UPLOAD_FOLDER = os.getcwd() + "/UploadFiles"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)
# sess = Session()
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.run(host='0.0.0.0')

nextId = 0

# def verifySessionId():
#     global nextId

#     if not 'userId' in session:
#         session['userId'] = nextId
#         nextId += 1
#         sessionId = session['userId']
#         print ("set userid[" + str(session['userId']) + "]")
#     else:
#         print ("using already set userid[" + str(session['userId']) + "]")
#     sessionId = session.get('userId', None)
#     return sessionId
from base64 import decodestring

def ocr(data):
    # print("inside ocr")
    # path = "UploadFiles/"+img.filename
    # print("img path : " + path)
    with open("UploadFiles/ss.jpeg", "wb") as fh:
        fh.write(base64.b64decode(data["photo"]))

    # print(data.keys())
    img = cv2.imread("UploadFiles/ss.jpeg")
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=custom_config)

    print(text)
    return text


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    # userId = verifySessionId()
    return render_template('register.html')
  
@app.route('/ocr', methods=['POST'])
def ExtractTextFromOcr():
    # userId = verifySessionId()
    # print(request)

    # print(request.data)
    data = json.loads(request.data)
    # if 'file' not in request.files:
    #     print('no file part')
    #     flash('No file part')
    #     return { "message": "NULL"}
    # file = request.files['file']
    # print('files extracted')
    # print(file.filename)

    # if file.filename == '':
    #     flash('No selected file')
    #     # return render_template('index.html')

    result = ""
    # print(data)

    # if file and allowed_file(file.filename):
    #     filename = secure_filename(file.filename)
    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #     # props["img"] = file
    result = ocr(data)

    print(result)
    return result

if __name__ == "__main__":
    # app.secret_key = 'super secret key'

    # sess.init_app(app)

    app.debug = True
    app.run()