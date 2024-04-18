from src.common import PokeConfig
import time

from src.common.PokeAction import PokeAction


class DriftveilCityFrillishEncounter(PokeAction):
    def __init__(self):
        super(DriftveilCityFrillishEncounter, self).__init__()

    def action_des_and_init(self):
        print("合众地区刷闪光轻飘飘")
        print("依赖功能：香甜气息，瞬间移动")
        print("pm: 帆巴市的pm")
        print("站位: 帆巴市的pm外面")
        toFire = input("是否进行战斗？（默认是战斗）[Y/N]:")
        if toFire != 'Y' and toFire != 'y':
            PokeConfig.POKE_FIRE = False
        print("5秒后开始，请切换到游戏界面")

    def action_inf(self, res):
        self.poke_pm(3)
        self.to_lake()
        return self.poke_sweet_scent_fire(res)

    def to_lake(self):
        self.clickButton(PokeConfig.RIGHT_BUTTON,1.5)
        self.clickButton(PokeConfig.UP_BUTTON,1)
        self.clickButton(PokeConfig.RIGHT_BUTTON,3)

        self.surfing()
        time.sleep(3)