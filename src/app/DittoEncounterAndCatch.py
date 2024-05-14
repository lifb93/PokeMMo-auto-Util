from src.common import PokeConfig
import time

from src.common.PokeAction import PokeAction


class DriftveilCityFrillishEncounter(PokeAction):
    def __init__(self):
        super(DriftveilCityFrillishEncounter, self).__init__()

    def action_des_and_init(self):
        print("丰源百变怪补抓")
        print("依赖功能：单车")
        print("pm: 百变怪的洞里")
        print("站位: 百变怪的洞里")
        toFire = input("是否进行战斗？（默认是战斗）[Y/N]:")
        if toFire != 'Y' and toFire != 'y':
            PokeConfig.POKE_FIRE = False
        print("5秒后开始，请切换到游戏界面")

    def action_inf(self, res):
        self.poke_pm(3, 8)
        self.to_cave()
        return self.poke_sweet_scent_fire(res)

    def to_cave(self):
        pass
        #todo: 去洞里抓百变怪