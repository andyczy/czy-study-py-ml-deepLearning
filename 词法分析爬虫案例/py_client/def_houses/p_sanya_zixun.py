#encoding:UTF-8
# chenzy python
from def_commons import def_beautifulSoup #应用模块 
from def_houses import def_matching #应用模块 
from def_commons import def_io #应用模块 
from def_commons import def_selenium #应用模块 
from def_commons import def_string_commons as strCommons
from def_houses import def_houses_db #应用模块 
from def_commons import def_path #应用模块 
from def_commons import upload_file_server
from def_nlp_jieba import def_jieba #应用模块 
import time

# 采集操作
def client(mainUrl,keyWordList,dongtai_clean_url,isDelete,isDeleteImg,isSelenium,host,uName,pw,port,dbName,tableName,siteName,paths,isJiebaCut,serverUrl):
    a = 0
    if isDelete==True:
        # 先清空数据再爬取
        def_houses_db.deletehousesData(host,uName,pw,port,dbName,tableName)
    if isDeleteImg==True:
        # 是否删除本地图片文件
        def_path.del_file(paths+"/img")

    # 获取标题
    read = def_io.defReadlines(dongtai_clean_url)
    for line in read: 
        # 动态url
        url = mainUrl+line
        illegalID = line[7:-6] #17006362

        # 爬取内容
        soup = def_beautifulSoup.getCrawlContentByUrl(url)
        content = soup.find("div",{"class":"SjD_LeftSm_content"})
        if content != None:
            content = content.get_text().replace("\n", "")

        # 标题
        titleH = soup.select(".SjD_LeftSm_title h2")[0]
        title = str(titleH).replace("<h2>", "")
        title = str(title).replace("</h2>", "")
        # 采集到关键字信息 
       
        valueList = def_matching.getMatchingText(keyWordList,title+content)
        if len(valueList):
            # 数据存储对象
            objectList = []
            objectList.insert(6,'\"'+"，".join('%s' %id for id in valueList)+'\"')    #采集到关键字有
            print("——》  正在采集URL:",url)
            print("——》  采集到关键字有：",valueList) 
            # 是否启动分词采集
            if isJiebaCut == True:  #分词-清理-匹配-关键字标红
                isCut = 1
                contentList = def_jieba.jiebaCut(paths,title+content) #分词
                cleanList =  strCommons.strs(strCommons.cleanContentElement(contentList))#清楚元素
                jiebaValue = strCommons.newKeyWord(host,uName,pw,port,dbName,cleanList,valueList) 
                # 关键词与分词是否有相同
                if jiebaValue:
                    value = jiebaValue
                    content = strCommons.replaceStr(jiebaValue,titleH,content)
                    cleanList = ','.join(list(set(cleanList)))
                else:
                    continue
                print("——》  除去jieba分词后有：",value)  
            else:
                isCut = 0
                value = valueList
                cleanList = " "
                content = strCommons.replaceStr(valueList,titleH,title+content)
            
            print("——》  准备采集的关键字有：",value)  
            # 查询id是否已经存在
            results = def_houses_db.selectByillegalID(host,uName,pw,port,dbName,tableName,illegalID)

            objectList.insert(0,int(illegalID))  
            objectList.insert(1,'\"'+siteName+'\"')
            objectList.insert(2,'\"'+content+'\"')  #内容
            objectList.insert(3,'\"'+url+'\"')  #链接
            objectList.insert(4,'\"'+strCommons.strs(title)+'\"')
            objectList.insert(5, '\"'+strCommons.strs("，".join('%s' %id for id in value)) +'\"')
            objectList.insert(8,isCut)
            objectList.insert(7,'\"'+strCommons.strs(str(cleanList))+'\"')  #分词数据

            # 如何截图存在就不进行截图
            successIsHaveImg = def_path.isHaveImg(paths+"/img/"+illegalID+".png")
            if isSelenium==True:
                # 执行截图(本地无图)
                if successIsHaveImg==False:
                    # detester = time.strftime("%Y%m%d%H%M%S", time.localtime()) 
                    imgPath = def_selenium.getScreenshotLinux(paths,url,illegalID)
                    if imgPath != False:
                        imageUrls = upload_file_server.upload_post_img(serverUrl,imgPath) 
                        objectList.insert(9, '\"'+str(imageUrls)+'\"')
                else:
                    if results['screenshot']:
                        imageUrls = upload_file_server.upload_post_img(serverUrl,paths+"/img/"+illegalID+".png") 
                        objectList.insert(9, '\"'+str(imageUrls)+'\"')
                        print("——》  更新数据、截图存在、重新上传图片到服务器！")
                    else:
                        objectList.insert(9, '\"'+str(results['screenshot'])+'\"')
                        print("——》  更新图片URL链接！")
            else:
                objectList.insert(9,False)

                
            # 添加更新操作
            success = def_houses_db.updateAndInsertHouses(host,uName,pw,port,dbName,tableName,results,objectList)
                
            if success: 
                if results==None:
                    print("——》  第:",a+1," 条，数据添加成功!")
                else:
                    print("——》  第:",a+1," 条，数据更新成功!")
            else:
                print("——》  第:",a+1," 条，存储失败、请检查程序!")
            print("——》  ღ ღ ღ ღ ღ ღ ღ ღ ღ 《帅气的分割线》 ღ ღ ღ ღ ღ ღ ღ ღ ღ  《——")
            print(" ")
            print(" ")
            objectList.clear
            a = a+1
    return a;          


