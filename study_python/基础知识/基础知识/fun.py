# 所有的变量都可以理解是内存中一个对象的“引用”，或者，也可以看似c中void*的感觉。
# 通过id来看引用a的内存地址可以比较理解：

# https://github.com/taizilongxu/interview_python#20-%E5%89%8D%E5%BA%8F%E4%B8%AD%E5%BA%8F%E6%B1%82%E5%90%8E%E5%BA%8F
a = []
def fun(a):
    print( "func_in",id(a) ) # func_in 53629256
    a.append(1)
print( "func_out",id(a))     # func_out 53629256
fun(a)
print (a) # [1]

# 这里记住的是类型是属于对象的，而不是变量。而对象有两种,“可更改”（mutable）与“不可更改”（immutable）对象。在python中，strings, tuples, 和numbers是不可更改的对象，而 list, dict, set 等则是可以修改的对象。(这就是这个问题的重点)