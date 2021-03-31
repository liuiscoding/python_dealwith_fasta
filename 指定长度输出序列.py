# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/30 19:50
@Author  : lhd - l17354000520@163.com
@FileName: 指定长度输出序列.py
@Software: PyCharm
'''
'''
和上面的操作一样，将序列转换为字符串后取索引就行了
'''
#这里我取每个序列的前10个
from Bio import SeqIO
from Bio.Seq import Seq
def transform_format(file):
    f = open('./data/result3.fa', 'w')
    for record_seq in SeqIO.parse(file, 'fasta'):   #解析fasta文件
        f.write('>' + str(record_seq.id) + '\n')
        f.write((str(record_seq.seq))[0:10] + '\n')
    f.close()
transform_format('./data/gene.ffn')