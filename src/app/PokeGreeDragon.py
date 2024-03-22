from src.common import PokeConfig

import time
class PokeGreeDragon(object):
    def __init__(self, pokeAction):
        self.pokeAction = pokeAction

    def poke_gree_dragon(self):
        time.sleep(5)
        res = 0
        while res != PokeConfig.THREAD_STOP:
            time.sleep(2)
            self.pokeAction.clickButton(PokeConfig.DOWN_BUTTON, 0.5)
            self.pokeAction.poke_pm()
            self.poke_cave()
            res = self.pokeAction.poke_random_fire(res)
            print('执行完毕： %d' % res)

        if res == PokeConfig.THREAD_STOP:
            print('遇到闪光精灵了！！！')

    # 飞翔到龙洞逻辑
    def poke_cave(self):
        print('进入洞穴')

        self.pokeAction.clickButton('2', 0.5)
        time.sleep(1)
        self.pokeAction.clickButton(PokeConfig.DOWN_BUTTON, 0.1)
        self.pokeAction.clickButton(PokeConfig.LEFT_BUTTON, 0.1)
        self.pokeAction.clickButton(PokeConfig.A_BUTTON, 0.5)
        time.sleep(5)
        self.pokeAction.clickButton(PokeConfig.UP_BUTTON, 2)

