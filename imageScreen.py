import pyautogui
import cv2
import numpy as np
import pytesseract
from PIL import Image
from pytesseract import Output


def getScreenShot():
    global original_image

    # img = pyautogui.screenshot()    #返回值为一个Img对象

    img = pyautogui.screenshot(region=(0,0, 300, 400))
    img.save('C:/Users/11947/Desktop/pyTestImg.jpg')



# 安装tesseract ： https://digi.bib.uni-mannheim.de/tesseract/
def recognition_img():
    pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    pytesseract.pytesseract.tesseract_cmd = pytesseract_cmd
    img = Image.open(r'C:\Users\11947\Desktop\pyTestImg.jpg')
    print(pytesseract.image_to_string(img))


getScreenShot()
# recognition_img()

