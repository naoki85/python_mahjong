from my_hand import *
from pretreatment import *
from one_layer_net import *

my_hand = MyHand()
initial_my_hand = my_hand.set_my_hand()

pretreatment = Pretreatment()
number_of_chows = pretreatment.have_number_of_chows(initial_my_hand)
print(number_of_chows)
number_of_pairs, number_of_pungs = pretreatment.have_number_of_pairs_and_pungs(initial_my_hand)
print(number_of_pairs)
print(number_of_pungs)

input_data = [number_of_chows, number_of_pairs, number_of_pungs]
print(input_data)

one_layer_net = OneLayerNetwork(3, 2)
result = one_layer_net.predict(input_data)
print("結果")
print(result)
