#-*- coding:utf-8 -*-
from preprocess import Vector
import sys


def list2file(rs_list, fout):
    with open(fout, 'w') as f:
        for i, val in enumerate(rs_list):
            f.write("{}\n".format(val.encode("utf-8")))



if __name__ == "__main__":
    fin = sys.argv[1]
    fout = sys.argv[2]

    rs_list = []
    with open(fin, 'r') as f:
        for line in f:
            vec1 = Vector.str2vec(line.strip("\r\n"))
            rs_list.append(vec1)
    list2file(rs_list, fout)

