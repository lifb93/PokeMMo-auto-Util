import time

import pyautogui
from PIL import Image
import random
import easyocr
# import pytesseract

IMAGE_URL = r"C:/Users/11947/Desktop/3.png"

# -i https://mirrors.aliyun.com/pypi/simple some-package

class ImageScreen(object):
    pass


    def getScreenShot(self, topX, topY, width, high, url):
        # img = pyautogui.screenshot()    #返回值为一个Img对象
        img = pyautogui.screenshot(url,region=(topX,topY,width,high))
        img.save(url)

    # 安装tesseract ： https://digi.bib.uni-mannheim.de/tesseract/
    # 语言包安装https://tesseract-ocr.github.io/tessdoc/Data-Files
    # 隐藏maxvit中的OrderedDict的包 pip install collective.ordereddict
    def recognition_img(self, url):
        # pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # pytesseract.pytesseract.tesseract_cmd = pytesseract_cmd
        img = Image.open(url)
        # text = pytesseract.image_to_string(img, lang='chi_sim')

        reader = easyocr.Reader(['ch_sim', 'en'],gpu=False)
        text = reader.readtext(url,detail=0)

        print(text)
        hasShiny = False
        for item in text:
            if not hasShiny and '闪光' in item:
                print(item)
                hasShiny = True
                break
        return hasShiny

    def check_shiny(self):
        time.sleep(1)
        c = ImageScreen()
        c.getScreenShot(0,750, 500, 300, IMAGE_URL)
        return c.recognition_img(IMAGE_URL)


        # rInt = random.randint(1,10)
        # print('random int %d' % rInt)
        # if rInt > 5:
        #     return True
        # else:
        #     return False


# c = ImageScreen()
# c.getScreenShot()
# print(c.check_shiny())
# print(c.check_shiny())
# print(c.check_shiny())

