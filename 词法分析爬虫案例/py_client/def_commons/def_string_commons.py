#encoding:UTF-8
# chenzy python
from def_houses import def_houses_db  as db#应用模块 
# 清理内容特殊内容(不去除。号)
removeList = ['\'','\"','#','@','&','*','#','$',',','（','）','(',')','.','，','cc','、',' ','','','-','[',']','/',':','：','\\', '·','\\xa0','“','”']

# 删除list全部中指定元素
def cleanContentElement(contentElement):
    for rL in removeList:
        for num in contentElement:
            if num == rL:
                contentElement.remove(rL)
    return contentElement

# 分词匹配与清理错误词
def newKeyWord(host,uName,pw,port,dbName,cleanList,keyWordList):
    newKeyWord = []
    newkeyWordList = keyWordList
    for rL in newkeyWordList:
        for num in list(set(cleanList)):
            if num == rL:
                newkeyWordList.remove(rL)
                newKeyWord.append(rL) 

    # 是否强制添加关键字
    results = db.selectJiebaUserdict(host,uName,pw,port,dbName,1)
    if len(results):
        for row in results:
             for key in newkeyWordList:
                force_keyWord = row['errorWord']
                if key == force_keyWord:
                    print("——》  正在强制添加关键字！",force_keyWord)
                    newKeyWord.append(force_keyWord)
    

    return newKeyWord


#去除所有的 " "
def strs(strs):
    strs = str(strs).replace('\"'," ")  #去除所有的 " "
    strs = str(strs).replace(','," ")  #去除所有的 " "
    return strs

# 替换html文本为红色+标题
def replaceStr(keywordList,title,content):
    content = strs(content)  #去除所有的 " "
    title = strs(title).replace("<h2>", "<div style=\\'text-align:center;font-weight:bold;font-size:20px;\\'>")
    title = strs(title).replace("</h2>", "</div><br><br>。")
    content = title + content
    newcontent = content.split("。")
   
    for i in range(len(newcontent)):
        newcontent[i] = "<p>"+newcontent[i].replace("\r\n","")+"</p>"
    for rL in keywordList:
        # 如果关键词在内容内就加html标签
        if rL in content:
            newcontent = ''.join(newcontent).replace(rL,"<font size=\\'5\\' color=\\'red\\'>"+rL+"</font>")
    return str(newcontent)
