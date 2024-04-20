from src.common import PokeConfig
import time

from src.common.PokeAction import PokeAction


class EmeraldBattleParkUpLevel(PokeAction):
    def __init__(self):
        super(EmeraldBattleParkUpLevel, self).__init__()

    def action_des_and_init(self):
        pass
        self.emeraldBattleParkUpLevel()

    def action_inf(self, res):
        time.sleep(5)
        self.poke_pm(3, 2)
        self.clickButton(PokeConfig.BTN_BICYCLE, 0.2)

        self.clickButton(PokeConfig.DOWN_BUTTON, 1)
        self.clickButton(PokeConfig.RIGHT_BUTTON, 2)
        self.clickButton(PokeConfig.DOWN_BUTTON, 0.2)
        self.clickButton(PokeConfig.RIGHT_BUTTON, 1)
        self.clickButton(PokeConfig.DOWN_BUTTON, 0.2)

        self.surfing()
        return self.poke_sweet_scent_fire(res)


    def emeraldBattleParkUpLevel(self):
        print("丰源战斗公园地区刷水母")
        print("依赖功能：单车，冲浪，香甜气息，瞬间移动")
        print("pm: 战斗公园的pm")
        print("站位: 战斗公园的pm外面")
        print("5秒后开始，请切换到游戏界面")

