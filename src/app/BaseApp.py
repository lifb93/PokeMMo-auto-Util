from src.common import PokeConfig
import time

from src.common.PokeAction import PokeAction


class BaseApp(PokeAction):
    def __init__(self):
        super(BaseApp, self).__init__()

    def action_des(self):
        pass

    def action_inf(self, res):
        pass

