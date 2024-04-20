import time

from src.common import PokeConfig

from src.common.PokeAction import PokeAction


class EmeraldMagikarpEncounter(PokeAction):
    def __init__(self):
        super(EmeraldMagikarpEncounter, self).__init__()

    def action_des_and_init(self):
        pass
        self.emeraldBattleParkUpLevel()

    def action_inf(self, res):
        self.poke_pm(1.5, 2)

        self.clickButton(PokeConfig.BTN_BICYCLE, 0.2)
        self.clickButton(PokeConfig.DOWN_BUTTON, 2)
        self.surfing()

        time.sleep(3)

        return self.poke_sweet_scent_fire(res)


    def emeraldBattleParkUpLevel(self):
        print("丰源琉璃市刷鲤鱼王")
        print("依赖功能：冲浪，香甜气息，瞬间移动")
        print("pm: 琉璃市的pm")
        print("站位: 琉璃市的pm外面")
        toFire = input("是否进行战斗？（默认是战斗）[Y/N]:")
        if toFire != 'Y' and toFire != 'y':
            PokeConfig.POKE_FIRE = False
        print("5秒后开始，请切换到游戏界面")

