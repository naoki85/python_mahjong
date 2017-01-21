import random
import csv

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

    def load_trainig_data(self):
        u"""
        CSVファイルから教師データを読み込み、データを返します。
        @return array
        [0]で教師データの配牌、[1]で結果を返します
        """
        with open('csv/training_data.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            hand = []
            results = []
            for row in reader:
                tmp_hand = []
                for tile in range(0, 12):
                    tmp_hand.append(row[tile])

                results.append([row[13], row[14]])
                hand.append(tmp_hand)

        return hand, results




