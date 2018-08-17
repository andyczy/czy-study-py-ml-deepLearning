#encoding:UTF-8
# chenzy python
import numpy as  np

# numpy资料：https://docs.scipy.org/doc/numpy/user/whatisnumpy.html
# NumPy是Python中科学计算的基础包。它是一个Python库，提供多维数组对象，各种派生对象（如掩码数组和矩阵），以及用于数组快速操作的各种例程，包括数学，逻辑，形状操作，排序，选择，I / O离散傅立叶变换，基本线性代数，基本统计运算，随机模拟等等。

# NumPy 中定义的最重要的对象是称为 ndarray 的 N 维数组类型。 
# 它描述相同类型的元素集合。 可以使用基于零的索引访问集合中的项目。

# ndarray 对象由计算机内存中的一维连续区域组成，带有将每个元素映射到内存块中某个位置的索引方案。 
# 内存块以按行(C 风格)或按列(FORTRAN 或 MatLab 风格)的方式保存元素。

data=np.array([2,5,6,8,3]) #构造一个简单的数组
print(data)

data1=np.array([[2,5,6,8,3],np.arange(5)])  #构建一个二维数组
print(data1)
# 我们也可以通过shape和dtype方法查看数组的维度和数据格式
print(data.shape)
print(data.dtype)
print(data1.shape)
print(data1.dtype)

# 三行五列
datareshape=np.arange(15).reshape(3,5)
print("NumPy 也提供了reshape函数来调整数组大小:",datareshape)


a = np.array([[1,2,3],[4,5,6]])  
print("NumPy shape属性返回一个包含数组维度的元组:",a.shape)

x = np.array([1,2,3,4,5], dtype = np.float32)  
print ("这一数组属性返回数组中每个元素的字节单位长度:",x.itemsize)


x = np.array([1,2,3,4,5])  
print("属性值：",x.flags)

a = np.asarray(x, dtype =  float)  
print("设置了 dtype :",a)


zeros = np.zeros((2, 3))
print("返回特定大小，以 0 填充的新数组:",zeros)

linspace = np.linspace(1., 4., 6)
print("linspace:",linspace)

print("indices:",np.indices((3,3)))

# numpy.frombuffer
# s =  'Hello World' 
# frombuffer = np.frombuffer(s, dtype =  'S1')  
# print (frombuffer)

list = range(5) 
it = iter(list)  
# 使用迭代器创建 ndarray 
x = np.fromiter(it, dtype =  float)  
print ("此函数从任何可迭代对象构建一个ndarray对象，返回一个新的一维数组。:",x)

x = np.arange(10,20,2)  
print("")


 






