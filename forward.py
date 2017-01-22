from classes.my_hand import *
from classes.pretreatment import *
from classes.one_layer_net import *

my_hand = MyHand()
initial_my_hand = my_hand.set_my_hand()

pretreatment = Pretreatment()
input_data = pretreatment.get_list_pretreatments(initial_my_hand)
print(input_data)

one_layer_net = OneLayerNetwork(3, 2)
result = one_layer_net.predict(input_data)
print("結果")
print(result)
