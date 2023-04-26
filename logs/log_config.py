import os
import time
import logging


def get_log(name):
    '''
    生成日志
    @param name: 日志名字
    @return:
    '''
    # 创建一个日志生成器
    logger = logging.getLogger(name)
    # 设置日志生成器的日志级别
    logger.setLevel(logging.INFO)
    # 设置日志路径
    logPath = os.path.abspath(os.path.dirname(__file__)) + r'/log/'
    if not os.path.exists(logPath):
        os.makedirs(logPath)
    # 获取当前时间
    nowTime = time.strftime("%Y_%m_%d %H_%M_%S", time.localtime())
    # 创建一个日志处理器
    fh = logging.FileHandler(r'./logs/log/{}.log'.format(nowTime), encoding='utf-8')
    fh.setLevel(logging.INFO)
    # 创建一个日志格式器
    formatter = logging.Formatter(
        '%(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    # 为日志处理器设置日志格式
    fh.setFormatter(formatter)
    # 为日志生成器添加日志处理器
    logger.addHandler(fh)
    return logger


log = get_log('UI自动化测试')


def path():
    return os.path.abspath(os.path.dirname(__file__))


if __name__ == '__main__':
    print(os.path.abspath(os.path.dirname(__file__)))
