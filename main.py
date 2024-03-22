import threading
from src.common.PokeAction import PokeAction
from src.app.PokeGreeDragon import PokeGreeDragon

# https://www.lfd.uci.edu/~gohlke/pythonlibs/ 安装pyhook
# https://pypi.org/project/pywin32/#files
#  pyUserInput install   pyinstaller
# pyinstaller.exe -F .\main.py  打包

def __poke_main__():
    # pr = PreparePokeConfig()
    # pr.prepare_poke()
    action = PokeAction()
    poke = PokeGreeDragon(action)
    t1 = threading.Thread(target=poke.poke_gree_dragon())
    t1.start()

__poke_main__()













