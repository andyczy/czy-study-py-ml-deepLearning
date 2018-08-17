#encoding:UTF-8
# czy study nlp Learning 
import jieba

# 分词并转化list
def jiebaCut(path,textFile):
    # 词典格式和dict.txt 一样，一个词占一行；每一行分三部分：词语、词频（可省略）、词性（可省略）用空格隔开，顺序不可颠倒。
    jieba.load_userdict(path)
    seg_list = jieba.cut(textFile, cut_all=False)
    lists =  "ღ".join(seg_list).split("ღ")
    # print("——》  开始分词采集逻辑  《——") 
    return lists

test = "带上您最爱的人一起享受海岛阳光！红苹果双语幼儿园等构建了完善的教育体系；农垦医院、解放军四二五医院、体育会展、金鸡岭公园和新行政等众多城市资源在这里汇集成三亚的近在咫尺去三亚高铁站和凤凰国际机场"
tests = jiebaCut("F:\codePython\czy-study-python\sanya_house_py\py_client\config\jieba_userdict.txt",test)
print(tests)
