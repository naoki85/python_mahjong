import numpy as np
import pickle

class OneLayerNetwork:
    u"""
    配牌からあがりを予測するモデルです。
    """

    def __init__(self, input_size, output_size, weight_init_std=0.01):
        self.params = {}
        self.params['W'] = weight_init_std * np.random.randn(input_size, output_size)
        self.params['b'] = np.zeros(output_size)

    def load_parameters_from_pickle(self):
        u"""
        前回の重み、バイアスの学習結果をpickleファイルから取得する
        """
        pickle_filepath = '/Users/user/python_mahjong/pickle/output_results.pickle'
        with open(pickle_filepath, 'rb') as f:
            params = pickle.load(f)

        self.params['W'] = params['W']
        self.params['b'] = params['b']

    def predict(self, x):
        u"""
        予測値を返します。
        """
        W, b = self.params['W'], self.params['b']

        a = np.dot(x, W) + b
        y = self.softmax(a)

        return y

    def loss(self, x, t):
        u"""
        損失関数の値を返します。
        """
        y = self.predict(x)

        return self.cross_entropy_error(y, t)

    def return_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)
        
        grads = {}
        grads['W'] = self.numerical_gradient(loss_W, self.params['W'])
        grads['b'] = self.numerical_gradient(loss_W, self.params['b'])
        
        return grads

    def softmax(self, x):
        u"""
        正規化する関数です。
        今回は1次元のリストなので、簡易的に実装します。
        """
        # オーバーフロー対策
        x = x - np.max(x)
        return np.exp(x) / np.sum(np.exp(x))

    def cross_entropy_error(self, y, t):
        u"""
        損失関数には交差エントロピーを用います。
        """
        delta = 1e-7
        return -np.sum(t * np.log(y + delta))

    def numerical_gradient(self, f, x):
        h = 1e-4
        grad = np.zeros_like(x)
        
        it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
        while not it.finished:
            idx = it.multi_index
            tmp_val = x[idx]
            x[idx] = float(tmp_val) + h
            fxh1 = f(x)
            
            x[idx] = tmp_val - h 
            fxh2 = f(x)
            grad[idx] = (fxh1 - fxh2) / (2*h)
            
            x[idx] = tmp_val # 値を元に戻す
            it.iternext()
            
        return grad

    def load_parameters_from_pickle(self):
        u"""
        前回の重み、バイアスの学習結果をpickleファイルから取得する
        """
        pickle_filepath = '/Users/user/python_mahjong/pickle/output_results.pickle'
        with open(pickle_filepath, 'rb') as f:
            params = pickle.load(f)

        self.params['W'] = params['W']
        self.params['b'] = params['b']
