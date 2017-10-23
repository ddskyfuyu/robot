#-*- coding:utf-8 -*-
import argparse
import pdb

class FileObject(object):
    def __init__(self, fin):
        self.fin = fin
    
    def __iter__(self):
        with open(fin, 'r') as f:
            for line in f:
                for word in line.strip("\n").split():
                    yield word

class Vocab(object):

    def __init__(self, verbose, min_count, max_vocab=0):
        self._verbose = verbose
        self._max_vocab = max_vocab
        self._min_count = min_count

    def get_counts(self, fin):
        count_dict = {}
        file_obj = FileObject(fin)
        for word in file_obj:
            if word not in count_dict:
                count_dict.update({word:0})
                if self._verbose > 1 and len(count_dict) % 100000 == 0:
                    print("Process tokens number: {}".format(len(count_dict)))
            count_dict[word] += 1
        #sort count_dict based on count
        filter_list = [(key, count_dict[key]) for key in count_dict if count_dict[key] >= self._min_count]
        max_vocab = self._max_vocab
        if max_vocab and len(filter_list) > max_vocab:
            count_sorted_list = sorted(filter_list, key = lambda x:x[1], reverse = True)
        else:
            count_sorted_list = filter_list
            max_vocab = len(count_sorted_list)
        alph_sorted_list = sorted(count_sorted_list, key = lambda x:x[0], reverse = True)
        return alph_sorted_list[:max_vocab]
    
    def list2file(self, sorted_list, fout):
        with open(fout, 'w') as f:
            for i, val in enumerate(sorted_list):
                f.write("{}\t{}\n".format(val[0], val[1]))
                
        
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-verbose', help="set verbosity: 0, 1, 2(default)", type=int, required=True)
    parser.add_argument('-max_vocab', help="Upper bound on vocabulary size", type=int)
    parser.add_argument('-min_count', help="The minimum frequency words", type=int, required=True)
    parser.add_argument('-input', help='The input file path', type=str, required=True)
    parser.add_argument('-output', help='The output file path', type=str, required=True)

    args = parser.parse_args()
    verbose = args.verbose
    max_vocab = args.max_vocab
    min_count = args.min_count
    fin = args.input
    fout = args.output

    vocab = Vocab(verbose, min_count)
    words = vocab.get_counts(fin)
    vocab.list2file(words, fout)
