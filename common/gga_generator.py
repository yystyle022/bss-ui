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

    strLogin = 'GET /%s HTTP/1.0\r\nUser-Agent: NTRIP RTKLIB/2.4.3\r\nAccept: */*\r\nAuthorization: Basic %s\r\nConnection: close\r\n\r\n' % (
        monutpoint, bytesUser.decode())

    return strLogin.encode('utf-8')

if __name__ == '__main__':
    print(gen_ntriplogin('xtmwif17055','K2sReKjr','RTCM32_GRECJ2'))