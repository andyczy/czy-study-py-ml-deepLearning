#encoding:UTF-8
# chenzy python

import logging

# 读取日志配置文件
# logging.config.fileConfig('logging.conf')  
logging.basicConfig(
   level= logging.DEBUG,
   format = '%(asctime)s : %(levelname)s : %(message)s',
   filename=  'log.log'
)

# Logger：日志记录器，是应用程序中可以直接使用的接口。
# Handler：日志处理器，用以表明将日志保存到什么地方以及保存多久。
# Formatter：格式化，用以配置日志的输出格式。

logging.debug('debug message')
logging.info("info message")
logging.warn('warn message')
logging.error("error message")
logging.critical('critical message')
 