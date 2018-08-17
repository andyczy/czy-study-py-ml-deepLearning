#encoding:UTF-8
# czy study python


import heapq


# 怎样从一个集合中获得最大或者最小的 N 个元素列表？
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2,100]
# heapq 模块有两个函数：nlargest() 和 nsmallest() 可以完美解决这个问题。
print(heapq.nlargest(3, nums)) # Prints [100, 42, 37]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

portfolio = [
            {'name': 'IBM', 'shares': 100, 'price': 91.1},
            {'name': 'AAPL', 'shares': 50, 'price': 543.22},
            {'name': 'FB', 'shares': 200, 'price': 21.09},
            {'name': 'HPQ', 'shares': 35, 'price': 31.75},
            {'name': 'YHOO', 'shares': 45, 'price': 16.35},
            {'name': 'ACME', 'shares': 75, 'price': 115.65}
        ]
# 两个函数都能接受一个关键字参数，用于更复杂的数据结构中
cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
# 上面代码在对每个元素进行对比的时候，会以 price 的值进行比较。
# [{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}]
# [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}]
print(cheap)  
print(expensive) 




