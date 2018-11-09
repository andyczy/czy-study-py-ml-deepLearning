#encoding:UTF-8
# czy study Machine Learning 
import jieba.posseg as pseg
from jieba import analyse


# 关键词提取-tfidf
def keyword_extract(data, file_name):
   tfidf = analyse.extract_tags
   keywords = tfidf(data)
   return keywords


# 关键词提取（每句话进行提取）
def getKeywords(docpath, savepath):
   with open(docpath, 'r') as docf, open(savepath, 'w') as outf:
      for data in docf:
         data = data[:len(data)-1]
         keywords = keyword_extract(data, savepath)
         for word in keywords:
            outf.write(word + ' ')
         outf.write('\n')
