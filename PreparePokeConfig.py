import PokeConfig


class PreparePokeConfig(object):

    #     def __init__(self, up, down, left, right, a, b):
    #         self.A_BUTTON = a
    #         self.B_BUTTON = b
    #         self.UP_BUTTON = up
    #         self.DOWN_BUTTON = down
    #         self.LEFT_BUTTON = left
    #         self.RIGHT_BUTTON = right
    #
    #     def __str__(self):
    #         var = (self.A_BUTTON
    #                + " " + self.B_BUTTON
    #                + " " + self.UP_BUTTON
    #                + " " + self.DOWN_BUTTON
    #                + " " + self.LEFT_BUTTON
    #                + " " + self.RIGHT_BUTTON
    #                )
    #         print(var)

    def prepare_poke(self):
        print("请见游戏键盘设置(默认)：上 (w) , 下 (s) , 左 (a) , 右 (d) , a键 (j) , b键 (k)")
        response = input("是否使用默认配置？[Y/N]:")
        # config = PokeConfig(UP_BUTTON, DOWN_BUTTON, LEFT_BUTTON, RIGHT_BUTTON, A_BUTTON, B_BUTTON)
        if response != 'Y' and response != 'y':
            up = input("请输入 (上 键):")
            down = input("请输入 (下 键):")
            left = input("请输入 (左 键):")
            right = input("请输入 (右 键):")
            a = input("请输入 (a 键):")
            b = input("请输入 (b 键):")
            print('up : %s , down : %s , left: %s , right: %s ,a %s ,b %s' % (up, down, left, right, a, b))
            PokeConfig.A_BUTTON = a
            PokeConfig.B_BUTTON = b
            PokeConfig.UP_BUTTON = up
            PokeConfig.DOWN_BUTTON = down
            PokeConfig.LEFT_BUTTON = left
            PokeConfig.RIGHT_BUTTON = right

            # config = PokeConfig(up, down, left, right, a, b)

        # config.__str__()
        var = (PokeConfig.A_BUTTON
               + " " + PokeConfig.B_BUTTON
               + " " + PokeConfig.UP_BUTTON
               + " " + PokeConfig.DOWN_BUTTON
               + " " + PokeConfig.LEFT_BUTTON
               + " " + PokeConfig.RIGHT_BUTTON
               )
        print(var)