from src.common import PokeConfig
import time

from src.common.PokeAction import PokeAction


class FiveIslandEncounter(PokeAction):
    def __init__(self):
        super(FiveIslandEncounter, self).__init__()

    def action_des_and_init(self):
        pass
        self.fiveIslandEncounterDes()

    def action_inf(self, res):


        return self.poke_sweet_scent_fire(res)


    def fiveIslandEncounterDes(self):
        print("五岛遭遇神鸟和刷钱")
        print("依赖功能：单车，香甜气息，瞬间移动")
        print("请调整队伍第一只怪的技能： 聚宝功 放到技能一， 群体攻击 放到技能二")
        print("pm: 五岛pm")
        print("站位: 五岛pm外面")
        print("5秒后开始，请切换到游戏界面")

