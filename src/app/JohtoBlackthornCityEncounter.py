from src.common import PokeConfig
import time

from src.common.PokeAction import PokeAction
from src.constants import Direction


class JohtoBlackthornCityEncounter(PokeAction):
    def __init__(self):
        super(JohtoBlackthornCityEncounter, self).__init__()

    def action_des_and_init(self):
        pass
        self.fiveIslandEncounterDes()

    def action_inf(self, res):
        if PokeConfig.PAY_DAY_PP_COUNT_CUR > 0 or PokeConfig.GROUP_SKILL_PP_COUNT_CUR > 0:
            return self.poke_random_scent_fire(self.horValue)
        elif PokeConfig.PAY_DAY_PP_COUNT_CUR == 0 and PokeConfig.GROUP_SKILL_PP_COUNT_CUR == 0:
            self.poke_pm(2.3)

            # 刷新pp
            PokeConfig.PAY_DAY_PP_COUNT_CUR = PokeConfig.PAY_DAY_PP_COUNT
            PokeConfig.GROUP_SKILL_PP_COUNT_CUR = PokeConfig.GROUP_SKILL_PP_COUNT
            print("刷新pp， 聚宝功：%s  群体技能： %s" % (PokeConfig.PAY_DAY_PP_COUNT_CUR, PokeConfig.GROUP_SKILL_PP_COUNT_CUR))

            # 去草坪
            self.clickButton(PokeConfig.BICYCLE, 0.2)

            self.clickButton(PokeConfig.LEFT_BUTTON, 1.13)
            self.clickButton(PokeConfig.DOWN_BUTTON, 3.5)


        return PokeConfig.DEFAULT_AUTO


    def fiveIslandEncounterDes(self):
        print("成都烟墨市遭遇神兽和刷钱")
        print("依赖功能：单车，香甜气息，瞬间移动")
        print("请调整队伍第一只怪的技能： 聚宝功 放到技能一， 群体攻击 放到技能二")
        print("pm: 烟墨市pm")
        print("站位: 烟墨市pm外面")
        isHorizontal = input("是否水平遇怪？[Y/N]:")
        self.horValue = Direction.Horizontal
        if isHorizontal != 'Y' and isHorizontal != 'y':
            self.horValue = Direction.Vertical

        toFire = input("是否进行战斗？（默认是战斗）[Y/N]:")
        if toFire != 'Y' and toFire != 'y':
            PokeConfig.POKE_FIRE = False
        else:
            payDayCount = input("聚宝功 技能的pp数量:")
            PokeConfig.PAY_DAY_PP_COUNT = int(payDayCount)
            PokeConfig.PAY_DAY_PP_COUNT_CUR = 0
            print(PokeConfig.PAY_DAY_PP_COUNT)

            groupSkillCount = input("群体攻击 技能的pp数量:")
            PokeConfig.GROUP_SKILL_PP_COUNT = int(groupSkillCount)
            PokeConfig.GROUP_SKILL_PP_COUNT_CUR = 0
            print(PokeConfig.GROUP_SKILL_PP_COUNT)
        print("5秒后开始，请切换到游戏界面")



#c = JohtoBlackthornCityEncounter()
#c.action_inf(1)






















