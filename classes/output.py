import csv
import pickle

class Output:
    u"""
    出力層のクラスです。
    """
    def write_results_in_pickle(self, weight_parameter, bias_parameter):
        u"""
        結果をpickelに書き込みます。
        """
        pickle_filepath = '/Users/user/python_mahjong/pickle/output_results.pickle'
        results = {}
        results['W'] = weight_parameter
        results['b'] = bias_parameter

        with open(pickle_filepath, 'wb') as f:
            writer = pickle.dump(results, f)
            


