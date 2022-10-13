# —— coding :utf-8 ——
# @time:    2020/10/7 20:59
# @IDE:     webTest_frmewok_v2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    my_log.py
import os
import pathlib
from datetime import datetime
import logging
from Common.file_path import logs_path
class MyLog:
    today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    now_date_time = datetime.now().strftime('%Y%m%d%H%M%S')
    def mylog(self, msg, level):
        # 1. 定义一个日志收集器 logger
        logger = logging.getLogger('my_logger')
        # 2. 设置级别
        logger.setLevel('INFO')

        # 3. 设置输出格式
        formater = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        # 4. 创建一个输出渠道
        ch = logging.StreamHandler()
        ch.setLevel('INFO')
        ch.setFormatter(formater)  # 输出格式
        # log_file = os.path.join(logs_path,'{}.log'.format(self.now_date_time))
        log_file = os.path.join(logs_path,'test.log')
        # pathlib.Path(log_file).touch()
        fh = logging.FileHandler(log_file, encoding='UTF-8')
        fh.setLevel('ERROR')
        fh.setFormatter(formater)

        # 5. 两者对接----指定输出渠道
        logger.addHandler(ch)
        logger.addHandler(fh)

        # 6. 收集日志
        if level == 'DEBUG':
            logger.debug(msg)
        elif level == 'INFO':
            logger.info(msg)
        elif level == 'WARNING':
            logger.warning(msg)
        elif level == 'ERROR':
            logger.error(msg)
        elif level == 'CRITICAL':
            logger.critical(msg)
        # 关闭渠道
        logger.removeHandler(ch)
        logger.removeHandler(fh)

    def debug(self, msg):
        self.mylog(msg, 'DEBUG')

    def info(self, msg):
        self.mylog(msg, 'INFO')

    def warning(self, msg):
        self.mylog(msg, 'WARNING')

    def error(self, msg):
        self.mylog(msg, 'ERROR')

    def critical(self, msg):
        self.mylog(msg, 'CRITICAL')


if __name__ == '__main__':
    my_logger = MyLog()
    my_logger.debug('debug级别信息！')
    my_logger.info('info级别信息！')
    my_logger.warning('warning级别信息！')
    my_logger.error('error级别信息！')
    # my_logger.critical('critical级别信息！')
