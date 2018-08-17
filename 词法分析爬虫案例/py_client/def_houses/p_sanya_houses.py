#encoding:UTF-8
# chenzy python
from def_commons import def_beautifulSoup #应用模块 
from def_commons import def_io #应用模块 
from def_houses import def_matching #应用模块 
# BeautifulSoup : https://cuiqingcai.com/1319.html
# http://sanya.home898.com/ 爬取页面显示的三亚楼盘获取楼盘详情url地址
# http://www.home898.com/loupan/1748/ 爬取动态（http://www.home898.com/loupan/1748/dongtai/）
# http://www.home898.com/zixun/1800256213.html 爬取动态详情获取内容

# 爬取页面显示的三亚楼盘获取楼盘详情url地址
def getHouseUrl(sanyaUrl,sanya_loupan_clean_url,sanya_loupan_url):
    # 爬取页面显示的三亚楼盘获取楼盘详情url地址
    soup = def_beautifulSoup.getCrawlContentByUrl(sanyaUrl)
    content = soup.select('.img-list .img-outer a')
    # 生成文件存储
    # 三亚楼盘url写入文件
    for item in content:
        data = item.get("href")
        iou = def_io.defWritelines(data,sanya_loupan_url,'a') # 追加
        line = def_io.getReadCount(sanya_loupan_url)
    print("--##  文件行数：",line,"  ##--")
    iou.close()

    # 清洗的url文件
    readTxt = def_io.defReadlines(sanya_loupan_url)
    # 删除后面6行广告utl
    cleanContent =''.join(readTxt[:line-18])
    iouw = def_io.defWritelines(cleanContent,sanya_loupan_clean_url,'w')

    # 清空文件
    def_io.closeTruncate(sanya_loupan_url)
    iouw.close
