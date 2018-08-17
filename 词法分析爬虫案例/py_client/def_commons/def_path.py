#encoding:UTF-8
# chenzy python

import os

# 创建目录--图片路径
def init_mkdir(paths):
    success = os.path.exists(paths) # 判断一个目录是否存在
    if success==False:
       os.mkdir(paths)  #创建目录
    return paths

def isHaveImg(filePath):
    success = os.path.exists(filePath) # 判断一个截图是否存在
    return success

# 删除目录下所有文件
def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)


# print(os.getcwd())
# print( os.path.abspath(os.curdir))#获得当前工作目录
# print(os.path.abspath(os.path.dirname(__file__)))