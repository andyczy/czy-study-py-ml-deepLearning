# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:45:28 2018

@author: Administrator
"""
# 2017-12-20
# python 第三方库
# time 模块

import time

# 时间戳
print("当前时间戳为:",time.time())
# 时间元祖
print(time.localtime())
# 时间格式化
# %y 小写是两位数字的年份
print(time.strftime('%y', time.localtime()) + '年')
# %Y 大写是四位数字的年份
print(time.strftime('%Y', time.localtime()) + '年')
# %m 月
print(time.strftime('%m', time.localtime()) + '月')
# %d 日
print(time.strftime('%d', time.localtime()) + '日')
# %H 24进制的小时
print(time.strftime('%H', time.localtime()) + '小时')
# %I 12进制的小时
print(time.strftime('%I', time.localtime()) + '小时')
# %M 分
print(time.strftime('%M', time.localtime()) + '分')
# %S 秒
print(time.strftime('%S', time.localtime()) + '秒')
# %A 本地星期
print(time.strftime('%A', time.localtime()) + '星期')
# %a 本地简化星期
print(time.strftime('%a', time.localtime()) + '星期')

# 时间字符串转时间
print(time.strptime('2017-12-22 12:52:23', '%Y-%m-%d %H:%M:%S'))
 