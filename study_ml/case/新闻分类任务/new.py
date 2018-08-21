#encoding:UTF-8
# czy study Machine Learning 
import pandas as pd
import jieba
import jieba.analyse
import numpy
from gensim import corpora, models, similarities
import gensim
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer


from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib

# 数据源：http://www.sogou.com/labs/resource/ca.php
#####1  pandas 读写数据
df_news = pd.read_table('./study_ml/case/data/val.txt',names=['category','theme','URL','content'],encoding='utf-8')
df_news = df_news.dropna()
new_head = df_news.head()
new_shape = df_news.shape
# 数据
print(new_head)
# 数据结构
print(new_shape)

#####2  分词：使用结吧分词器
content = df_news.content.values.tolist()
print (content[1000])
# 分词清洗
content_S = []
for line in content:
    current_segment = jieba.lcut(line)
    if len(current_segment) > 1 and current_segment != '\r\n': #换行符
        content_S.append(current_segment)
print(content_S[1000])

#####3  pandas数据格式转换
df_content=pd.DataFrame({'content_S':content_S})
content_S_head = df_content.head()
print(content_S_head)

#####3  pandas加载停用词
stopwords=pd.read_csv("./study_ml/case/data/stopwords.txt",index_col=False,sep="\t",quoting=3,names=['stopword'], encoding='utf-8')
stopwords = stopwords.head(20)
print(stopwords)

# 普通函数:停用词数据清洗
def drop_stopwords(contents,stopwords):
    contents_clean = []
    all_words = []
    for line in contents:
        line_clean = []
        for word in line:
            if word in stopwords:
                continue
            line_clean.append(word)
            all_words.append(str(word))
        contents_clean.append(line_clean)
    return contents_clean,all_words
    # print (contents_clean)

contents = df_content.content_S.values.tolist()    
stopwords = stopwords.stopword.values.tolist()
contents_clean,all_words = drop_stopwords(contents,stopwords)
# print(contents_clean,all_words)

# pandas 函数：停用词数据清洗
#df_content.content_S.isin(stopwords.stopword)
#df_content=df_content[~df_content.content_S.isin(stopwords.stopword)]
#df_content.head()

# 清洗后的数据
df_content=pd.DataFrame({'contents_clean':contents_clean})
print(df_content.head())

df_all_words=pd.DataFrame({'all_words':all_words})
print(df_all_words.head())

#####4  pandas 词频
words_count=df_all_words.groupby(by=['all_words'])['all_words'].agg({"count":numpy.size})
# 排序
words_count=words_count.reset_index().sort_values(by=["count"],ascending=False)
print(words_count.head())


#####5  词云展示（可无） 
# matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
# 引入词云字体
# wordcloud=WordCloud(font_path="./study_ml/case/data/simhei.ttf",background_color="white",max_font_size=80)
# word_frequence = {x[0]:x[1] for x in words_count.head(100).values}
# wordcloud=wordcloud.fit_words(word_frequence)
# plt.imshow(wordcloud)



#####6   TF-IDF ：提取关键词
index = 2400
print (df_news['content'][index])
content_S_str = "".join(content_S[index])  
print ("  ".join(jieba.analyse.extract_tags(content_S_str, topK=5, withWeight=False)))


#####7   LDA ：主题模型 (格式要求：list of list形式，分词好的的整个语料)
#做映射，相当于词袋
dictionary = corpora.Dictionary(contents_clean)
corpus = [dictionary.doc2bow(sentence) for sentence in contents_clean]
print (dictionary)
#类似Kmeans自己指定K值
lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=20) 
#一号分类结果
print (lda.print_topic(1, topn=5))
# for topic in lda.print_topics(num_topics=20, num_words=5):
#     print (topic[1])


df_train=pd.DataFrame({'contents_clean':contents_clean,'label':df_news['category']})
lda_tail = df_train.tail()
print (lda_tail)

#####8  基于贝叶斯算法分类  
df_train.label.unique()
# array(['汽车', '财经', '科技', '健康', '体育', '教育', '文化', '军事', '娱乐', '时尚'], dtype=object)
label_mapping = {"汽车": 1, "财经": 2, "科技": 3, "健康": 4, "体育":5, "教育": 6,"文化": 7,"军事": 8,"娱乐": 9,"时尚": 0}
df_train['label'] = df_train['label'].map(label_mapping)
print(df_train.head())



# 训练集、测试集
x_train, x_test, y_train, y_test = train_test_split(df_train['contents_clean'].values, df_train['label'].values, random_state=1)
#x_train = x_train.flatten()
print(x_train[0][1])

# list转str
words = []
for line_index in range(len(x_train)):
    try:
        #x_train[line_index][word_index] = str(x_train[line_index][word_index])
        words.append(' '.join(x_train[line_index]))
    except:
        print (line_index,word_index)
print(words[0]) 
# 测试集
test_words = []
for line_index in range(len(x_test)):
    try:
        #x_train[line_index][word_index] = str(x_train[line_index][word_index])
        test_words.append(' '.join(x_test[line_index]))
    except:
         print (line_index,word_index)
test_words[0]


# 构造向量:预处理
vec = CountVectorizer(analyzer='word', max_features=4000,  lowercase = False)
vec.fit(words)
# 贝叶斯
classifier = MultinomialNB()
classifier.fit(vec.transform(words), y_train)
# 贝叶斯：测试集
score = classifier.score(vec.transform(test_words), y_test)
print("贝叶斯-测试集:",score)



# TfidfVectorizer
vectorizer = TfidfVectorizer(analyzer='word', max_features=4000,  lowercase = False)
vectorizer.fit(words)
# TfidfVectorizer 
classifier = MultinomialNB()
classifier.fit(vectorizer.transform(words), y_train)
# TfidfVectorizer：测试集
score = classifier.score(vectorizer.transform(test_words), y_test)
print("TfidfVectorizer-测试集:",score)

