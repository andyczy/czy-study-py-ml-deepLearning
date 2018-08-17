#encoding:UTF-8
# czy study python


# 1、解压序列赋值给多个变量
# 任何的序列（或者是可迭代对象）可以通过一个简单的赋值语句解压并赋值给多个变量。唯一的前提就是变量的数量必须跟序列元素的数量是一样的。
# 如果变量个数和序列元素的个数不匹配，会产生一个异常。
# 实际上，这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。包括字符串，文件对象，迭代器和生成器

p = (4,5)
x,y = p
# 4,5
print(x,y)

data = [ 'ACME', 50, 91.1, (2018, 12, 21) ]
name, shares, price, date = data
# ACME (2012, 12, 21)
print(name,date)

name, shares, price, (year, mon, day) = data
# 2018 12 21
print(year, mon, day)


# 2、如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。那么怎样才能从这个可迭代对象中解压出 N 个元素出来？
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
# 值得注意的是上面解压出的 phone_numbers 变量永远都是列表类型
# ['773-555-1212', '847-555-1212']
print(phone_numbers)

# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
# nobody
print(uname)




