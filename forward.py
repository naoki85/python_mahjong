# モジュールの読み込み
import os
from bottle import route, get, post, run, template, request, static_file
from classes.my_hand import *
from classes.pretreatment import *
from classes.one_layer_net import *

@get('/index')
def index():
    return template('index')

@get('/show_result')
def show_result():
    tiles = request.query.getlist('tile')
    initial_my_hand = []
    for i in range(13):
        initial_my_hand.append(int(tiles[i]))

    # データの前処理
    pretreatment = Pretreatment()
    input_data = pretreatment.get_list_pretreatments(initial_my_hand)

    # 予測の返却
    one_layer_net = OneLayerNetwork(3, 2)
    one_layer_net.load_parameters_from_pickle()
    result = one_layer_net.predict(input_data)
    ret_value = int(result[0] * 100)

    return template('show_result', ret_value=ret_value)

@route('/<filename:path>')
def static(filename):
    print(os.getcwd())
    return static_file(filename, root="/Users/user/python_mahjong/static")

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)

