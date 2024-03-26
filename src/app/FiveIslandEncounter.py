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
        if PokeConfig.PAY_DAY_PP_COUNT_CUR > 0 and PokeConfig.GROUP_SKILL_PP_COUNT_CUR > 0:
            sp = self.poke_random_scent_fire(self.horValue)

            if sp is None:
                return 1

            # 是否是群怪
            if sp.size > 1:
                print("遇到群怪")
                PokeConfig.GROUP_SKILL_PP_COUNT_CUR -= 1
                return self.poke_fire_with_sp(sp, 1)
            else:
                print("遇到怪")
                PokeConfig.PAY_DAY_PP_COUNT_CUR -= 1
                return self.poke_fire_with_sp(sp, 0)
        else:
            self.poke_pm()

            # 刷新pp
            PokeConfig.PAY_DAY_PP_COUNT_CUR = PokeConfig.PAY_DAY_PP_COUNT
            PokeConfig.GROUP_SKILL_PP_COUNT_CUR = PokeConfig.GROUP_SKILL_PP_COUNT
            print("刷新pp  %s %s" % (PokeConfig.PAY_DAY_PP_COUNT_CUR, PokeConfig.GROUP_SKILL_PP_COUNT_CUR))

            # 去草坪
            self.clickButton(PokeConfig.BICYCLE, 0.2)

            self.clickButton(PokeConfig.LEFT_BUTTON, 0.5)
            self.clickButton(PokeConfig.DOWN_BUTTON, 0.5)
            self.clickButton(PokeConfig.RIGHT_BUTTON, 0.5)
            self.clickButton(PokeConfig.UP_BUTTON, 0.5)

            self.clickButton(PokeConfig.RIGHT_BUTTON, 0.5)
            self.clickButton(PokeConfig.UP_BUTTON, 0.5)



    def fiveIslandEncounterDes(self):
        print("五岛遭遇神鸟和刷钱")
        print("依赖功能：单车，香甜气息，瞬间移动")
        print("请调整队伍第一只怪的技能： 聚宝功 放到技能一， 群体攻击 放到技能二")
        print("pm: 五岛pm")
        print("站位: 五岛pm外面")
        print("5秒后开始，请切换到游戏界面")
        isHorizontal = input("是否水平遇怪？[Y/N]:")
        self.horValue = 'Horizontal'
        if isHorizontal != 'Y' and isHorizontal != 'y':
            self.horValue = 'Vertical'

        payDayCount = input("聚宝功 技能的pp数量:")
        PokeConfig.PAY_DAY_PP_COUNT = payDayCount
        PokeConfig.PAY_DAY_PP_COUNT_CUR = 0
        print(PokeConfig.PAY_DAY_PP_COUNT)

        groupSkillCount = input("群体攻击 技能的pp数量:")
        PokeConfig.GROUP_SKILL_PP_COUNT = groupSkillCount
        PokeConfig.GROUP_SKILL_PP_COUNT_CUR = 0
        print(PokeConfig.GROUP_SKILL_PP_COUNT)





