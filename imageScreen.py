import time

import pyautogui
import pytesseract
from PIL import Image
import random

class ImageScreen(object):
    pass

    #
    # def getScreenShot(self):
    #     global original_image
    #
    #     # img = pyautogui.screenshot()    #返回值为一个Img对象
    #
    #     time.sleep(1)
    #     img = pyautogui.screenshot(region=(50,670, 300, 300))
    #     img.save('C:/Users/11947/Desktop/pyTestImg.jpg')
    #
    #
    #
    # # 安装tesseract ： https://digi.bib.uni-mannheim.de/tesseract/
    # # 语言包安装https://tesseract-ocr.github.io/tessdoc/Data-Files
    # def recognition_img(self):
    #     pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    #     pytesseract.pytesseract.tesseract_cmd = pytesseract_cmd
    #     img = Image.open(r'C:\Users\11947\Desktop\1.jpeg')
    #     text = pytesseract.image_to_string(img, lang='chi_sim')
    #     print(text)
    #     print('闪')
    #     return '闪' in text

    def check_shiny(self):
        rInt = random.randint(1,10)
        print('random int %d' % rInt)
        if rInt > 5:
            return True
        else:
            return False


# c = ImageScreen()
# c.getScreenShot()
# print(c.recognition_img())
# print(c.check_shiny())

