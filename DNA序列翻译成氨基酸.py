# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/30 19:52
@Author  : lhd - l17354000520@163.com
@FileName: DNA序列翻译成氨基酸.py
@Software: PyCharm
'''
from Bio import SeqIO
from Bio.Seq import Seq
def translate(file):
    f=open('./data/result2.fa','w')
    for record_seq in SeqIO.parse(file,'fasta'):
        f.write('>'+str(record_seq.id)+'\n')
        new_seq=(Seq(str(record_seq.seq))).translate(table=2,to_stop=True)  #table=2表示用NCBI标准的密码子表，to_stop表示遇到终止密码子停止翻译
        f.write(str(new_seq)+'\n')
    f.close()
translate('./data/gene.ffn')