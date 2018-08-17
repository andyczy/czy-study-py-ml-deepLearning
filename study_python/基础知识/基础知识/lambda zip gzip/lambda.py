#encoding:UTF-8
# chenzy python

def fun(x,y):
    print(x+y)

fun(1,3)

fun2 = lambda x,y:x+y
p = fun2(2,5)
print(p)


# map
ls = list(map(fun,[1,2,4],[2,3,4]))
print(ls)


