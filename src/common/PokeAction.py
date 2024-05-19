import datetime
import time

from src.common import PokeConfig
from src.common.Action import Action
from src.common.ImageScreen import ImageScreen
from src.common.PokeCount import PokeCount
from src.constants import Direction


class PokeAction(Action):
    pass

    def __init__(self):
        super(PokeAction, self).__init__()
        self.imageScreen = ImageScreen()
        self.pokeCount = PokeCount(PokeConfig.SAVE_PATH)

    def action_des_and_init(self):
        pass

    def action_inf(self, res):
        pass

    def action_loop(self, target):
        self.action_des_and_init()
        time.sleep(5)
        res = target
        while res != PokeConfig.THREAD_STOP:
            res = self.action_inf(res)
            print('执行完毕： %d' % res)
            if res != PokeConfig.THREAD_STOP:
                res = self.target_time_stop(PokeConfig.TARGET_TIME_STOP)

        if res == PokeConfig.THREAD_STOP:
            print('遇到闪光精灵了！！！')

    def target_time_stop(self, target):
        if target is None:
            return PokeConfig.DEFAULT_AUTO

        targetTime = datetime.datetime.strptime(target, "%Y-%m-%d %H:%M").timestamp()
        now = time.time()
        if now >= targetTime:
            print("达到预期时间 %s ", target)
            return PokeConfig.THREAD_STOP
        else:
            return PokeConfig.DEFAULT_AUTO


    # Horizontal 水平的
    # Vertical 垂直的
    def poke_random_scent_fire(self, direction):
        isFire = False
        sp = None
        while not isFire:
            count = 0
            while count < 4:
                if direction in Direction.Horizontal:
                    self.clickButton(PokeConfig.RIGHT_BUTTON, 0.5)
                    self.clickButton(PokeConfig.LEFT_BUTTON, 0.5)
                    self.clickButton(PokeConfig.RIGHT_BUTTON, 0.5)
                    self.clickButton(PokeConfig.LEFT_BUTTON, 0.5)
                else:
                    self.clickButton(PokeConfig.DOWN_BUTTON, 0.5)
                    self.clickButton(PokeConfig.UP_BUTTON, 0.5)
                    self.clickButton(PokeConfig.DOWN_BUTTON, 0.5)
                    self.clickButton(PokeConfig.UP_BUTTON, 0.5)
                count += 1
                # time.sleep(0.3)


            time.sleep(5)

            sp = self.imageScreen.check_default_list()
            poke = sp.poke
            if poke is not None:
                print('已经进入战斗，复位按键')
                isFire = True

                # 复位按键到技能一
                #time.sleep(5)
                self.clickButton(PokeConfig.UP_BUTTON, 0.5)
                self.clickButton(PokeConfig.LEFT_BUTTON, 0.5)

        if sp is None:
            return PokeConfig.DEFAULT_AUTO

        # 是否是群怪
        if sp.size == 1:
            print("遇到单怪")
            if PokeConfig.PAY_DAY_PP_COUNT_CUR > 0 and PokeConfig.POKE_FIRE:
                PokeConfig.PAY_DAY_PP_COUNT_CUR -= 1
                return self.poke_fire_with_sp(sp, PokeConfig.FIRST_SKILL)
            #else:
                #return self.poke_fire_with_sp(sp, PokeConfig.ESCAPE_SKILL)
        else:
            print("遇到群怪")

        if PokeConfig.GROUP_SKILL_PP_COUNT_CUR > 0 and PokeConfig.POKE_FIRE:
            PokeConfig.GROUP_SKILL_PP_COUNT_CUR -= 1
            return self.poke_fire_with_sp(sp, PokeConfig.SECOND_SKILL)
        else:
            return self.poke_fire_with_sp(sp, PokeConfig.ESCAPE_SKILL)



    def poke_pp_sweet_scent_fire(self, eat_num):
        currentSentNum = PokeConfig.NUM_SEED_PP
        res = PokeConfig.DEFAULT_AUTO
        if currentSentNum == 0:
            res = PokeConfig.THREAD_STOP
        currentCount = 0
        while currentSentNum > 0:
            time.sleep(2)
            self.clickButton(PokeConfig.BTN_SWEET_SCENT, 0.2)

            sp = self.imageScreen.check_sweet_scent_talk()
            if sp.isTarget:
                if currentSentNum < eat_num:
                    print("pp 果子数量不够了！ 已经使用了 %d 次香甜气息" % currentCount)
                    return PokeConfig.THREAD_STOP
                self.clickButton(PokeConfig.A_BUTTON, 0.2)
                time.sleep(1)
                self.clickButton(PokeConfig.A_BUTTON, 0.2)
                time.sleep(1)

                currentSentNum -= eat_num
                print("吃果子， pp 果子还剩下 %d " % currentSentNum)
            else:
                if PokeConfig.POKE_FIRE:
                    res = self.poke_fire_with_sp(sp, PokeConfig.FIRST_SKILL)
                else:
                    res = self.poke_fire_with_sp(sp, PokeConfig.ESCAPE_SKILL)
                print('已经使用了 %d 次，识别结果： %d' % (currentCount, res))
                if res == PokeConfig.THREAD_STOP:
                    return PokeConfig.THREAD_STOP
                else:
                    currentCount += res

        return res


    def poke_sweet_scent_fire(self,current):
        currentCount = current - 1

        while currentCount < PokeConfig.TIMES_SWEET_SCENT:
            time.sleep(2)
            self.clickButton(PokeConfig.BTN_SWEET_SCENT, 0.2)

            res = self.poke_fire()
            print('已经使用了 %d 次，识别结果： %d' % (currentCount, res))
            if res == PokeConfig.THREAD_STOP:
                return PokeConfig.THREAD_STOP
            else:
                currentCount += res

        print('甜甜香气已经没了')
        return PokeConfig.DEFAULT_AUTO


    # 进入战斗
    def poke_fire(self):
        print('进入战斗')
        time.sleep(9)
        # 截图识别是否出现闪光

        sp = self.imageScreen.check_default_list()
        isShiny = sp.isTarget
        self.pokeCount.increament(sp.poke, sp.size)
        print('是否遇到闪光 %d , 出现的精灵是 %s' % (isShiny, sp.to_str()))
        if isShiny:
            print('遇到闪光精灵了！！！')
            return PokeConfig.THREAD_STOP
        else:
            if PokeConfig.POKE_FIRE:
                time.sleep(2)
                self.fire(PokeConfig.FIRST_SKILL)
            else:
                time.sleep(2)
                self.fire(PokeConfig.ESCAPE_SKILL)
            return PokeConfig.DEFAULT_AUTO

    def poke_fire_with_sp(self, sp, skillIndex):
        print('进入战斗')

        text = sp.text
        sp2 = self.imageScreen.check_default_list_with_text(text)
        isShiny = sp2.isTarget
        self.pokeCount.increament(sp2.poke, sp2.size)
        print('是否遇到闪光 %d , 出现的精灵是 %s' % (isShiny, sp2.to_str()))
        if isShiny:
            print('遇到闪光精灵了！！！')
            return PokeConfig.THREAD_STOP
        else:
            self.fire(skillIndex)
            time.sleep(1)
            return PokeConfig.DEFAULT_AUTO


    # 战斗处理
    def fire(self, skill):
        if skill == PokeConfig.FIRST_SKILL:
            print("使用 FIRST_SKILL")
            self.first_skill()
        elif skill == PokeConfig.SECOND_SKILL:
            print("使用 SECOND_SKILL")
            self.second_skill()
        elif skill == PokeConfig.THIRD_SKILL:
            print("使用 THIRD_SKILL")
            self.third_skill()
        elif skill == PokeConfig.FOURTH_SKILL:
            print("使用 FOURTH_SKILL")
            self.fourth_skill()
        elif skill == PokeConfig.ESCAPE_SKILL:
            print("使用 ESCAPE_SKILL")
            self.escape()
            return
        else:
            return

        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)

        if PokeConfig.LEARN_SKILL_SWITCH:
            forget = self.imageScreen.check_forget_skill()
            print("需要忘记技能： %s" % forget)
            if PokeConfig.LEARN_SKILL and forget:
                #睡眠线程 让用户去学习技能
                print("请忘记技能，10秒钟之后自动取消学习")
                time.sleep(15)

            if forget:
                print("取消学习技能中...")
                self.clickButton(PokeConfig.B_BUTTON, 0.5)
                time.sleep(0.5)
                self.clickButton(PokeConfig.B_BUTTON, 0.5)
                time.sleep(0.5)
                self.clickButton(PokeConfig.A_BUTTON, 0.5)
                time.sleep(0.5)
                self.clickButton(PokeConfig.A_BUTTON, 0.5)
                time.sleep(2)
        # else:
            # time.sleep(3)


    def poke_fire_target(self, skill, target):
        isTarget = self.imageScreen.check_target_poke(target)
        if isTarget:
            self.fire(skill)



    # 进入pm 出来pm逻辑
    def poke_pm(self, run, delay):
        print('准备恢复')
        time.sleep(2)
        self.clickButton(PokeConfig.BTN_MOVEMENT, 1)

        # 回血
        time.sleep(3)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(1)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(1)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(1)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(1)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(delay)
        self.clickButton(PokeConfig.B_BUTTON, 0.5)
        time.sleep(2)
        self.clickButton(PokeConfig.B_BUTTON, 0.5)
        time.sleep(2)
        self.clickButton(PokeConfig.B_BUTTON, 0.5)
        time.sleep(2)
        self.clickButton(PokeConfig.B_BUTTON, 0.5)
        time.sleep(2)
        self.clickButton(PokeConfig.DOWN_BUTTON, run)
        time.sleep(2)
        return


    # 冲浪
    def surfing(self):
        time.sleep(1)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(1.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(1)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(1)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)


    # 第一个技能
    def first_skill(self):
        time.sleep(2)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(8)

    # 第二个技能
    def second_skill(self):
        time.sleep(2)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.RIGHT_BUTTON, 0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(8)

    # 第三个技能
    def third_skill(self):
        time.sleep(2)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.DOWN_BUTTON, 0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(8)

    # 第四个技能
    def fourth_skill(self):
        time.sleep(2)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.RIGHT_BUTTON, 0.5)
        self.clickButton(PokeConfig.DOWN_BUTTON, 0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(8)

    def escape(self):
        self.clickButton(PokeConfig.RIGHT_BUTTON, 0.5)
        self.clickButton(PokeConfig.DOWN_BUTTON, 0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(4)



# p = PokeAction()
# p.poke_fire()
# print(p.target_time_stop(PokeConfig.TARGET_TIME_STOP))