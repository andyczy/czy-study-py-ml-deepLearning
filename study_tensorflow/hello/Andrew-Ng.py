# encoding:UTF-8
# czy study Machine Learning
import os  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error   
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error  

import numpy as np
import tensorflow as tf


# 定义参数w，在TensorFlow中，你要用tf.Variable()来定义参数
w = tf.Variable(0,dtype = tf.float32)

# 定义损失函数：
cost = w**2-10*w+25  # tensorflow 也能识别
# cost = tf.add(tf.add(w**2,tf.multiply(- 10.,w)),25)
# 定义损失函数：(让我们用0.01的学习率，目标是最小化损失)
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

# 开启了一个TensorFlow session。
session = tf.Session()

# 用来初始化全局变量。
init = tf.global_variables_initializer()
session.run(init)

# 定义train为学习算法，它用梯度下降法优化器使损失函数最小化，但实际上我们还没有运行学习算法，所以session.run(w)评估了w等于0
print(session.run(w))

# 运行了梯度下降的1000次迭代，最后w变成了4.99999(4.9999886)，记不记得我们说〖(w-5)〗^2最小化，因此w的最优值是5，这个结果已经很接近了
for _ in range(10000):
    session.run(train)
print(session.run(w))





