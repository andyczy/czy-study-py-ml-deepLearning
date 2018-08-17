import urllib.request
import http.cookiejar
import saveFile

# 方法使用了 build_opener 这个方法, 用来自定义 opener, 这种方法的好处是可以方便的拓展功能,
# 例如下面的代码就拓展了自动处理 Cookies 的功能.
# head: dict of header
def makeMyOpener(head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

oper = makeMyOpener()
uop = oper.open(' http://www.zhihu.com', timeout = 1000)
data = uop.read()
print(data.decode())
saveFile.saveFileFunction("F:","zhihu",data)