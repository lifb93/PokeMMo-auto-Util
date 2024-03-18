import pyautogui
import cv2
import numpy as np
import pytesseract
from PIL import Image
from pytesseract import Output


def getScreenShot():
    global original_image

    img = pyautogui.screenshot()    #返回值为一个Img对象
    # img = np.array(img)    #将Img对象转换成ndarray
    # original_image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img.save('C:/Users/11947/Desktop/pyTestImg.jpg')



def recognition_img():
    pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    pytesseract.pytesseract.tesseract_cmd = pytesseract_cmd
    img = Image.open(r'C:\Users\11947\Desktop\pyTestImg.jpg')
    print(pytesseract.image_to_string(img))


getScreenShot()
recognition_img()

