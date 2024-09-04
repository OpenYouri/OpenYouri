import os
import time
import logging
import inspect
from Test.Interface.Common.handle_config import conf
from Test.Interface.Common.handle_path import logs_dir
#判断是否存在 当前日志这个文件夹 如果不存在那就创建一个
if not os.path.exists(os.path.join(logs_dir, time.strftime("%Y_%m_%d"))):
    os.makedirs(os.path.join(logs_dir, time.strftime("%Y_%m_%d")))
    # 日志输出到文件绝对路径=----日志分开写入，按日期创建文件
file_name=conf.get('log','file_name')
handlers = {
            logging.DEBUG: "{}_debug.log".format(file_name),
            logging.INFO: "{}_info.log".format(file_name),
            logging.WARNING: "{}_warning.log".format(file_name),
            logging.ERROR: "{}_error.log".format(file_name),
            logging.CRITICAL: "{}_critical.log".format(file_name)
            }

#
def createHandlers():
    logLevels = handlers.keys()
    for level in logLevels:
        path = os.path.join(logs_dir,time.strftime("%Y_%m_%d"),handlers[level])
        handlers[level] = logging.FileHandler(path,encoding='utf-8')

createHandlers()


class TNLog(object):
    def printfNow(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def __init__(self):
        self.__loggers = {}
        logLevels = handlers.keys()
        for level in logLevels:
            logger = logging.getLogger(str(level))
            # 如果不指定level，获得的handler似乎是同一个handler?
            logger.addHandler(handlers[level])
            logger.setLevel(level)
            self.__loggers.update({level: logger})

    def getLogMessage(self, level, message):
        frame, filename, lineNo, functionName, code, unknowField = inspect.stack()[2]
        '''日志格式：[时间] [类型] [记录代码] 信息'''
        return "[%s] [%s] [%s - %s - %s] %s" % (self.printfNow(), level,os.path.basename(filename),  functionName,lineNo, message)

    def info(self, message):
        message = self.getLogMessage("info", message)
        self.__loggers[logging.INFO].info(message)

    def error(self, message):
        message = self.getLogMessage("error", message)
        self.__loggers[logging.ERROR].exception(message)

    def warning(self, message):
        message = self.getLogMessage("warning", message)
        self.__loggers[logging.WARNING].warning(message)

    def debug(self, message):
        message = self.getLogMessage("debug", message)
        self.__loggers[logging.DEBUG].debug(message)

    def critical(self, message):
        message = self.getLogMessage("critical", message)
        self.__loggers[logging.CRITICAL].critical(message)


def log_close():

    #获取当前日期下的所有文件名
    files=os.listdir(os.path.join(logs_dir, time.strftime("%Y_%m_%d")))

    #先关闭logger 进程，否则文件无法删除
    logging.shutdown()

    for file in files:
        #判断当前文件是否是空文件
        if os.path.getsize(os.path.join(logs_dir, time.strftime("%Y_%m_%d"), file)) == 0:
            #删除空文件
            os.remove(os.path.join(logs_dir, time.strftime("%Y_%m_%d"), file))


log=TNLog()
# log.info()
# log.error("错误")

