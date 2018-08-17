#encoding:UTF-8
# czy study python


# 你有一个字典或者实例的序列，然后你想根据某个特定的字段比如 date 来分组迭代访问?
rows = [
            {'address': '5412 N CLARK', 'date': '07/01/2012'},
            {'address': '5148 N CLARK', 'date': '07/04/2012'},
            {'address': '5800 E 58TH', 'date': '07/02/2012'},
            {'address': '2122 N CLARK', 'date': '07/03/2012'},
            {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
            {'address': '1060 W ADDISON', 'date': '07/02/2012'},
            {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
            {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
        ]
from operator import itemgetter
from itertools import groupby
# Sort by the desired field first
rows.sort(key=itemgetter('date'))
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)


# 你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列？
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
 

# 另外一个值得关注的过滤工具就是 itertools.compress() ，它以一个 iterable
# 对象和一个相对应的 Boolean 选择器序列作为输入参数。然后输出 iterable 对象中对
# 应选择器为 True 的元素。当你需要用另外一个相关联的序列来过滤某个序列的时候，
# 这个函数是非常有用的。比如，假如现在你有下面两列数据：
addresses = [
            '5412 N CLARK',
            '5148 N CLARK',
            '5800 E 58TH',
            '2122 N CLARK',
            '5645 N RAVENSWOOD',
            '1060 W ADDISON',
            '4801 N BROADWAY',
            '1039 W GRANVILLE',
        ]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

# 现在你想将那些对应 count 值大于 5 的地址全部输出，那么你可以这样做：
from itertools import compress
more5 = [n > 5 for n in counts]
print( list(compress(addresses, more5)))