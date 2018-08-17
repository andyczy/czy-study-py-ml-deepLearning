#encoding:UTF-8
# chenzy python
import requests 
from bs4 import BeautifulSoup
 
# 采集模块 BeautifulSoup 使用方法: https://cuiqingcai.com/1319.html
def getCrawlContentByUrl(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    return soup

 
print(getCrawlContentByUrl("http://www.home898.com/zixun/1800131404.html"))

 