#encoding:UTF-8
# chenzy python
# from def_commons import def_io #应用模块 
import os
import re
# 是否包含违规信息函数
# 关键字(keyWordList)格式：['最', '最佳', '最具', '最爱', '最赚']
# 文本(inputText)格式："三亚天悦湖畔,更多楼盘销售信息等"
def getMatchingText(keyWordList,inputText):
    varList = []
    # varCountList = []
    keyWordList = [x for x in keyWordList if x != '']
    for keyWord in list(set(keyWordList)):
        result = keyWord in inputText
        count = inputText.count(keyWord)
        if result:
            varList.append(keyWord)  #词
            # varCountList.append(count)  #次数
    return varList


#########################  test  ##############################
# keyWordList =['三亚','三','czy','v信','总价240-350万元/套']
# inputText="天悦湖畔均价：38000㎡[三亚- 三亚市区] 吉阳区海螺一路二巷对面售楼处：400-664-8866 转 7088楼盘主页详细资料楼栋户型价格分析楼盘相册楼盘动态楼盘问答三亚天悦湖畔1#、2#、3#楼房源在售，一次性付款97折。户型有建面约59㎡、62㎡、64㎡、67㎡一房，86㎡的两房，总价240-350万元/套。建面59㎡户型仅剩3套顶层房源。如想了解更多楼盘销售信息，欢迎来电咨询！天悦湖畔鸟瞰图天悦湖畔位于吉阳区凤凰路与迎宾路交汇处，项目占地面积约42281平方米，建筑面积约149547平方米小区园林设计典雅精致，由巴厘岛团队操刀一步一景，营造绿色和谐生态社区，达到“人在园中、园在花中、花在家中”的境界。天悦湖畔区位图天悦湖畔实景图"

# test
# print(getMatchingText(keyWordList,inputText))
