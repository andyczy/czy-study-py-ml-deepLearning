# encoding:UTF-8
# czy study Machine Learning
import os  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error   
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error  
import tensorflow as tf
import numpy as np



# 使用numpy生成100个随机点
x_data = np.random.rand(100)
y_data = x_data*.01 + 0.2
# 构造一个线性模型
b = tf.Variable(0.)
k = tf.Variable(0.)
y = k*x_data + b

# 二次代价函数
loss  = tf.reduce_mean(tf.square(y_data-y))
# 定义一个梯度下降法来进行训练的优化器
optimizer = tf.train.GradientDescentOptimizer(0.2)
# 最小代价函数
train = optimizer.minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for step in range(201):
        sess.run(train)
        if step%20 == 0:
            print(step,sess.run([k,b]))





