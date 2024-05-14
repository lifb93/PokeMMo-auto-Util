import os
import threading

from src.app.DriftveilCityFrillishEncounter import DriftveilCityFrillishEncounter
from src.app.EmeraldBattleParkUpLevel import EmeraldBattleParkUpLevel
from src.app.EmeraldMagikarpEncounter import EmeraldMagikarpEncounter
from src.app.FiveIslandEncounter import FiveIslandEncounter
from src.app.JohtoBlackthornCityEncounter import JohtoBlackthornCityEncounter
from src.app.PokeEncounter import PokeEncounter
from src.app.PokePPSweetScentEncounter import PokePPSweetScentEncounter
from src.common import PokeConfig
from src.common.ImageScreen import ImageScreen
from src.common.PokeAction import PokeAction
from src.app.PokeGreeDragon import PokeGreeDragon

# https://www.lfd.uci.edu/~gohlke/pythonlibs/ 安装pyhook
# https://pypi.org/project/pywin32/#files
#  pyUserInput install   pyinstaller
# pyinstaller.exe -F .\main.py  打包

def __poke_main__():
    path = os.path.join(os.path.expanduser("~"), "Desktop")
    PokeConfig.IMAGE_URL = path + r"/poke_action.png"
    PokeConfig.SAVE_PATH = path
    print("init image url : %s " % PokeConfig.IMAGE_URL)

    # PokeConfig.TARGET_TIME_STOP = '2024-05-14 17:38'

    # pr = PreparePokeConfig()
    # pr.prepare_poke()
    mag = EmeraldMagikarpEncounter()
    frillish = DriftveilCityFrillishEncounter()
    emerald = EmeraldBattleParkUpLevel()
    five = FiveIslandEncounter()
    joh = JohtoBlackthornCityEncounter()
    poke = PokeEncounter()
    gree = PokeGreeDragon()
    t1 = threading.Thread(target=mag.action_loop(PokeConfig.DEFAULT_AUTO))
    t1.start()

__poke_main__()













