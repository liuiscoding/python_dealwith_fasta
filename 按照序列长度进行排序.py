# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/30 19:50
@Author  : lhd - l17354000520@163.com
@FileName: 按照序列长度进行排序.py
@Software: PyCharm
'''
from Bio import  SeqIO
from Bio.Seq import Seq
def sort_fasta(file):
    seq_dict = {}
    f = open('./data/result4.fa', 'w')
    for record in SeqIO.parse(file, 'fasta'):
        seq_dict[record.id] = str(record.seq)
    seq_sort = sorted(seq_dict.items(), key=lambda i: len(i[1]), reverse=False)  # len(i[1])表示是按照值排序  0表示按照键排序
    # print(seq_sort)
    for line in seq_sort:
        for list in line:
            f.write(list + '\n')
    f.close()
sort_fasta('./data/gene.ffn')