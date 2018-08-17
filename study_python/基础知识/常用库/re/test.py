#encoding:UTF-8
# chenzy python
import re

# 正则表达式
strs = "天悦湖畔位于吉阳区凤凰路与迎宾路交汇处，爬虫项目占地面积约42281平方米，建筑面积约149547平方米，小区园林设计典雅精致，爬虫由巴厘岛团队操刀一步一景，营造绿色和谐生态社区，达到“人在园中、园在花中、花在家中”的境界,爬66虫三亚一中。"

regex = "爬虫."
# regex = "^爬虫."
# re.search 扫描整个字符串并返回第一个成功的匹配。
p_str = strs.split("，")
for  line in  p_str:
    if re.search(regex,line) is not None:
        print("匹配成功：",line)

# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配