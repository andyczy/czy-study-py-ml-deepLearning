#encoding:UTF-8
# czy study Machine Learning 
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 2、训练
def my_function():
    wiki_news = open('./study_ml/data/text_vector/reduce_zhiwiki.txt', 'r')
    # sg=0使用CBOW模型，sg=1是Skip-gram;
    # size表示词向量维度
    # window表示当前词和预测词可能的最大距离（越大所需要枚举的预测词越多，计算时间越长）
    # min_count最小出现的次数
    # workers线程数
    model = Word2Vec(LineSentence(wiki_news), sg=0,size=192, window=5, min_count=5, workers=9)
    model.save('./study_ml/data/text_vector/zhiwiki_news.word2vec')

if __name__ == '__main__':
    my_function()
