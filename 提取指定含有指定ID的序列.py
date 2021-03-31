# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/30 19:51
@Author  : lhd - l17354000520@163.com
@FileName: 提取指定含有指定ID的序列.py
@Software: PyCharm
'''
from Bio import SeqIO
from Bio.Seq import Seq
def extract_seq(file1,file2):
    f=open('./data/result5.fa','w')
    list=[]
    seq_dict={}
    for line in open(file1,'r'):
        list.append(line.strip())
    for record in SeqIO.parse(file2, 'fasta'):
        new_id='>'+record.id
        seq_dict[str(new_id)] = str(record.seq)   #首先创建一个字典
    for id in seq_dict.keys():
        if id in list:
            f.write(id+'\n'+seq_dict[id]+'\n')
    f.close()
extract_seq('./data/id_list.txt','./data/gene.ffn')
