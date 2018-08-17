#encoding:UTF-8
# chenzy python
import time
from def_houses import client
from apscheduler.schedulers.blocking import BlockingScheduler

# APScheduler简介：https://www.cnblogs.com/luxiaojun/p/6567132.html
def my_job():
    nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print ("——》  ღ ღ ღ  采集任务开始时间：",nowTime,"  ღ ღ ღ  《——")
    resultObject = client.do_houses_main()
    if resultObject[0] == 1:
        print("——》  ღ ღ ღ  数据采集完毕，本次一共爬取了:",resultObject[1],"条   ღ ღ ღ  《——")
    else: 
        print ("——》  ღ ღ ღ  采集失败:",resultObject[1],"  ღ ღ ღ  《——")
    print ("——》  ღ ღ ღ  采集任务结束时间：",nowTime,"  ღ ღ ღ  《——")
    print(" ")
#表示每隔1天17时30分01秒执行一次任务
# sched = BlockingScheduler()
# sched.add_job(my_job, 'interval',days = 1,hours = 13,minutes = 20,seconds = 1)
# sched.start()

my_job()
