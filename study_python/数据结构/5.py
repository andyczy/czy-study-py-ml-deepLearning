#encoding:UTF-8
# czy study python
from collections import Counter
# 怎样找出一个序列中出现次数最多的元素呢？
# collections.Counter 类就是专门为这类问题而设计的，它甚至有一个有用的 most_common() 方法直接给了你答案。
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
    ]

word_counts = Counter(words)
# 出现频率最高的 3 个单词
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]
print( word_counts['not'])
# 1








