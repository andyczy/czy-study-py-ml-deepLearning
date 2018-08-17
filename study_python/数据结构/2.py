#encoding:UTF-8
# czy study python

from collections import deque
 
# 队列
# 在队列两端插入或删除元素时间复杂度都是 O(1) ，而在列表的开头插入或删除元素的时间复杂度为 O(N) 。
q = deque(maxlen=4)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.appendleft(8)
# deque([8, 1, 2, 3], maxlen=4)
print(q)