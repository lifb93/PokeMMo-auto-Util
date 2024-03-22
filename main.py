import threading
from PokeAction import PokeAction
from PreparePokeConfig import PreparePokeConfig
from app.PokeGreeDragon import PokeApplication

# https://www.lfd.uci.edu/~gohlke/pythonlibs/ 安装pyhook
# https://pypi.org/project/pywin32/#files
#  pyUserInput install   pyinstaller
# pyinstaller.exe -F .\main.py  打包

def __poke_main__():
    # pr = PreparePokeConfig()
    # pr.prepare_poke()
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













