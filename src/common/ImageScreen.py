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

    def __init__(self):
        self.filter_list= ['shiny', 'Suicune', 'Entei', 'Raikou', 'Zapdos', 'Articuno', 'Moltres']
        self.filter_list_zh= ['闪光', '水君', '炎帝', '雷公', '闪电鸟', '急冻鸟', '火焰鸟']

    def getScreenShot(self, topX, topY, width, high, url):
        # img = pyautogui.screenshot()    #返回值为一个Img对象
        img = pyautogui.screenshot(url,region=(topX,topY,width,high))
        img.save(url)

    def addFiltItem(self, item):
        self.filter_list_zh.append(item)

    # 安装tesseract ： https://digi.bib.uni-mannheim.de/tesseract/
    # 语言包安装https://tesseract-ocr.github.io/tessdoc/Data-Files
    # 隐藏maxvit中的OrderedDict的包 pip install collective.ordereddict
    def recognition_img(self, url, target):
        # pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # pytesseract.pytesseract.tesseract_cmd = pytesseract_cmd
        # img = Image.open(url)
        # text = pytesseract.image_to_string(img, lang='chi_sim')

        reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
        text = reader.readtext(url, detail=0)

        print(text)
        has_target = False
        for item in text:
            if not has_target:
                for tar in target:
                    if not has_target and tar in item:
                        has_target = True
                        break
        return has_target

    def check_shiny(self):
        time.sleep(1)
        c = ImageScreen()
        c.getScreenShot(0,750, 500, 300, IMAGE_URL)
        target = [self.filter_list[0], self.filter_list_zh[0]]
        print("filter list :  %s " % (target))
        return c.recognition_img(IMAGE_URL, target)

    def check_default_list(self):
        time.sleep(1)
        c = ImageScreen()
        c.getScreenShot(0,750, 500, 300, IMAGE_URL)
        target = self.filter_list_zh + self.filter_list
        print("filter list :  %s " % (target))
        return c.recognition_img(IMAGE_URL, target)

        # rInt = random.randint(1,10)
        # print('random int %d' % rInt)
        # if rInt > 5:
        #     return True
        # else:
        #     return False


# c = ImageScreen()
# c.addFiltItem('TestStr')
# c.check_default_list()
# print(c.check_shiny())
# print(c.check_shiny())
# print(c.check_shiny())

