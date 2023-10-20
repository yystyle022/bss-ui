# -*- coding=utf-8 -*-
# @Time : 2023/4/27 17:12
# @Author : yangyang
# @File : bss-ui/gga_generator.py
import base64


def gen_ntriplogin(username: str, password: str, monutpoint: str):
    '''
    登录语句
    :param username:
    :param password:
    :param monutpoint:
    :return:
    '''
    strUser = '%s:%s' % (username, password)
    bytesUser = base64.b64encode(strUser.encode('utf-8'))
    strLogin = f'GET /{monutpoint} HTTP/1.0\r\nUser-Agent: NTRIP RTKLIB/2.4.3\r\nAccept: */*\r\nAuthorization: Basic {bytesUser.decode()}\r\nConnection: close\r\n\r\n'
    return strLogin.encode('utf-8')


def gen_sdklogin(username: str, password: str, monutpoint: str):
    '''
    登录语句
    :param username:
    :param password:
    :param monutpoint:
    :return:
    '''
    strUser = '%s:%s' % (username, password)
    bytesUser = base64.b64encode(strUser.encode('utf-8'))
    strLogin = f'GET /{monutpoint} HTTP/1.0\r\nUser-Agent: SDK/csdk/1.1.2\r\nAccept: */*\r\nAuthorization: Basic {bytesUser.decode()}\r\nConnection: close\r\n\r\n'
    return strLogin.encode('utf-8')


if __name__ == '__main__':
    print(gen_ntriplogin('xtmwif17055', 'K2sReKjr', 'RTCM32_GRECJ2'))
