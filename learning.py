from classes.my_hand import *
from classes.pretreatment import *
from classes.one_layer_net import *
import matplotlib.pylab as plt

learning_rate = 0.01
loop_count = 100
my_hand = MyHand()
pretreatment = Pretreatment()
one_layer_net = OneLayerNetwork(3, 2)
trainig_hands, trainig_results = my_hand.load_trainig_data()
loss_array = []

for loop in range(0, loop_count):
    tmp_total_loss = 0

    for i in range(0, len(trainig_hands)):
        trainig_hand = trainig_hands[i]
        trainig_result = trainig_results[i]

        input_data = pretreatment.get_list_pretreatments(trainig_hand)
        loss = one_layer_net.loss(input_data, trainig_result)
        tmp_total_loss += loss
        # 勾配を求める
        grads = one_layer_net.return_gradient(input_data, trainig_result)
        one_layer_net.params['W'] -= learning_rate * grads['W']
        one_layer_net.params['b'] -= learning_rate * grads['b']

    print(tmp_total_loss)
    loss_array.append(tmp_total_loss)

print(one_layer_net.params['W'])
print(one_layer_net.params['b'])
x = range(0, 100)
y = loss_array
plt.xlabel("x")
plt.ylabel("loss")
plt.plot(x, y)
plt.show()