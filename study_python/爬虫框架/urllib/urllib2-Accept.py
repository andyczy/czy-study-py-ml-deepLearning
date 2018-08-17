import urllib.request

url = 'http://www.baidu.com/'
# 伪装浏览器
# 如果能够看懂这段话的第一句就OK了, 别的可以以后再配合 Fiddler 慢慢研究. 
# 所以我们要做的就是在 Python 爬虫向百度发起请求的时候, 顺便在请求里面写上 User-Agent, 表明自己是浏览器君.
# 在 GET 的时候添加 header 有很多方法, 下面介绍两种方法.

# 扩展性差
req = urllib.request.Request(url, headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})
oper = urllib.request.urlopen(req)
data = oper.read()
print(data.decode())