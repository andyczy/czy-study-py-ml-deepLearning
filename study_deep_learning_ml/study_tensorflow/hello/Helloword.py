# encoding:UTF-8
# czy study Machine Learning
import os  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error   
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error  
import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
ccc = tf.Session()
strh = ccc.run(hello)
# b'Hello, TensorFlow!'
print("常量：",strh)

a = tf.constant(10)
b = tf.constant(32)
# 加法
s = tf.add(a,b)
# 启动TensorFlow默认的图
sess = tf.Session()
s = sess.run(s)
print("两个数相加：",s)



# 矩阵
m1 = tf.constant([[2],[3]])
m2 = tf.constant([[3,3]])
ma = tf.matmul(m2,m1)
print("矩阵:",ma)

# 启动默认的图
mat = sess.run(ma)
print("矩阵:",mat)
# 关闭会话
sess.close()


# 这样就不用关闭session了
with tf.Session() as sess:
    m1 = tf.constant([[2],[3]])
    m2 = tf.constant([[3,3]])
    ma = tf.matmul(m2,m1)
    # 启动默认的图
    mat = sess.run(ma)
    print("矩阵:",mat) 

# 变量
v = tf.Variable([1,2])
# 常量
c = tf.constant([3,3])
# 减法
su = tf.subtract(v,c)
# 加法
ad = tf.add(v,c)
# 乘法
mul = tf.multiply(v,c)
# 变量初始化
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    # 启动默认的图
    print("加法:",sess.run(ad)) 
    print("减法:",sess.run(su)) 
    print("乘法:",sess.run(mul)) 


# 定义一个变量、初始化为零
state = tf.Variable(0,name="count")
# +1
new = tf.add(state,1)
# 赋值op
update = tf.assign(state,new)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    # 启动默认的图
    for i in range(5):
        sess.run(update)
        print("循环:",sess.run(state)) 
print("state.name:",state.name) 

# feed 用法
# 占位符：运行的时候才给它数据
input1 =  tf.placeholder(tf.float32)
input2 =  tf.placeholder(tf.float32)
# 乘法
fmul = tf.multiply(input1,input2)
with tf.Session() as sess:
    # feed的数据以字典的方式传入
    print("feed的数据以字典的方式传入:",sess.run(fmul,feed_dict={input1:[5.],input2:[6.]})) 
