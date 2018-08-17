import random
from fake_useragent import UserAgent
import requests 
import time
import json
import urllib.request

def saveInfo(count,save,sleep,isLaowu,isWU):
    for i in range(count):
        if save==True:
            ua = UserAgent()
            url = "http://app.i-sanya.com/vote/ajax/detail/save"
            headers = {'User-Agent':ua.random+ua.random+ua.random}

        # if isLaowu==True: 
            reData = requests.post(url,data = { 'detailId':29}, headers=headers )
            reData = requests.post(url,data = { 'detailId':29}, headers=headers )
            reData = requests.post(url,data = { 'detailId':29}, headers=headers )
            reData = requests.post(url,data = { 'detailId':29}, headers=headers )
            reData = requests.post(url,data = { 'detailId':29}, headers=headers )
            print("牛顿刷新第：",i,json.loads(reData.text))

            headers = {'User-Agent':ua.random+ua.random+ua.random+ua.random}
            reData = requests.post(url,data = { 'detailId':12}, headers=headers )
            reData = requests.post(url,data = { 'detailId':12}, headers=headers )
            reData = requests.post(url,data = { 'detailId':12}, headers=headers )
            reData = requests.post(url,data = { 'detailId':12}, headers=headers )
            reData = requests.post(url,data = { 'detailId':12}, headers=headers )

            headers = {'User-Agent':ua.random+ua.random+ua.random+ua.random+ua.random}
            reData = requests.post(url,data = { 'detailId':16}, headers=headers )
            reData = requests.post(url,data = { 'detailId':16}, headers=headers )
            reData = requests.post(url,data = { 'detailId':16}, headers=headers )
            reData = requests.post(url,data = { 'detailId':16}, headers=headers )
            reData = requests.post(url,data = { 'detailId':16}, headers=headers )
            print("牛顿刷新第：",i,json.loads(reData.text))

            
            headers = {'User-Agent':ua.random+ua.random+ua.random+ua.random+ua.random}
            reData = requests.post(url,data = { 'detailId':12}, headers=headers )
            reData = requests.post(url,data = { 'detailId':12}, headers=headers )
            reData = requests.post(url,data = { 'detailId':12}, headers=headers )
            reData = requests.post(url,data = { 'detailId':12}, headers=headers )
            reData = requests.post(url,data = { 'detailId':12}, headers=headers )

            headers = {'User-Agent':ua.random+ua.random+ua.random+ua.random+ua.random+ua.random+ua.random}
            reData = requests.post(url,data = { 'detailId':16}, headers=headers )
            reData = requests.post(url,data = { 'detailId':16}, headers=headers )
            reData = requests.post(url,data = { 'detailId':16}, headers=headers )
            reData = requests.post(url,data = { 'detailId':16}, headers=headers )
            reData = requests.post(url,data = { 'detailId':16}, headers=headers )
            print("牛顿刷新第：",i,json.loads(reData.text))
        if isWU==True:
            urllib.request.urlopen("http://app.i-sanya.com/vote/page/detail?id=29",timeout = 30).read()
            urllib.request.urlopen("http://app.i-sanya.com/vote/page/detail?id=29",timeout = 30).read()
            urllib.request.urlopen("http://app.i-sanya.com/vote/page/detail?id=29",timeout = 12).read()
            urllib.request.urlopen("http://app.i-sanya.com/vote/page/detail?id=29",timeout = 12).read()

        if sleep==True:
            if  i != 0 and i%5 == 0:
                time.sleep(10)
            if  i != 0 and i%50 == 0:
                time.sleep(30)
            if i != 0 and i%100 == 0:
                time.sleep(60)

# 数量+是否投票+是否睡眠+29+12
saveInfo(1000,True,True,True,True)