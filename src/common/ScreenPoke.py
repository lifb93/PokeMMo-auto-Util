

class ScreenPoke(object):

    def __init__(self):
        self.isTarget = False
        self.poke = ''
        self.size = 0
        self.text = []

    def __set_is_target__(self, isTarget):
        self.isTarget = isTarget

    def __set_poke__(self, poke):
        self.poke = poke

    def __set_size__(self, size):
        self.size = size

    def __set_text__(self, text):
        self.text = text

    def __str__(self):
        print('isTarget %s , '
              'poke %s ,'
              'size %d ,'
              % (self.isTarget,
                 self.poke,
                 self.size))