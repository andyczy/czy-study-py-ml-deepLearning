import urllib.request
# 函数
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

# 执行
html = getHtml('http://python.org/')
print(html)


data={}
data['word']='Jecvay Notes'

url_values=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values

data=urllib.request.urlopen(full_url).read()
data=data.decode('UTF-8')
print(data)
