from src.common import PokeConfig
import time

from src.common.PokeAction import PokeAction
from src.constants import Direction


class PokePPSweetScentEncounter(PokeAction):

    eat_num = 3

    def __init__(self):
        super(PokePPSweetScentEncounter, self).__init__()

    def action_des_and_init(self):
        print("宝可梦pp闪光遭遇")
        print("依赖功能：pp果子（pp果子放入快捷键6）")
        print("pm: 不恢复")
        print("站位: 遭遇怪的地方")
        seed_num = input("请输入pp种子数量？:")
        PokeConfig.NUM_SEED_PP = int(seed_num)
        print("设置pp种子数量 %s " % PokeConfig.NUM_SEED_PP)

        toFire = input("是否进行战斗？（默认是战斗）[Y/N]:")
        if toFire != 'Y' and toFire != 'y':
            PokeConfig.POKE_FIRE = False

        # eat_num = input("每次吃pp种子数量？:")
        # self.eat_num = int(eat_num)
        # print("设置pp种子数量 %s " % self.eat_num)

        print("5秒后开始，请切换到游戏界面")

    def action_inf(self, res):
        return self.poke_pp_sweet_scent_fire(self.eat_num)


# c = PokeEncounter()
# c.action_loop(PokeConfig.DEFAULT_AUTO)