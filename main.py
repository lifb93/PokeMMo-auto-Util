import threading
import time
import win32api
from pykeyboard import PyKeyboard
from pymouse import PyMouse
from pymouse import PyMouseEvent
import imageScreen
from imageScreen import ImageScreen
import random

m = PyMouse()
k = PyKeyboard()

THREAD_STOP = 99

def poke_main(thread_name, delay):
    # count = 0
    # while(count < 5):
    #     time.sleep(delay)
    #     count = count + 1
    #     # print("hello %s %d" % (thread_name, count))
    #
    #     k.tap_key(k.enter_key)

    res = 0
    while res != THREAD_STOP:
        poke_pm()
        poke_cave()
        res = poke_random_fire(res)
        print('执行完毕： %d' % res)

    if res == THREAD_STOP:
        print('遇到闪光精灵了！！！')



def poke_random_fire(current):
    time.sleep(0.5)

    currentCount = current

    while currentCount < 6:
        rInt = random.randint(1, 10)
        n = 0
        while n < rInt:
            k.tap_key('2')
            n += 1

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
    time.sleep(4)
    # 截图识别是否出现闪光

    imageScreen = ImageScreen()
    isShiny = imageScreen.check_shiny()
    if isShiny:
        print('遇到闪光精灵了！！！')
        return THREAD_STOP
    else:
        time.sleep(1)
        k.tap_key('z')
        k.tap_key('z')

        time.sleep(2)
        k.tap_key('z')
        k.tap_key('z')
        return 1


# 进入pm 出来pm逻辑
def poke_pm():
    print('准备恢复')
    k.tap_key(k.down_key)
    time.sleep(1)
    k.tap_key(9)
    time.sleep(2)

    # 回血
    k.tap_key('z')
    time.sleep(1)
    k.tap_key('z')
    k.tap_key('z')
    time.sleep(1)
    k.tap_key('z')
    k.tap_key('z')
    k.tap_key('z')
    time.sleep(1)

    k.tap_key(k.down_key)
    k.tap_key(k.down_key)
    k.tap_key(k.down_key)
    k.tap_key(k.down_key)
    k.tap_key(k.down_key)
    k.tap_key(k.down_key)


# 飞翔到龙洞逻辑
def poke_cave():
    print('进入洞穴')
    time.sleep(1)
    k.tap_key(2)
    k.tap_key(k.down_key)
    k.tap_key(k.down_key)
    k.tap_key(k.left_key)
    k.tap_key('z')
    time.sleep(2)

    k.tap_key(k.up_key)
    k.tap_key(k.up_key)
    k.tap_key(k.up_key)



t1 = threading.Thread(target= poke_main("thread--1",3))
t1.start()


