from src.common import PokeConfig
import time

from src.common.PokeAction import PokeAction


class PokeGreeDragon(PokeAction):
    def __init__(self):
        super(PokeGreeDragon, self).__init__()

    def action_des_and_init(self):
        self.poke_gree_dragon()

    def action_inf(self, res):
        time.sleep(2)
        self.clickButton(PokeConfig.DOWN_BUTTON, 0.5)
        self.poke_pm(3)
        self.poke_cave()
        return self.poke_sweet_scent_fire(res)

    def poke_gree_dragon(self):
        print("合众地区刷闪光绿龙")
        print("依赖功能：飞空，香甜气息，瞬间移动")
        print("pm: 战斗公园的pm")
        print("站位: 战斗公园的pm外面")
        toFire = input("是否进行战斗？（默认是战斗）[Y/N]:")
        if toFire != 'Y' and toFire != 'y':
            PokeConfig.POKE_FIRE = False
        print("5秒后开始，请切换到游戏界面")


    # 飞翔到龙洞逻辑
    def poke_cave(self):
        print('进入洞穴')

        self.clickButton('2', 0.5)
        time.sleep(1)
        self.clickButton(PokeConfig.DOWN_BUTTON, 0.1)
        self.clickButton(PokeConfig.LEFT_BUTTON, 0.1)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(5)
        self.clickButton(PokeConfig.UP_BUTTON, 2)

