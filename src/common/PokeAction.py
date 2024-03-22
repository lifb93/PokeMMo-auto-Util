
import time

from src.common import PokeConfig
from src.common.Action import Action
from src.common.ImageScreen import ImageScreen


class PokeAction(Action):
    pass

    def __init__(self):
        super(PokeAction, self).__init__()
        self.imageScreen = ImageScreen()

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

        if res == PokeConfig.THREAD_STOP:
            print('遇到闪光精灵了！！！')


    # Horizontal 水平的
    # Vertical 垂直的
    def poke_random_scent_fire(self, direction):
        isFire = False
        while not isFire:
            if direction in 'Horizontal':
                self.clickButton(PokeConfig.LEFT_BUTTON, 3)
                self.clickButton(PokeConfig.RIGHT_BUTTON, 3)
            else:
                self.clickButton(PokeConfig.UP_BUTTON, 3)
                self.clickButton(PokeConfig.DOWN_BUTTON, 3)

                isFire = self.imageScreen.check_fire() is None
                if isFire:
                    print('进入战斗')

        return self.poke_fire()


    def poke_sweet_scent_fire(self,current):
        currentCount = current

        while currentCount < 6:
            time.sleep(2)
            self.clickButton(PokeConfig.SWEET_SCENT, 0.2)

            res = self.poke_fire()
            print('已经使用了 %d 次，识别结果： %d' % (currentCount, res))
            if res == PokeConfig.THREAD_STOP:
                return PokeConfig.THREAD_STOP
            else:
                currentCount += res

        print('甜甜香气已经没了')
        return 0


    # 进入战斗
    def poke_fire(self):
        print('进入战斗')
        time.sleep(7)
        # 截图识别是否出现闪光

        isShiny = self.imageScreen.check_default_list()
        print('是否遇到闪光 %d' % isShiny)
        if isShiny:
            print('遇到闪光精灵了！！！')
            return PokeConfig.THREAD_STOP
        else:
            time.sleep(5)
            self.fire(0)

        return 1


    # 战斗处理
    def fire(self, skill):
        if skill == 1:
            self.second_skill()
        elif skill == 2:
            self.third_skill()
        elif skill == 3:
            self.fourth_skill()
        else:
            self.first_skill()

        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(0.5)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(2)

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


    def poke_fire_target(self, skill, target):
        isTarget = self.imageScreen.check_target_poke(target)
        if isTarget:
            self.fire(skill)



    # 进入pm 出来pm逻辑
    def poke_pm(self):
        print('准备恢复')
        time.sleep(2)
        self.clickButton(PokeConfig.MOVEMENT,1)

        # 回血
        time.sleep(2)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(1)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(1)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(1)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(1)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(8)
        self.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(2)
        self.clickButton(PokeConfig.DOWN_BUTTON, 3)
        time.sleep(2)
        return


    # 冲浪
    def surfing(self):
        time.sleep(1)
        self.clickButton(PokeConfig.A_BUTTON, 0.2)
        time.sleep(1)
        self.clickButton(PokeConfig.A_BUTTON, 0.2)
        time.sleep(1)
        self.clickButton(PokeConfig.A_BUTTON, 0.2)


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




# p = PokeAction()
# p.poke_fire()