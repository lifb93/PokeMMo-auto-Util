import threading
import time
import win32api
from pykeyboard import PyKeyboard
from pymouse import PyMouse
from pymouse import PyMouseEvent

m = PyMouse()
k = PyKeyboard()


def print_m(thread_name, delay):
    count = 0
    while(count < 5):
        time.sleep(delay)
        count = count + 1
        # print("hello %s %d" % (thread_name, count))

        k.tap_key(k.enter_key)

# 进入战斗
def poke_fire():


# 进入pm 出来pm逻辑
def poke_pm():



















t1 = threading.Thread(target= print_m("thread--1",3))
t1.start()


