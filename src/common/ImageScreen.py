import time

import pyautogui
from PIL import Image
import random
import easyocr

from src.common.ScreenPoke import ScreenPoke

# import pytesseract

IMAGE_URL = r"C:/Users/11947/Desktop/3.png"

# -i https://mirrors.aliyun.com/pypi/simple some-package

class ImageScreen(object):
    pass

    def __init__(self):
        self.filter_shiny= ['闪光', 'shiny']
        self.filter_list= ['Suicune', 'Entei', 'Raikou', 'Zapdos', 'Articuno', 'Moltres']
        self.filter_list_zh= [ '水君', '炎帝', '雷公', '闪电鸟', '急冻鸟', '火焰鸟']
        self.battle_win = [0, 750, 500, 300]
        self.poke_win = [200, 50, 1300, 300]


    def scan_win(self):
        try:
            while True:
                scw, seh = pyautogui.size()
                x, y = pyautogui.position()

                print(" %s %s , x: %s y: %s " % (scw, seh, x, y))
                time.sleep(1)
        except KeyboardInterrupt:
            print('end')


    def getScreenShot(self, topX, topY, width, high, url):
        # img = pyautogui.screenshot()    #返回值为一个Img对象
        img = pyautogui.screenshot(url,region=(topX,topY,width,high))
        img.save(url)
        return url

    def addFiltItem(self, item):
        self.filter_list_zh.append(item)

    def read_text(self, url):
        reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
        text = reader.readtext(url)
        return text

    def recognition_text(self, screenPoke, text):
        size = 0
        poke = None
        for item in text:
            if poke is None:
                if 'Lv' in item:
                    index = item.index('Lv')
                    poke = item[0, index]
                    size += 1
            else:
                if poke in item:
                    size += 1

        screenPoke.__set_poke__(poke)
        screenPoke.__set_size__(size)
        return screenPoke



    # 安装tesseract ： https://digi.bib.uni-mannheim.de/tesseract/
    # 语言包安装https://tesseract-ocr.github.io/tessdoc/Data-Files
    # 隐藏maxvit中的OrderedDict的包 pip install collective.ordereddict
    def recognition_img(self, text, target):
        # pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # pytesseract.pytesseract.tesseract_cmd = pytesseract_cmd
        # img = Image.open(url)
        # text = pytesseract.image_to_string(img, lang='chi_sim')

        sp = ScreenPoke()
        self.recognition_text(sp, text)
        has_target = False
        for item in text:
            if not has_target:
                for tar in target:
                    if not has_target and tar in item:
                        has_target = True
                        print('遇到： %s ' % tar)
                        break

        sp.__set_is_target__(has_target)
        sp.__set_text__(text)
        return sp


    def recognition_poke(self, text, target):

        sp = ScreenPoke()
        self.recognition_text(sp, text)
        has_target = False
        for item in text:
            if target in item:
                has_target = True
                sp.__set_poke__(target)
                break

        sp.__set_is_target__(has_target)
        sp.__set_text__(text)
        return sp

    def check_shiny(self):
        time.sleep(1)
        self.getScreenShot(self.poke_win[0],self.poke_win[1], self.poke_win[2], self.poke_win[3], IMAGE_URL)
        print("filter list :  %s " % (self.filter_shiny))
        text = self.read_text(IMAGE_URL)
        print(text)
        return self.recognition_img(text, self.filter_shiny).isTarget

    def check_default_list(self):
        time.sleep(1)
        self.getScreenShot(self.poke_win[0],self.poke_win[1], self.poke_win[2], self.poke_win[3], IMAGE_URL)
        target = self.filter_shiny + self.filter_list_zh + self.filter_list
        text = self.read_text(IMAGE_URL)
        print(text)
        return self.recognition_img(text, target)

        # rInt = random.randint(1,10)
        # print('random int %d' % rInt)
        # if rInt > 5:
        #     return True
        # else:
        #     return False

    def check_target_poke(self, tarItem):
        time.sleep(1)
        self.getScreenShot(self.poke_win[0],self.poke_win[1], self.poke_win[2], self.poke_win[3], IMAGE_URL)
        target = self.filter_shiny + self.filter_list_zh + self.filter_list
        target.append(tarItem)
        text = self.read_text(IMAGE_URL)
        print(text)
        return self.recognition_img(text, target)

    def check_forget_skill(self):
        time.sleep(1)
        self.getScreenShot(self.battle_win[0],self.battle_win[1], self.battle_win[2], self.battle_win[3], IMAGE_URL)
        text = self.read_text(IMAGE_URL)
        print(text)
        return self.recognition_img(text, ['掌握','四个','技能']).isTarget


    def check_fire(self):
        time.sleep(1)
        self.getScreenShot(self.battle_win[0],self.battle_win[1], self.battle_win[2], self.battle_win[3], IMAGE_URL)
        text = self.read_text(IMAGE_URL)
        print(text)
        return self.recognition_poke(text, '野生')

    def check_default_list_with_text(self, text):
        time.sleep(1)
        target = self.filter_shiny + self.filter_list_zh + self.filter_list
        return self.recognition_img(text, target)


# c = ImageScreen()
# c.addFiltItem('TestStr')
# print(c.check_default_list())
# print(c.check_fire())
# print(c.check_shiny())
# print(c.check_shiny())




