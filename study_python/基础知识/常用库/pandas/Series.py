#encoding:UTF-8
# czy study Machine Learning and DeepLearning

# Python Data Analysis Library 或 pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。pandas提供了大量能使我们快速便捷地处理数据的函数和方法。你很快就会发现，它是使Python成为强大而高效的数据分析环境的重要因素之一。
import pandas as pd
import numpy as np


s = pd.Series()
print("创建一个空的系列:", s)


data = np.array(['a','b','c','d'])
s = pd.Series(data)
print("从ndarray创建一个系列:",s)

data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print("在这里传递了索引值:",s)

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print("从字典创建一个系列:",s)
print("使用标签检索数据(索引):",s['a'])

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print("字典键用于构建索引:",s)


