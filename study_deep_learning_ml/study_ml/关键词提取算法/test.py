#encoding:UTF-8
# czy study Machine Learning 

from jieba.analyse import *

#  （TF-idf与TextRank）的关键词提取 
with open('./study_ml/data/keywordExtract_sample.txt','r', encoding='UTF-8') as f:
    data = f.read()


# TF-idf
for keyword, weight in extract_tags(data, withWeight=True):
    print('%s %s' % (keyword, weight))


# TextRank
for keyword, weight in textrank(data, withWeight=True):
    print('%s %s' % (keyword, weight))
