from src.common import PokeConfig
import time

from src.common.PokeAction import PokeAction
from src.constants import Direction


class PokeEncounter(PokeAction):
    def __init__(self):
        super(PokeEncounter, self).__init__()

    def action_des_and_init(self):
        print("宝可梦闪光遭遇")
        print("依赖功能：单车")
        print("pm: 不恢复")
        print("站位: 遭遇怪的地方")
        isHorizontal = input("是否水平遇怪？[Y/N]:")
        self.horValue = Direction.Horizontal
        if isHorizontal != 'Y' and isHorizontal != 'y':
            self.horValue = Direction.Vertical

        PokeConfig.POKE_FIRE = False
        print("5秒后开始，请切换到游戏界面")

    def action_inf(self, res):
        return self.poke_random_scent_fire(self.horValue)



# c = PokeEncounter()
# c.action_loop(PokeConfig.DEFAULT_AUTO)