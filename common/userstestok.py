# -*- coding: utf-8 -*-
import re
import json
import socket
import random
import requests
import pymysql
from time import sleep
from common.playwrightFunction import AuthURL
from common.gga_generator import gen_ntriplogin, gen_sdklogin

from common.unpassword import AES_ENCRYPT


def select_serverNum(serverNumber, content='*'):
    '''
    数据库查询差分账号信息
    @param serverNumber:
    @return:
    '''
    sql = "select {} from poseidon.bss_server_no where serverNo in ('{}')".format(content, serverNumber)
    conn = pymysql.connect(host='bj-cdb-9lx1unfs.sql.tencentcdb.com', port=61861, user='qatmp', password='P&JGRL#VJ6uq',
                           db='poseidon')
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchone()
    cursor.close()
    conn.close()
    return results


def select_instance(instance, content="*"):
    '''
    数据库查询实例信息
    @param instance:
    @param content:
    @return:
    '''
    sql = "SELECT {} FROM poseidon.bss_instance_no WHERE instanceId in ('{}') AND isbind = 0".format(content, instance)
    conn = pymysql.connect(host='bj-cdb-9lx1unfs.sql.tencentcdb.com', port=61861, user='qatmp', password='P&JGRL#VJ6uq',
                           db='poseidon')
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchone()
    cursor.close()
    conn.close()
    return results


def auth(appKey, appSecret):
    '''
    差分账号鉴权
    @param appKey: AK
    @param appSecret: AS
    @return:
    '''
    try:
        deivceType = random.randint(100000, 200000)
        body = {
            "apiType": "1",
            "apiKey": appKey,
            "apiSecret": appSecret,
            "deviceId": f"{deivceType}",
            "deviceType": f"{deivceType}"
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url=AuthURL, headers=headers, json=body).json()
        print(body, response)
        if response['status'] == 1201:
            return response['name'], response['pwd']
        else:
            return False
    except Exception as e:
        print(f"鉴权失败,错误信息为：{e}")


def ntrip_send_gga(serverNumber, pwd):
    '''
    差分账号ntrip登录验证是否可用
    @param serverNumber:
    @param appSecret:
    @return:
    '''
    try:
        sock = socket.socket()
        sock.connect(("uat1-vrs.sixents.com", 8002))
        sock.send(gen_ntriplogin(serverNumber, pwd, "RTCM32_GRECJ2"))
        response = sock.recv(1024)
        print(response)
        if b'ICY 200 OK' in response:
            data = '$GPGGA,025006.78,4007.5533880,N,11627.9528726,E,1,00,1.0,109.077,M,-9.077,M,0.0,*54\r\n\r\n'
            sock.send(data.encode('utf-8'))
            sleep(2)
            results = sock.recv(4096)
            sock.close()
            if results:
                print(results)
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print(e)


def sdk_send_gga(serverNumber, pwd):
    '''
    差分账号sdk登录验证是否可用
    @param serverNumber:
    @param appSecret:
    @return:
    '''
    try:
        sock = socket.socket()
        sock.connect(("uat1-vrs.sixents.com", 8002))
        sock.send(gen_sdklogin(serverNumber, pwd, "RTCM32_GRECJ2"))
        response = sock.recv(1024)
        print(response)
        if b'ICY 200 OK' in response:
            data = '$GPGGA,025006.78,4007.5533880,N,11627.9528726,E,1,00,1.0,109.077,M,-9.077,M,0.0,*54\r\n\r\n'
            sock.send(data.encode('utf-8'))
            sleep(2)
            results = sock.recv(4096)
            sock.close()
            if results:
                print(results)
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # print(ntrip_send_gga(serverNumber='xtmwif659330', pwd='mKEKxsN2'))
    # print(auth('0143769132', 'x7tr2yuw90b9y33fr555f4ye0rqjj6yu7zwe2uinerxqfhyy5u23pf7eadpk87fq'))
    print(f"uiceshi{random.randint(20000, 30000)}")
