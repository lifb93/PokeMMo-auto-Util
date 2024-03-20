import threading
import time
from pykeyboard import PyKeyboard
from pymouse import PyMouse

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
#  pyUserInput install


def poke_gree_dragon():
    time.sleep(5)
    res = 0
    while res != THREAD_STOP:
        poke_pm()
        poke_cave()
        res = poke_random_fire(res)
        print('执行完毕： %d' % res)

    if res == THREAD_STOP:
        print('遇到闪光精灵了！！！')

def poke_random_fire(current):
    currentCount = current

    while currentCount < 6:
        time.sleep(2)
        clickButton('7', 0.2)

        res = poke_fire(False)
        print('已经使用了 %d 次，识别结果： %d' % (currentCount , res))
        if res == THREAD_STOP:
            return THREAD_STOP
        else:
            currentCount += res

    print('甜甜香气已经没了')
    return 0


# 进入战斗
def poke_fire(shiny):
    print('进入战斗')
    time.sleep(7)
    # 截图识别是否出现闪光

    # imageScreen = ImageScreen()
    # imageScreen.check_shiny()
    isShiny = False
    if isShiny:
        print('遇到闪光精灵了！！！')
        return THREAD_STOP
    else:
        clickButton(A_BUTTON, 0.5)
        time.sleep(0.5)
        clickButton(A_BUTTON, 0.5)
        time.sleep(5)
        clickButton(A_BUTTON, 0.5)
        time.sleep(0.5)
        clickButton(A_BUTTON, 0.5)
        time.sleep(0.5)
        clickButton(A_BUTTON, 0.5)
        time.sleep(1)

    return 1


# 进入pm 出来pm逻辑
def poke_pm():
    time.sleep(2)
    print('准备恢复')
    clickButton(DOWN_BUTTON, 0.5)
    time.sleep(2)
    clickButton('9',1)

    # 回血
    time.sleep(2)
    clickButton(A_BUTTON, 0.5)
    time.sleep(1)
    clickButton(A_BUTTON, 0.5)
    time.sleep(1)
    clickButton(A_BUTTON, 0.5)
    time.sleep(1)
    clickButton(A_BUTTON, 0.5)
    time.sleep(1)
    clickButton(A_BUTTON, 0.5)
    time.sleep(8)
    clickButton(A_BUTTON, 0.5)
    return


# 飞翔到龙洞逻辑
def poke_cave():
    print('进入洞穴')
    time.sleep(2)
    clickButton(DOWN_BUTTON, 3)
    time.sleep(2)


    clickButton('2', 0.5)
    time.sleep(1)
    clickButton(DOWN_BUTTON, 0.1)
    clickButton(LEFT_BUTTON, 0.1)
    clickButton(A_BUTTON, 0.5)
    time.sleep(5)
    clickButton(UP_BUTTON, 2)

def clickButton(target, delay):
    k.press_key(target)
    time.sleep(delay)
    k.release_key(target)

def __poke_main__():
    t1 = threading.Thread(target=poke_gree_dragon)
    t1.start()

__poke_main__()
# poke_pm()
# poke_cave()
# poke_random_fire(5)
# poke_fire()











