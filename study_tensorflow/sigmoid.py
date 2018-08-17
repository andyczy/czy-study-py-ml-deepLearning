# encoding:UTF-8
# czy study Machine Learning
import os  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error   
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error  

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 定义sigmoid函数
def sigmoid(z):
    # Exp 函数 返回 e（自然对数的底）的幂次方。
    return 1 / (1 + np.exp(-z))

nums = np.arange(-5, 5, step=0.3)
fig = plt.figure(figsize=(12, 4))
ax = fig.add_subplot(111)
ax.plot(nums, sigmoid(nums), 'r')
plt.show()

