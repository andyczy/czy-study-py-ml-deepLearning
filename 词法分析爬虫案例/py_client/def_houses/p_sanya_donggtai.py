#encoding:UTF-8
# chenzy python
from def_commons import def_beautifulSoup   #应用模块 
from def_commons import def_io #应用模块 
import shutil 
import math
# BeautifulSoup : https://cuiqingcai.com/1319.html
# http://sanya.home898.com/ 爬取页面显示的三亚楼盘获取楼盘详情url地址
# http://www.home898.com/loupan/1748/ 爬取动态（http://www.home898.com/loupan/1748/dongtai/）
# http://www.home898.com/zixun/1800256213.html 爬取动态详情获取内容


# 爬取动态url
def getDontaiUrl(sanya_loupan_clean_url,sanya_dongtai_url,sanya_dongtai_clean_url):
    # 爬取动态 
    allUrl = def_io.defReadlines(sanya_loupan_clean_url)
    if len(allUrl):
        for list in allUrl:
            cleanList = list.strip('\n')  
            newListUrl = cleanList.strip()
            if newListUrl:
                url = newListUrl+"dongtai"
                soup = def_beautifulSoup.getCrawlContentByUrl(url)
                # 分页获取
                page_total = soup.select('.main_center_left .page_total')
                if len(page_total):
                    total =int(" ".join('%s' %id for id in page_total).split(">")[1].split(" ")[0])
                    count = math.ceil(total/10) 
                    for ct in range(0,count):
                        # 执行分页获取
                        soupurl = def_beautifulSoup.getCrawlContentByUrl(newListUrl+"dongtai/p"+str(ct+1))
                        content = soupurl.select('.main_center_left .center_quanbu_left .ckxq_01 ')
                        # 三亚楼盘动态url写入文件
                        for item in content:
                            data = item.get("href")
                            print("正在循环",url,"链接的第：", ct+1," 页的",data)
                            iou = def_io.defWritelines(data,sanya_dongtai_url,'a') # 追加
                        iou.close()

        # sanya_dongtai_url 内容复制给 sanya_dongtai_clean_url
        shutil.copyfile(sanya_dongtai_url, sanya_dongtai_clean_url) 
        # 清空文件
        def_io.closeTruncate(sanya_dongtai_url)
    else:
        # 无 url 不能往下执行 
        return -1001 