# encoding:UTF-8
# czy study Machine Learning


#逆向最大匹配
class IMM(object):
    # 内置方法__init__方法
    # __init__方法的第一参数永远是self，表示创建的类实例本身
    def __init__(self, dic_path):
        # 创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
        self.dictionary = set()  
        self.maximum = 0
        # 读取词典
        # with open 是 Python内置的open()函数
        with open(dic_path, 'r', encoding='utf8') as f:
            for line in f:
                line = line.strip()  # 删除开头或是结尾的空格字符
                
                print("词典数据：",line)
                if not line:
                    continue
                self.dictionary.add(line)
                print("数据dictionary：", self.dictionary)

                if len(line) > self.maximum:
                    self.maximum = len(line)
                    print("数据maximum：", self.maximum)
                    print("数据行数line：", len(line))


    def cut(self, text):
        result = []
        index = len(text)

        while index > 0:
            word = None
            # start: 计数从 start 开始。默认是从 0 开始；
            # stop: 计数到 stop 结束，但不包括 stop；
            # step：步长，默认为1
            for size in range(self.maximum, 0, -1):
                if index - size < 0:
                    continue

                piece = text[(index - size):index]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index -= size
                    break
            if word is None:
                index -= 1
        return result[::-1]

def main():
    text = "南京市长江大桥"
    
    tokenizer = IMM('./study_ml/data/imm_dic.utf8')
    print(tokenizer.cut(text))

main()