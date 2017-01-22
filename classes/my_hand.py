import sys, os, random, csv

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
        # CSVを格納しているディレクトリのパス
        self.csv_dirpath = '/Users/user/python_mahjong/csv'

    def set_my_hand(self):
        u"""
        配牌をセットします。
        """
        my_hand = random.sample(self.wall, 13)
        return my_hand

    def load_trainig_data(self):
        u"""
        CSVファイルから教師データを読み込み、データを返します。
        """
        # CSVファイルのパスを追加
        #csv_dir = os.path.normpath(os.path.join(os.getcwd(), '../csv/training_data.csv'))
        csv_filepath = self.csv_dirpath + '/training_data.csv'

        with open(csv_filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            hands = []
            results = []
            for row in reader:
                tmp_hand = [int(tile) for tile in row]
                results.append([int(row[13]), int(row[14])])
                hands.append(tmp_hand)

        return hands, results
