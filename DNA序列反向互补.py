# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/30 19:49
@Author  : lhd - l17354000520@163.com
@FileName: DNA序列反向互补.py
@Software: PyCharm
'''
from Bio import SeqIO
from Bio.Seq import Seq
def rev_com(file):
    f = open('./data/result1.fa', 'w')
    for record_seq in SeqIO.parse(file, 'fasta'):   #解析fasta文件
        f.write('>' + str(record_seq.id) + '\n')
        new_seq=(Seq(str(record_seq.seq))).reverse_complement()
        f.write(str(new_seq) + '\n')
    f.close()
rev_com('./data/gene.ffn')
