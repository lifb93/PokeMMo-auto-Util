import time

import pyautogui
from PIL import Image
import random
import easyocr

from src.common import PokeConfig
from src.common.ScreenPoke import ScreenPoke

# import pytesseract

# -i https://mirrors.aliyun.com/pypi/simple some-package

class ImageScreen(object):
    pass

    def __init__(self):
        self.filter_shiny = ['闪光', 'shiny', '闪']
        self.filter_list = ['Suicune', 'Entei', 'Raikou', 'Zapdos', 'Articuno', 'Moltres']
        self.filter_list_zh = ['水君', '炎帝', '雷公', '闪电鸟', '急冻鸟', '火焰鸟']
        self.filter_list_ext = ['君', '帝', '公', '闪电', '急冻', '火焰']
        self.encounter_win = [0, 930, 500, 150]
        self.battle_win = [0, 750, 500, 300]
        self.poke_win = [200, 50, 1300, 300]


    def scan_win(self):
        try:
            point_list = []
            count = 0
            while count < 2:
                time.sleep(5)
                scw, seh = pyautogui.size()
                x, y = pyautogui.position()

                print(" %s %s , x: %s y: %s " % (scw, seh, x, y))
                point_list.append(int(x))
                point_list.append(int(y))
                count += 1

            print('point_list : %d , %d , %d , %d' % (point_list[0], point_list[1], point_list[2], point_list[3]))
        except KeyboardInterrupt:
            print('end')


    def getScreenShot(self, topX, topY, width, high, url):
        # img = pyautogui.screenshot()    #返回值为一个Img对象
        img = pyautogui.screenshot(url,region=(topX,topY,width,high))
        if PokeConfig.GREY_IMG:
            img = img.convert("L")
        img.save(url)
        return url

    def addFiltItem(self, item):
        self.filter_list_zh.append(item)

    def read_text(self, url):
        reader = easyocr.Reader(['en', 'ch_sim'], gpu=False)
        text = reader.readtext(url, detail=0)
        return text

    def read_en_text(self, url):
        reader = easyocr.Reader(['en'], gpu=False)
        text = reader.readtext(url, detail=0)
        return text

    def recognition_text(self,  text):
        screenPoke = ScreenPoke()
        size = 0
        poke = None
        for item in text:
            if poke is None:
                if 'L' in item:
                    index = item.index('L')
                    poke = item[0:index]
                    poke = poke.strip()
                    size += 1
            else:
                if poke in item:
                    size += 1
                elif 'L' in item:
                    index = item.index('L')
                    poke = item[0:index]
                    poke = poke.strip()
                    size += 1

        size = len(text)
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
        # print(target)

        sp = self.recognition_text(text)
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

        sp = self.recognition_text(text)
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
        print("filter list :  %s " % (self.filter_shiny))
        self.getScreenShot(self.poke_win[0],self.poke_win[1], self.poke_win[2], self.poke_win[3], PokeConfig.IMAGE_URL)
        text = self.read_text(PokeConfig.IMAGE_URL)
        print(text)
        return self.recognition_img(text, self.filter_shiny).isTarget

    def check_default_list(self):
        time.sleep(1)
        target = self.filter_shiny + self.filter_list_zh + self.filter_list
        self.getScreenShot(self.poke_win[0],self.poke_win[1], self.poke_win[2], self.poke_win[3], PokeConfig.IMAGE_URL)
        text = self.read_text(PokeConfig.IMAGE_URL)
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
        target = self.filter_shiny + self.filter_list_zh + self.filter_list
        target.append(tarItem)
        self.getScreenShot(self.poke_win[0],self.poke_win[1], self.poke_win[2], self.poke_win[3], PokeConfig.IMAGE_URL)
        text = self.read_text(PokeConfig.IMAGE_URL)
        print(text)
        return self.recognition_img(text, target)

    def check_forget_skill(self):
        time.sleep(1)
        self.getScreenShot(self.encounter_win[0],self.encounter_win[1], self.encounter_win[2], self.encounter_win[3], PokeConfig.IMAGE_URL)
        text = self.read_text(PokeConfig.IMAGE_URL)
        print(text)
        return self.recognition_img(text, ['掌握','四个','技能']).isTarget

    def check_default_list_with_text(self, text):
        time.sleep(1)
        target = self.filter_shiny + self.filter_list_zh + self.filter_list
        return self.recognition_img(text, target)

    def check_sweet_scent_talk(self):
        time.sleep(1)
        self.getScreenShot(self.poke_win[0],self.poke_win[1], self.poke_win[2], self.poke_win[3], PokeConfig.IMAGE_URL)
        text = self.read_text(PokeConfig.IMAGE_URL)
        print(text)
        target = ['pp', '补充']
        return self.recognition_img(text, target)


    def grey_test(self):
        origin = r'C:\Users\11947\Desktop\poke_action 2.png'
        img = Image.open(origin)
        imgGrey = img.convert('L')
        origin_grep = r'C:\Users\11947\Desktop\poke_action2_grep.png'
        imgGrey.save(origin_grep)

        # print(img.width)
        # print(img.height)
        # box = (0, 0, img.width/2 , img.height)

        cat_path = r'C:\Users\11947\Desktop\poke_action_cat.png'
        # img = img.crop(box)
        # img = img.resize((img.width * 2, img.height * 2), Image.BICUBIC)
        # img.save(cat_path)

        # grep = img.convert('L')
        path = r'C:\Users\11947\Desktop\poke_action_grey.png'
        # grep.save(path)

        text = self.read_text(origin_grep)
        print(text)
        text = self.read_text(path)
        print(text)
        text = self.read_text(cat_path)
        print(text)


# l = ['比比乌 LV。 48', '比比鸟 LV。 47 $', '比比乌 LV。 48古', '比比鸟 LV。 48古', '比比鸟 LV。 46古']
# c = ImageScreen()
# path = r'C:\Users\Administrator\Desktop\poke_action.png'
# t = c.read_en_text(path)
# print(t)
# t = c.read_text(path)
# print(t)
# c.check_default_list()
# c.grey_test()
# c.scan_win()
# poke = c.recognition_text(l)
# print(poke.to_str())
# c.addFiltItem('TestStr')
# sp = c.check_default_list()
# sp = c.check_forget_skill()
# print(sp.to_str())
# print(c.check_fire())
# print(c.check_shiny())
# print(c.check_shiny())




