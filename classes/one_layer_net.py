import numpy as np

class OneLayerNetwork:
    u"""
    配牌からあがりを予測するモデルです。
    """

    def __init__(self, input_size, output_size, weight_init_std=0.01):
        self.params = {}
        self.params['W'] = weight_init_std * np.random.randn(input_size, output_size)
        self.params['b'] = np.zeros(output_size)

    def predict(self, x):
        u"""
        予測値を返します。
        @input array
        @return array
        """
        W, b = self.params['W'], self.params['b']

        a = np.dot(x, W) + b
        y = self.softmax(a)

        return y

    def softmax(self, x):
        u"""
        正規化する関数です。
        今回は1次元のリストなので、簡易的に実装します。
        @input array
        @return array
        """
        # オーバーフロー対策
        x = x - np.max(x)
        return np.exp(x) / np.sum(np.exp(x))