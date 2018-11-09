#encoding:UTF-8
# czy study Machine Learning 
from gensim.corpora import WikiCorpus
from wiki_zh_converter import langconv
import jieba



# 1、维基百科语料下载和处理（繁体字转换和分词）
def my_function():
    space = ' '
    i = 0
    l = []
    zhwiki_name = './study_ml/data/text_vector/zhwiki-latest-pages-articles.xml.bz2'
    f = open('./study_ml/data/text_vector/reduce_zhiwiki.txt', 'w')
    # 维基百科语料将xml的wiki数据转换为text格式
    wiki = WikiCorpus(zhwiki_name, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        for temp_sentence in text:
            # 繁体字转换
            temp_sentence = langconv.Converter('zh-hans').convert(temp_sentence)
            # 分词
            seg_list = list(jieba.cut(temp_sentence))
            for temp_term in seg_list:
                l.append(temp_term)
        f.write(space.join(l) + '\n')
        l = []
        i = i + 1

        if (i %200 == 0):
            print('Saved ' + str(i) + ' articles')
    f.close()

# 主函数
if __name__ == '__main__':
    my_function()
