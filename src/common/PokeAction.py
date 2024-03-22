
import time

from src.common import PokeConfig
from src.common.Action import Action
from src.common.ImageScreen import ImageScreen


class PokeAction(Action):
    pass
    def __init__(self):
        super(PokeAction, self).__init__()

    def poke_random_fire(self,current):
        currentCount = current

        while currentCount < 6:
            time.sleep(2)
            self.clickButton('7', 0.2)

            res = self.poke_fire(False)
            print('已经使用了 %d 次，识别结果： %d' % (currentCount, res))
            if res == PokeConfig.THREAD_STOP:
                return PokeConfig.THREAD_STOP
            else:
                currentCount += res

        print('甜甜香气已经没了')
        return 0

    # 进入战斗
    def poke_fire(self, shiny):
        print('进入战斗')
        time.sleep(7)
        # 截图识别是否出现闪光

        imageScreen = ImageScreen()
        isShiny = imageScreen.check_shiny()
        print('是否遇到闪光 %d' % isShiny)
        if isShiny:
            print('遇到闪光精灵了！！！')
            return PokeConfig.THREAD_STOP
        else:
            self.clickButton(PokeConfig.A_BUTTON, 0.5)
            time.sleep(0.5)
            self.clickButton(PokeConfig.A_BUTTON, 0.5)
            time.sleep(2)
            self.clickButton(PokeConfig.A_BUTTON, 0.5)
            time.sleep(7)
            self.clickButton(PokeConfig.A_BUTTON, 0.5)
            time.sleep(0.5)
            self.clickButton(PokeConfig.A_BUTTON, 0.5)
            time.sleep(0.5)
            self.clickButton(PokeConfig.A_BUTTON, 0.5)
            time.sleep(0.5)
            self.clickButton(PokeConfig.A_BUTTON, 0.5)
            time.sleep(2)

        return 1


    # 进入pm 出来pm逻辑
    def poke_pm(self):
        print('准备恢复')
        time.sleep(2)
        self.clickButton('9',1)

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
