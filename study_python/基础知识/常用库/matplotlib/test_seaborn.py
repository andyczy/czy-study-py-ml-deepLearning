#encoding:UTF-8
# czy study Machine Learning and DeepLearning

# Matplotlib 是一个 Python 的 2D绘图库，它以各种硬拷贝格式和跨平台的交互式环境生成出版质量级别的图形。
# Seaborn属于Matplotlib的一个高级接口，为我们进行数据的可视化分析提供了极大的方便。 

import numpy as np  
import seaborn as sns  
import matplotlib.pyplot as plt  


sns.set( palette="muted", color_codes=True)  
rs = np.random.RandomState(10)  
d = rs.normal(size=100)  
f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)  
sns.distplot(d, kde=False, color="b", ax=axes[0, 0])  
sns.distplot(d, hist=False, rug=True, color="r", ax=axes[0, 1])  
sns.distplot(d, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])  
sns.distplot(d, color="m", ax=axes[1, 1])  
plt.show()  


