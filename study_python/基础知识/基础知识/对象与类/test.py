#encoding:UTF-8
# chenzy python
# from unittest.mock import patch


# @patch('example.func')
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # 你想通过 format() 函数和字符串方法使得一个对象能支持自定义的格式化。
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3, 4)
print(p)














