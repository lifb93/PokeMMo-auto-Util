import threading

from src.app.EmeraldBattleParkUpLevel import EmeraldBattleParkUpLevel
from src.app.FiveIslandEncounter import FiveIslandEncounter
from src.app.JohtoBlackthornCityEncounter import JohtoBlackthornCityEncounter
from src.common import PokeConfig
from src.common.PokeAction import PokeAction
from src.app.PokeGreeDragon import PokeGreeDragon

# https://www.lfd.uci.edu/~gohlke/pythonlibs/ 安装pyhook
# https://pypi.org/project/pywin32/#files
#  pyUserInput install   pyinstaller
# pyinstaller.exe -F .\main.py  打包

def __poke_main__():
    # pr = PreparePokeConfig()
    # pr.prepare_poke()
    poke = PokeGreeDragon()
    five = FiveIslandEncounter()
    poke2 = EmeraldBattleParkUpLevel()
    joh = JohtoBlackthornCityEncounter()
    t1 = threading.Thread(target=five.action_loop(PokeConfig.DEFAULT_AUTO))
    t1.start()

__poke_main__()













