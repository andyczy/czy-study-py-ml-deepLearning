#encoding:UTF-8
# czy study Machine Learning 
import sys
sys.path.append("../")

# 词典格式和 dict.txt 一样，一个词占一行；每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒。
# file_name 若为路径或二进制方式打开的文件，则文件必须为 UTF-8 编码。
import jieba
jieba.load_userdict("./study_algorithm_book/data/jieba_userdict.txt")


test_sent = ("鲁能三亚湾现特推出看海美宅8号楼中庭楼王")
words = jieba.cut(test_sent)
print('/'.join(words))

