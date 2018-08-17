# 这个也是python彪悍的特性.

# 自省就是面向对象的语言所写的程序在运行时,所能知道对象的类型.简单一句就是运行时能够获得对象的类型.比如type(),dir(),getattr(),hasattr(),isinstance().

a = [1,2,3]
b = {'a':1,'b':2,'c':3}
c = True
print (type(a),type(b),type(c)) # <type 'list'> <type 'dict'> <type 'bool'>
print (isinstance(a,list))  # True