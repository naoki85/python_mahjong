import collections as col

class Pretreatment:
    u"""
    手配の条件を整理するクラスです。
    そのままノードとして考えています。
    """

    def get_list_pretreatments(self, my_hand):
        my_hand.sort()
        number_of_chows = self.have_number_of_chows(my_hand)
        number_of_pairs, number_of_pungs = self.have_number_of_pairs_and_pungs(my_hand)

        return [number_of_chows, number_of_pairs, number_of_pungs]

    def have_number_of_chows(self, my_hand):
        u"""
        順子の数を数えます
        @input my_hand 手牌
        @return integer
        """
        # Pythonではリストの代入は参照渡しなので、新しくオブジェクトを作成
        tmp_my_hand = list(my_hand)
        number_of_chows = 0
        for i in range(0, len(my_hand)):
            # 字牌、8, 9の数牌の場合はcontinueする
            if my_hand[i] > 40 or my_hand[i] % 10 > 7:
                continue

            if my_hand[i] + 1 in tmp_my_hand and my_hand[i] + 2 in tmp_my_hand:
                tmp_my_hand.remove(my_hand[i] + 1)
                tmp_my_hand.remove(my_hand[i] + 2)
                number_of_chows = number_of_chows + 1

        return number_of_chows

    def have_number_of_pairs_and_pungs(self, my_hand):
        u"""
        対子と暗刻の数を数えます。
        @input my_hand 手牌
        @return integer
        [0]で対子の数、[1]で暗刻の数を返します。
        """
        number_of_pairs = 0
        number_of_pungs = 0
        overlap_counter = col.Counter(my_hand).most_common()
        for num, cnt in overlap_counter:
            if cnt == 3:
                number_of_pungs += 1
            elif cnt == 2 or cnt == 4:
                # TODO: 4つある場合も対子とみなしていますが、要検討です。
                number_of_pairs += 1

        return number_of_pairs, number_of_pungs
