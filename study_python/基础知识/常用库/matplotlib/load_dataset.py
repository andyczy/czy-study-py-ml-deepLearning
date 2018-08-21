#encoding:UTF-8
# czy study Machine Learning and DeepLearning

# Matplotlib 是一个 Python 的 2D绘图库，它以各种硬拷贝格式和跨平台的交互式环境生成出版质量级别的图形。
# Seaborn属于Matplotlib的一个高级接口，为我们进行数据的可视化分析提供了极大的方便。 


import seaborn as sns
import matplotlib.pyplot as plt

# 加载数据
iris_data = sns.load_dataset('iris')
 
# 绘图
sns.lmplot(x='sepal_length', y='sepal_width', hue='species', data=iris_data)
plt.show()






