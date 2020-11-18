import cv2 
import numpy as np
import pytesseract

def ocr(props):

    print(props)
    
    img = cv2.imread('ss.jpeg')
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=custom_config)

    return text