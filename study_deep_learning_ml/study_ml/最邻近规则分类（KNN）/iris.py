#encoding:UTF-8
# czy study Machine Learning 

from sklearn import neighbors
from sklearn import datasets

knn = neighbors.KNeighborsClassifier()
# 加载数据（sklearn datasets已经封装）
iris = datasets.load_iris()
print(iris.data) # 数据集中的数据
print(iris.target) #  iris的种类
 

# 建立模型
knn.fit(iris.data,iris.target)
# 测试（如）
predictedLabel = knn.predict([[0.1, 0.2, 0.3, 0.4]])
print ("predictedLabel is :",predictedLabel)