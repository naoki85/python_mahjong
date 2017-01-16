import random

class MyHand:
    u"""
    ゲームに必要な情報を定義するクラスです。
    """

    def __init__(self):
        # 牌の初期化
        # 萬子
        self.characters = [11, 12, 13, 14, 15, 16, 17, 18, 19]
        # 筒子
        self.circles = [21, 22, 23, 24, 25, 26, 27, 28, 29]
        # 索子
        self.bamboos = [31, 32, 33, 34, 35, 36, 37, 38, 39]
        # 字牌
        self.honours = [41, 42, 43, 44, 45, 46, 47]
        # 全ての牌
        self.tiles = (self.characters + self.circles + self.bamboos + self.honours)
        # 山
        self.wall = self.tiles * 4

    def set_my_hand(self):
        u"""
        配牌をセットします。
        @return array
        """
        my_hand = random.sample(self.wall, 13)
        my_hand.sort()
        return my_hand


# 出力値
# 上がれたか上がれないか
# y = [1, 0]

# np.array(X).shape = [13,]
# [3, ]
# np.array(W1).shape = [3, 2]
# np.array(b1).shape = [2,]
# np.array(W2).shape = [3, 2]
# np.array(b2).shape = [2,]
# np.array(y).shape = [2, ]