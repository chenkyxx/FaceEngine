# coding:utf-8
import logging
import getpass
import os


class MyLog(object):
    """用于创建一个自用的log"""
    def __init__(self, name):
        # user = getpass.getuser()
        self.logger = logging.getLogger()

        self.logger.handlers.clear()
        self.logger.setLevel(logging.INFO)
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")
        # self.name = os.path.realpath(__file__).split("\\")[-1].split(".")[0]
        # self.logFile = self.path+"\\"+self.name+time.strftime("%Y%m%d%H%M%S", time.localtime())+".log"  # 日志文件名字
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s")

        """日志输出到日志文件内"""
        filehand = logging.FileHandler(self.path+"\\"+name+".log", encoding="utf-8")
        filehand.setFormatter(formatter)
        filehand.setLevel(logging.DEBUG)

        """日志输出到控制台"""
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        # console.setLevel(logging.DEBUG)

        self.logger.addHandler(console)
        self.logger.addHandler(filehand)

        filehand.close()
        console.close()

    def log(self):
        return self.logger


if __name__ == '__main__':
    log = MyLog("lll").log()
    log.info("test")
    log.warn("11111111111111")