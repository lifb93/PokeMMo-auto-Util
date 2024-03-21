import threading
import time
from pykeyboard import PyKeyboard
from pymouse import PyMouse

from imageScreen import ImageScreen

m = PyMouse()
k = PyKeyboard()

THREAD_STOP = 99
A_BUTTON = 'j'
B_BUTTON = 'k'
UP_BUTTON = 'w'
DOWN_BUTTON = 'S'
LEFT_BUTTON = 'a'
RIGHT_BUTTON = 'd'

# https://www.lfd.uci.edu/~gohlke/pythonlibs/ 安装pyhook
# https://pypi.org/project/pywin32/#files
#  pyUserInput install   pyinstaller
# pyinstaller.exe -F .\main.py  打包


# class PokeConfig(object):
#     def __init__(self, up, down, left, right, a, b):
#         self.A_BUTTON = a
#         self.B_BUTTON = b
#         self.UP_BUTTON = up
#         self.DOWN_BUTTON = down
#         self.LEFT_BUTTON = left
#         self.RIGHT_BUTTON = right
#
#     def __str__(self):
#         var = (self.A_BUTTON
#                + " " + self.B_BUTTON
#                + " " + self.UP_BUTTON
#                + " " + self.DOWN_BUTTON
#                + " " + self.LEFT_BUTTON
#                + " " + self.RIGHT_BUTTON
#                )
#         print(var)

def prepare_poke():
    print("请见游戏键盘设置(默认)：上 (w) , 下 (s) , 左 (a) , 右 (d) , a键 (j) , b键 (k)")
    response = input("是否使用默认配置？[Y/N]:")
    # config = PokeConfig(UP_BUTTON, DOWN_BUTTON, LEFT_BUTTON, RIGHT_BUTTON, A_BUTTON, B_BUTTON)
    if response != 'Y' and response != 'y':
        up = input("请输入 (上 键):")
        down = input("请输入 (下 键):")
        left = input("请输入 (左 键):")
        right = input("请输入 (右 键):")
        a = input("请输入 (a 键):")
        b = input("请输入 (b 键):")
        print('up : %s , down : %s , left: %s , right: %s ,a %s ,b %s' % (up, down, left, right, a, b))
        A_BUTTON = a
        B_BUTTON = b
        UP_BUTTON = up
        DOWN_BUTTON = down
        LEFT_BUTTON = left
        RIGHT_BUTTON = right

        # config = PokeConfig(up, down, left, right, a, b)

    # config.__str__()
    var = (A_BUTTON
           + " " + B_BUTTON
           + " " + UP_BUTTON
           + " " + DOWN_BUTTON
           + " " + LEFT_BUTTON
           + " " + RIGHT_BUTTON
           )
    print(var)


class Action():
    pass
    def __init__(self):
        pass

    def clickButton(self, target, delay):
        k.press_key(target)
        time.sleep(delay)
        k.release_key(target)


class PokeAction(Action):
    pass
    def __init__(self):
        super(PokeAction, self).__init__()

    def poke_random_fire(self,current):
        currentCount = current

        while currentCount < 6:
            time.sleep(2)
            self.clickButton('7', 0.2)

            res = self.poke_fire(False)
            print('已经使用了 %d 次，识别结果： %d' % (currentCount, res))
            if res == THREAD_STOP:
                return THREAD_STOP
            else:
                currentCount += res

        print('甜甜香气已经没了')
        return 0

    # 进入战斗
    def poke_fire(self, shiny):
        print('进入战斗')
        time.sleep(7)
        # 截图识别是否出现闪光

        imageScreen = ImageScreen()
        isShiny = imageScreen.check_shiny()
        print('是否遇到闪光 %d' % isShiny)
        if isShiny:
            print('遇到闪光精灵了！！！')
            return THREAD_STOP
        else:
            self.clickButton(A_BUTTON, 0.5)
            time.sleep(0.5)
            self.clickButton(A_BUTTON, 0.5)
            time.sleep(2)
            self.clickButton(A_BUTTON, 0.5)
            time.sleep(7)
            self.clickButton(A_BUTTON, 0.5)
            time.sleep(0.5)
            self.clickButton(A_BUTTON, 0.5)
            time.sleep(0.5)
            self.clickButton(A_BUTTON, 0.5)
            time.sleep(0.5)
            self.clickButton(A_BUTTON, 0.5)
            time.sleep(2)

        return 1


    # 进入pm 出来pm逻辑
    def poke_pm(self):
        print('准备恢复')
        time.sleep(2)
        self.clickButton('9',1)

        # 回血
        time.sleep(2)
        self.clickButton(A_BUTTON, 0.5)
        time.sleep(1)
        self.clickButton(A_BUTTON, 0.5)
        time.sleep(1)
        self.clickButton(A_BUTTON, 0.5)
        time.sleep(1)
        self.clickButton(A_BUTTON, 0.5)
        time.sleep(1)
        self.clickButton(A_BUTTON, 0.5)
        time.sleep(8)
        self.clickButton(A_BUTTON, 0.5)
        time.sleep(2)
        self.clickButton(DOWN_BUTTON, 3)
        time.sleep(2)
        return



class PokeApplication(object):
    def __init__(self, pokeAction):
        self.pokeAction = pokeAction

    def poke_gree_dragon(self):
        time.sleep(5)
        res = 0
        while res != THREAD_STOP:
            time.sleep(2)
            self.pokeAction.clickButton(DOWN_BUTTON, 0.5)
            self.pokeAction.poke_pm()
            self.poke_cave()
            res = self.pokeAction.poke_random_fire(res)
            print('执行完毕： %d' % res)

        if res == THREAD_STOP:
            print('遇到闪光精灵了！！！')

    # 飞翔到龙洞逻辑
    def poke_cave(self):
        print('进入洞穴')

        self.pokeAction.clickButton('2', 0.5)
        time.sleep(1)
        self.pokeAction.clickButton(DOWN_BUTTON, 0.1)
        self.pokeAction.clickButton(LEFT_BUTTON, 0.1)
        self.pokeAction.clickButton(A_BUTTON, 0.5)
        time.sleep(5)
        self.pokeAction.clickButton(UP_BUTTON, 2)




def __poke_main__():
    action = PokeAction()
    poke = PokeApplication(action)
    t1 = threading.Thread(target=poke.poke_gree_dragon())
    t1.start()

__poke_main__()
# poke_pm()
# poke_cave()
# poke_random_fire(5)
# poke_fire()


# prepare_poke()













