#encoding:UTF-8
# chenzy python

# MySQLdb只支持Python2.*，还不支持3.*,可以用PyMySQL代替。
# 安装方法：pip install PyMySQL
import pymysql
import time
from def_commons import def_io #应用模块
pymysql.install_as_MySQLdb()
# import MySQLdb
# import MySQLdb.cursors

# 链接mysql数据库
def getMySQLDB(host,uName,pw,dbName,port):
    # print("——》  数据库正在连接！  《——")
    conn = pymysql.connect(host=host, user=uName, passwd=pw, db=dbName, port=port, charset='utf8', cursorclass = pymysql.cursors.DictCursor)
    conn.autocommit(True)
    # print("——》  数据库连接正常！ 《——")
    return conn

# 关闭资源
def closeAll(db,cursor):
    if db:
      db.close()
    if cursor:
        cursor.close()

# 获取关键字
def selectHouses(host,uName,pw,port,dbName,tableName):
    sql = "SELECT * FROM "+tableName
    try: 
        # 链接数据库
        db = getMySQLDB(host,uName,pw,dbName,port)
        cursor = db.cursor()
        # 执行
        cursor.execute(sql)>0
        # 获取所有记录列表
        results = cursor.fetchall()
        keyWordList = []
        for row in results:
            key = row['key']
            keyWordList.append(key)
    except:  
        # 如果发生错误则回滚  
        db.rollback()  
    closeAll(db,cursor)
    return keyWordList

# 获取关键字
def closeAndAddUserdict(host,uName,pw,port,dbName,path,userdictTableName):
    sql = "SELECT * FROM "+userdictTableName
    try: 
        # 链接数据库
        db = getMySQLDB(host,uName,pw,dbName,port)
        cursor = db.cursor()
        # 执行
        cursor.execute(sql)>0
        # 获取所有记录列表
        results = cursor.fetchall()
        # 清空文件
        def_io.closeTruncate(path+"/config/jieba_userdict.txt")
        for row in results:
            key = row['errorWord']
            w = def_io.defWritelines(key,path+"/config/jieba_userdict.txt","a")
            w.close
    except:  
        # 如果发生错误则回滚  
        db.rollback()  
    closeAll(db,cursor)


# 获取关键字
def selectByillegalID(host,uName,pw,port,dbName,tableName,illegalID):
    # SQL 查询语句
    sql = "SELECT * FROM "+tableName +" where illegalID="+illegalID
    try: 
        # 链接数据库
        db = getMySQLDB(host,uName,pw,dbName,port)
        cursor = db.cursor()
        # 执行
        cursor.execute(sql)>0
        # 获取所有记录列表
        results = cursor.fetchone()
    except:  
        # 如果发生错误则回滚  
        db.rollback()  
    closeAll(db,cursor)
    return results

# 获取关键字illegal_jieba_userdict表
def selectJiebaUserdict(host,uName,pw,port,dbName,force_keyWord):
    # SQL 查询语句
    sql = "SELECT * FROM illegal_jieba_userdict where is_force_keyWord="+force_keyWord
    try: 
        # 链接数据库
        db = getMySQLDB(host,uName,pw,dbName,port)
        cursor = db.cursor()
        # 执行
        cursor.execute(sql)>0
        # 获取所有记录列表
        results = cursor.fetchall()
    except:  
        # 如果发生错误则回滚  
        db.rollback()  
    closeAll(db,cursor)
    return results



# 更新房产数据
def updateAndInsertHouses(host,uName,pw,port,dbName,tName,isUpdate,OList):
    illegalID = OList[0]
    siteName = OList[1]
    content = OList[2]
    adUrl = OList[3]
    title = OList[4]
    keyWord = OList[5]
    keyWord_before = OList[6]
    isCut = OList[8]
    cutWord = OList[7]
    modifyTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    if isUpdate==None:
        screenshot = OList[9]
        if screenshot == False:
            screenshot = " \" \" "
        sql ="insert into "+tName+"(illegalID,siteName,illegalContent,adUrl,screenshot,illegalKeyWord,isCut,cutWord,title,illegalKeyWord_before) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (illegalID, siteName,content,adUrl,screenshot,keyWord,isCut,cutWord,title,keyWord_before)
        print("——》  正在添加数据，sql：",sql)
    else:
        # 更新
        sql= "update "+tName+" set illegalContent='%s',title='%s',illegalKeyWord='%s',illegalKeyWord_before='%s' ,modifyTime='%s' where illegalID='%s' " % (content ,title,keyWord,keyWord_before,modifyTime,illegalID)
        print("——》  正在更新数据，sql：",sql)
    try: 
        # print("sqlsql:",sql)
        db = getMySQLDB(host,uName,pw,dbName,port)
        cursor = db.cursor()
        success = cursor.execute(sql)>0
        # 提交到数据库执行  
        # print("success:",success)
        # if success==True:         
        #     print("——》  数据存储成功!") 
        # else:
        #     print("——》  数据存储失败!") 
        db.commit()
    except ValueError:  
        print("——》  数据存储异常:",ValueError)
        db.rollback()  
    finally:
        closeAll(db,cursor)
    return success;

# insertHouses('127.0.0.1','root','root',3306,'py_czy_test','illegal_ad',1)
   
 


# 删除房产信息（清空）
def deletehousesData(host,uName,pw,port,dbName,tableName):
    db = getMySQLDB(host,uName,pw,dbName,port)
    cursor = db.cursor()
    success = cursor.execute("delete from "+tableName)>0
    try:  
    # 提交到数据库执行  
        db.commit() 
        if success:         
            print("——》  删除成功")
        else:
            print("——》  删除失败") 
    except:  
        # 如果发生错误则回滚  
        db.rollback()  
    closeAll(db,cursor)


 