# -*- coding: utf-8 -*-
import json
import socket
import random
import requests
import pymysql
from time import sleep
from common.gga_generator import gen_ntriplogin
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
    sql = "SELECT {} FROM poseidon.bss_instance_no WHERE instanceId in ('{}')".format(content, instance)
    conn = pymysql.connect(host='bj-cdb-9lx1unfs.sql.tencentcdb.com', port=61861, user='qatmp', password='P&JGRL#VJ6uq',
                           db='poseidon')
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchone()
    cursor.close()
    conn.close()
    return results


def check_auth(instance, appSecret):
    '''
    sdk差分账号鉴权
    @param serverNumber:
    @return:
    '''
    selectResults = select_instance(instance, content='appKey')
    print(selectResults)
    url1 = "http://82.157.72.94:8080/api/v3/auth"
    body = {
        "apiType": "1",
        "apiKey": "{}".format(selectResults[0]),
        "apiSecret": "{}".format(appSecret),
        "deviceId": "{}".format(random.randint(10000, 90000)),
        "deviceType": "{}".format(random.randint(10000, 90000))
    }
    print(body)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url1, headers=headers, data=json.dumps(body))
    json_response = json.loads(response.text)
    if json_response['status'] == 1201:
        return json_response
    else:
        raise Exception('该实例下的差分账号不正常，请重新鉴权')


def check_server_number(serverNumber, appSecret):
    '''
    差分账号登录验证是否可用
    @param serverNumber:
    @param appSecret:
    @return:
    '''
    server = select_serverNum(serverNumber, content='serverNo,serverPwd,instanceId')
    sleep(2)
    connectType = select_instance(server[2], content='connectType')
    if server:
        if connectType == 3:
            serverNsum = check_auth(server[2], appSecret)['name']
            serverPswd = check_auth(server[2], appSecret)['pwd']
        else:
            serverNsum = server[0]
            serverPswd = server[1]
        aes_encrypt = AES_ENCRYPT()
        d = aes_encrypt.decrypt(serverPswd.encode("utf-8"))
        try:
            sock = socket.socket()
            sock.connect(("uat1-vrs.sixents.com", 8002))
            # print(i,d)
            sock.send(gen_ntriplogin(serverNsum, d.decode("utf-8"), "RTCM32_GRECJ2"))
            sss = sock.recv(1024)
            if b'ICY 200 OK' in sss:
                data = '$GPGGA,025006.78,4007.5533880,N,11627.9528726,E,1,00,1.0,109.077,M,-9.077,M,0.0,*54\r\n\r\n'
                sock.send(data.encode('utf-8'))
                results = sock.recv(4096)
                sleep(1)
                sock.close()
                if results:
                    return True
        except Exception as e:
            print(e)
    else:
        raise Exception('差分账号不存在')


if __name__ == '__main__':
    print(check_server_number('xtmwif17052','vw0x0jhez1j8yzedf1qbu65yqgbew631y18dsaxjc5n91dg9qxq3gnv4cisybdur'))
