

from pykeyboard import PyKeyboard
from pymouse import PyMouse
import time

m = PyMouse()
k = PyKeyboard()
class Action():
    pass
    def __init__(self):
        pass

    def clickButton(self, target, delay):
        k.press_key(target)
        time.sleep(delay)
        k.release_key(target)
