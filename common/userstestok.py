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
    sql = "SELECT {} FROM poseidon.bss_instance_no WHERE instanceId = '{}'".format(content, instance)
    conn = pymysql.connect(host='bj-cdb-9lx1unfs.sql.tencentcdb.com', port=61861, user='qatmp', password='P&JGRL#VJ6uq',
                           db='poseidon')
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchone()
    cursor.close()
    conn.close()
    return results


def check_auth(instance, appKey, appSecret):
    '''
    sdk差分账号鉴权
    @param serverNumber:
    @return:
    '''
    selectResults = select_instance(instance, content='appKey,appSecret')
    print(selectResults)
    url1 = "http://82.157.72.94:8080/api/v3/auth"
    body = {
        "apiType": "1",
        "apiKey": "{}".format(selectResults[0]),
        "apiSecret": "{}".format(selectResults[1]),
        "deviceId": "{}".format(random.randint(10000, 90000)),
        "deviceType": "{}".format(random.randint(10000, 90000))
    }
    print(body)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url1, headers=headers, data=json.dumps(body))
    print(type(response.text))
    print(response.text)


def ntrip_check_server_number(serverNumber):
    server = select_serverNum(serverNumber, content='serverNo,serverPwd,instanceId')
    sleep(2)
    print(server[2])
    connectType = select_serverNum(serverNumber, content='connectType')
    print(connectType)
    if server:
        if connectType == 3:
            pass
        else:
            aes_encrypt = AES_ENCRYPT()
            d = aes_encrypt.decrypt(server[1].encode("utf-8"))
            try:
                sock = socket.socket()
                sock.connect(("uat1-vrs.sixents.com", 8002))
                # print(i,d)
                sock.send(gen_ntriplogin(server[0], d.decode("utf-8"), "RTCM32_GRECJ2"))
                sss = sock.recv(1024)
                if b'ICY 200 OK' in sss:
                    data = '$GPGGA,025006.78,4007.5533880,N,11627.9528726,E,1,00,1.0,109.077,M,-9.077,M,0.0,*54\r\n\r\n'
                    sock.send(data.encode('utf-8'))
                else:
                    return False
                results = sock.recv(4096)
                if results:
                    return True
                sleep(2)
                sock.close()
            except Exception as e:
                print(e)
    else:
        raise Exception('差分账号不存在')


# num = 300
# us = {}
# # sql1 = """select serverNo,serverPwd from poseidon.bss_server_no bon where serverType=2 and activeRecord=2 and isActive=1 and (expireTime >"2023-10-08 10:07:07.000" or expireTime=null) and serverNo not like "stuser%"  and serverNo not like "hzh%"  order by rand() limit 100"""
# sql2 = """select serverNo,serverPwd from poseidon.bss_server_no where serverNo in ('xtmwif17055')"""
# while len(us) < num:
# cursor.execute(sql2)
# for i in cursor.fetchall():
#     print(i)
#         # print(i)
#         aes_encrypt = AES_ENCRYPT()
#         d = aes_encrypt.decrypt(i[1].encode("utf-8"))
#         try:
#             sock = socket.socket()
#             sock.connect(("uat1-vrs.sixents.com", 8002))
#             # print(i,d)
#             sock.send(gen_ntriplogin(i[0], d.decode("utf-8"), "RTCM32_GRECJ2"))
#             sss = sock.recv(1024)
#             # print(sss)
#             if b'ICY 200 OK' in sss:
#                 us[i[0]] = [i[0], d.decode("utf-8"), "uat1-vrs.sixents.com", 8002, "RTCM32_GRECJ2"]
#                 print(us[i[0]])
#             sock.close()
#         except Exception as e:
#             print(e)
# with open('test1us1.json', 'w', encoding='utf-8') as f:
#     us = json.dump({"users": list(us.values())}, f)
#
#     # num = 300
# cursor.close()
# conn.close()
# exit(0)
# with open('test1us.json', 'r', encoding='utf-8') as f:
#     us = json.load(f)
# for u in us['users']:
#     for i in ["82.157.72.94", ]:
#         u[2] = i
#         try:
#             sock = socket.socket()
#             sock.connect(tuple(u[2:4]))
#             print(gen_ntriplogin(*u[:2], u[-1]))
#             # print(u)
#             sock.send(gen_ntriplogin(*u[:2], u[-1]))
#             sss = sock.recv(1024)
#             print(sss)
#             if b'200 OK' in sss:
#                 print(u, sss)
#             sock.close()
#         except Exception as e:
#             print(e)
#             raise

if __name__ == '__main__':
    print(check_auth('68356'))
