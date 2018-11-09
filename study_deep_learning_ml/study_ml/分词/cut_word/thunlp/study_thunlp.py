#encoding:UTF-8
# czy study Machine Learning 
import thulac	

# 代码示例1
thu1 = thulac.thulac()  #默认模式
text = thu1.cut("天悦湖畔位于吉阳区凤凰路与迎宾路交汇处，项目占地面积约42281平方米，建筑面积约149547平方米，小区园林设计典雅精致，由巴厘岛团队操刀一步一景，营造绿色和谐生态社区，达到“人在园中、园在花中、花在家中”的境界。三亚一中。", text=True)  #进行一句话分词

#  代码示例2
# thu1 = thulac.thulac(seg_only=True)  #只进行分词，不进行词性标注
# thu1.cut_f("input.txt", "output.txt")  #对input.txt文件内容进行分词，输出到output.txt


print(text)