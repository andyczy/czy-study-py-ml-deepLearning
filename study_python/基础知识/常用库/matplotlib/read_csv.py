#encoding:UTF-8
# czy study Machine Learning and DeepLearning

# Matplotlib 是一个 Python 的 2D绘图库，它以各种硬拷贝格式和跨平台的交互式环境生成出版质量级别的图形。
# Seaborn属于Matplotlib的一个高级接口，为我们进行数据的可视化分析提供了极大的方便。 


import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('./study_python/data/matplotlib/percent-bachelors-degrees-women-usa.csv')
plt.plot(women_degrees['Year'], women_degrees['Biology'])
plt.show()

plt.plot(women_degrees['Year'], women_degrees['Biology'], c='blue', label='Women')
plt.plot(women_degrees['Year'], 100-women_degrees['Biology'], c='green', label='Men')
plt.legend(loc='upper right')
plt.title('Percentage of Biology Degrees Awarded By Gender')
plt.show()