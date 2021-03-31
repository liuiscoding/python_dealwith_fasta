# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/30 20:43
@Author  : lhd - l17354000520@163.com
@FileName: 将fasta格式文件序列输出为一行.py
@Software: PyCharm
'''

#第一种方法-------纯字典方法
'''
from Bio.Seq import Seq
def transform_format(file):
    f = open("./data/new_gene.fnn", "w")
    dict_fa = {}
    for line in open(file, "r"):
        if line.startswith(">"):
            key = line.strip()
            dict_fa[key] = []
        else:
            dict_fa[key].append(line.strip())
    for key, value in dict_fa.items():
        f.write(key + '\n')
        f.write(''.join(value) + '\n')
    f.close()
transform_format('./data/gene.ffn')
'''

#第二种方法----使用biopython------python处理生物数据的利器
from Bio import SeqIO
from Bio.Seq import Seq
def transform_format(file):
    f = open('./data/new_gene.fnn', 'w')
    for record_seq in SeqIO.parse(file, 'fasta'):   #解析fasta文件
        f.write('>' + str(record_seq.id) + '\n')
        f.write(str(record_seq.seq) + '\n')
    f.close()
transform_format('./data/gene.ffn')