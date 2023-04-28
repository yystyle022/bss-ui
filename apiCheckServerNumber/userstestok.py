# -*- coding: utf-8 -*-
import socket
import json

import pymysql
import sock as sock
from time import sleep
from apiCheckServerNumber.gga_generator import gen_ntriplogin
from apiCheckServerNumber.unpassword import AES_ENCRYPT

conn = pymysql.connect(host='bj-cdb-9lx1unfs.sql.tencentcdb.com', port=61861, user='qatmp', password='P&JGRL#VJ6uq',db='poseidon')
cursor = conn.cursor()
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
def check_server_number(serverNumber):
    sql1 = """select serverNo,serverPwd from poseidon.bss_server_no where serverNo in ('{}')""".format(serverNumber)
    cursor.execute(sql1)
    server = cursor.fetchone()
    cursor.close()
    conn.close()
    if server:
        aes_encrypt = AES_ENCRYPT()
        d = aes_encrypt.decrypt(server[1].encode("utf-8"))
        try:
            sock = socket.socket()
            sock.connect(("uat1-vrs.sixents.com", 8002))
            # print(i,d)
            sock.send(gen_ntriplogin(server[0], d.decode("utf-8"), "RTCM32_GRECJ2"))
            sss = sock.recv(1024)
            # print(sss)
            if b'ICY 200 OK' in sss:
                data = '$GPGGA,054435.92,3953.9705580,N,11611.5596306,E,1,00,1.0,109.937,M,-9.937,M,0.0,*51\r\n\r\n'
                sock.send(data.encode('utf-8'))
            else:
                raise
            print(sock.recv(4096))
            sleep(2)
            sock.close()
        except Exception as e:
            print(e)
    else:
        raise Exception('差分账号不存在')


if __name__ == '__main__':
    print(check_server_number('xtmwif17055'))


