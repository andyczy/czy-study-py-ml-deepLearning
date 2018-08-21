#encoding:UTF-8
# czy study Machine Learning and DeepLearning

# Matplotlib 是一个 Python 的 2D绘图库，它以各种硬拷贝格式和跨平台的交互式环境生成出版质量级别的图形。
# Seaborn属于Matplotlib的一个高级接口，为我们进行数据的可视化分析提供了极大的方便。 
import matplotlib.pyplot as plt
from pylab import *


x = linspace(0, 5, 10)
y = x ** 2

fig, ax = plt.subplots()

ax.plot(x, x**2, label="y = x**2")
ax.plot(x, x**3, label="y = x**3")
ax.legend(loc=2); # upper left corner
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title');

plt.show()