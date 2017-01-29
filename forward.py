from classes.my_hand import *
from classes.pretreatment import *
from classes.one_layer_net import *
# 配牌をセット
my_hand = MyHand()
initial_my_hand = my_hand.input_my_hand()
# データの前処理
pretreatment = Pretreatment()
input_data = pretreatment.get_list_pretreatments(initial_my_hand)
print(input_data)
# 予測の返却
one_layer_net = OneLayerNetwork(3, 2)
one_layer_net.load_parameters_from_pickle()
result = one_layer_net.predict(input_data)
print("結果")
print(result)
