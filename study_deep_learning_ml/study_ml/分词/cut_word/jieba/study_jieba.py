#encoding:UTF-8
# czy study Machine Learning 
import jieba
import jieba.analyse

seg_list = jieba.cut("鲁能三亚湾现特推出看海美宅8号楼中庭楼王", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))

# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))



# s = "鲁能三亚湾现特推出看海美宅8号楼中庭楼王"
# for x, w in jieba.analyse.extract_tags(s, withWeight=True):
#     print('%s %s' % (x, w))

# print('-'*40)
# print(' TextRank')
# print('-'*40)

# for x, w in jieba.analyse.textrank(s, withWeight=True):
#     print('%s %s' % (x, w))