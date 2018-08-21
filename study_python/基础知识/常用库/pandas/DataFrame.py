#encoding:UTF-8
# czy study Machine Learning and DeepLearning

# 数据帧(DataFrame)是二维数据结构，即数据以行和列的表格方式排列
# 数据帧(DataFrame)的功能特点：
    # 潜在的列是不同的类型
    # 大小可变
    # 标记轴(行和列)
    # 可以对行和列执行算术运算
import pandas as pd

df = pd.DataFrame()
print ("创建一个空的DataFrame:")
print (df)
print ()

data = [1,2,3,4,5]
df = pd.DataFrame(data)
print ("从列表创建DataFrame:")
print (df)
print ()

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print ("从列表创建DataFrame:")
print (df)
print ()

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print ("从ndarrays/Lists的字典来创建DataFrame:")
print (df)
print ()


df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print ("从ndarrays/Lists的字典来创建DataFrame:")
print (df)
print ()

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print ("从列表创建数据帧DataFrame:")
print (df)
print ()

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
print ("使用append()函数将新行添加到DataFrame:")
print (df)
print ()