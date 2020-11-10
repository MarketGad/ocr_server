
from flask import Flask
import cv2 
import pytesseract

app = Flask(__name__)


img = cv2.imread('ss.jpeg')
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)

print(text)


@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'