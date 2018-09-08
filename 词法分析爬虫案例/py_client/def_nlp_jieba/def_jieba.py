#encoding:UTF-8
# czy study nlp Learning 
import jieba
from def_commons import def_io






# 分词并转化list
def jiebaCut(path,textFile):
    # 词典格式和dict.txt 一样，一个词占一行；每一行分三部分：词语、词频（可省略）、词性（可省略）用空格隔开，顺序不可颠倒。
    jieba.load_userdict(path+"/config/jieba_userdict.txt")
    seg_list = jieba.cut(textFile,cut_all=False)
    lists =  "ღ".join(seg_list).split("ღ")
    # print("——》  开始分词采集逻辑  《——") 
    return lists

