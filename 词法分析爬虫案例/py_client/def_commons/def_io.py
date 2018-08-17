#encoding:UTF-8
# chenzy python

# 行写
def defWritelines(data,inputFile,type):
    iou = open(inputFile,type,encoding='utf-8')  
    iou.writelines(data+"\n")
    print("写入数据："+data)
    return iou
# 写
def defWrite(data,inputFile,type):
    iou = open(inputFile,type,encoding='utf-8')  
    iou.write(data)
    return iou


# 行读
def defReadlines(inputFile):
    iou = open(inputFile,"r",encoding='utf-8')  
    readlines = iou.readlines()
    return readlines

# 读
def defRead(inputFile):
    iou = open(inputFile,"r",encoding='utf-8')  
    read = iou.read()
    return read

# 清空文件
def closeTruncate(inputFile):
    iou = open(inputFile,"w")  
    iou.truncate()


# 读写文件行数
def getReadCount(inputFile):
    f=open(inputFile,'r')
    lines=f.readlines()
    f.close()
    count=1
    for line in lines:
        count =count+1
    return count