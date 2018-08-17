#encoding:UTF-8
# chenzy python
import os
from config import def_config
from def_houses import p_sanya_houses,p_sanya_zixun,p_sanya_donggtai,def_houses_db
from def_commons import def_io #应用模块

# 数据库配置
mysqlConfig = def_config.getMysqlConfig()
host = mysqlConfig['host']
uName = mysqlConfig['uName']
pw = mysqlConfig['pw']
port = mysqlConfig['port']
dbName = mysqlConfig['dbName']
data_tableName = mysqlConfig['data_tableName']
 
# 程序配置
housesConfig = def_config.getHousesConfig()
mainUrl = housesConfig['mainUrl']# 主域名
sanyaUrl = housesConfig['sanyaUrl']# 子域名
siteName = housesConfig['siteName']# 网站名称
isDelete = housesConfig['isDelete'] # 是执行删除操作（删除数据库数据和图片文件）
isSelenium = housesConfig['isSelenium'] #isSelenium=True是截图、否则不截图  ###
isJiebaCut = housesConfig['isJiebaCut'] #isJiebaCut=True是否分词
serverUrl = housesConfig['serverUrl']  # 图片服务器
isDeleteImg = housesConfig['isDeleteLocalhostImg']  # 是否删除本地图片文件
isFilterUrl = housesConfig['isFilterUrl']  # # isFilterUrl=True 不重新抓取网页、用原来的、一般用于测试、节约时间

# 1、读取关键字配置文件
path =  os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
keywordData = def_io.defReadlines(path+"/config/key_word_data.txt") # 读文件
keyWordList = '、'.join(keywordData).strip().split('、') #list转str再切分成['最', '最佳', '最爱', '最赚']格式


# 2、程序生成文件
sanya_loupan_clean_url = path+'/data_file/sanya_loupan_clean_url.txt'
sanya_loupan_url = path+'/data_file/sanya_loupan_url.txt'
sanya_dongtai_clean_url = path+'/data_file/sanya_dongtai_clean_url.txt'
sanya_dongtai_url = path+'/data_file/sanya_dongtai_url.txt'
dongtai_clean_url =path+'/data_file/sanya_dongtai_clean_url.txt'

# 从数据库获取然后写入jieba_userdict.txt文件
def_houses_db.closeAndAddUserdict(host,uName,pw,port,dbName,path,"illegal_jieba_userdict")
 
# 返回对象(下标第一位：存放执行状态，第二位：执行信息成功与否信息，第三位：执行的数字信息)
resultObject = []  
def do_houses_main():
    if isFilterUrl==True:
        result = 1
    else:
       # 爬取页面显示的三亚楼盘获取楼盘详情url地址
        p_sanya_houses.getHouseUrl(sanyaUrl,sanya_loupan_clean_url,sanya_loupan_url)
        # 爬取动态url
        result = p_sanya_donggtai.getDontaiUrl(sanya_loupan_clean_url,sanya_dongtai_url,sanya_dongtai_clean_url)
   
        if result != -1001:
            # 执行判断和存储
            conut = p_sanya_zixun.client(mainUrl,keyWordList,dongtai_clean_url,isDelete,isDeleteImg,isSelenium,host,uName,pw,port,dbName,data_tableName,siteName,path,isJiebaCut,serverUrl)
            # print("############################# 数据采集完毕，本次一共爬取了:",conut,"条 ############################")
            resultObject.insert(0,1)
            resultObject.insert(1,conut)
        else:
            resultObject.insert(0,-1001)
            resultObject.insert(1,"p_sanya_donggtai 程序---采集URL异常、请检查！")
    return resultObject
