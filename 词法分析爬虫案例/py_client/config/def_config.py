#encoding:UTF-8
# chenzy python

# 程序配置
def getHousesConfig():
    housesConfig = {
        'serverUrl':'http://221.182.203.16:9098/oss/uploadImages', # 图片服务器
        'mainUrl':'http://www.home898.com',# 主域名
        'sanyaUrl':'http://sanya.home898.com/',# 子域名
        'siteName':'海南房产网 三亚市',# 网站名称
        'isDelete':False,   # isDelete=True是执行删除操作（删除数据库数据） 
        'isDeleteLocalhostImg':False, # 是否删除本地图片文件
        'isJiebaCut':True,  # isJiebaCut=True是否分词
        'isSelenium':False ,  # isSelenium=True是截图、否则不截图
        'isFilterUrl':False  #  True   不重新抓取网页、用原来的、一般用于测试、节约时间
    }
    return housesConfig
# 数据库配置
def getMysqlConfig():
    # 本地数据库
    # db = {
    #         'host' : '127.0.0.1' , 
    #         'uName' : 'root',
    #         'pw':'root',
    #         'port':3306,
    #         'dbName': 'py_czy_test',
    #         'data_tableName':'illegal_ad'
    #     }
    # # 测试数据库
    db = {
            'port':3306,
            'dbName': 'sycdp',
            'data_tableName':'illegal_ad'
    }
    return db

 

 