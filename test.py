# -*- coding=utf-8 -*-
# @Time : 2023/5/6 9:35
# @Author : yangyang
# @File : bss-ui/test.py
import json
import requests

Authorization = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjEwLCJhY3RpdmUiOiJ1YXQiLCJpYXQiOjE2ODMyODMwMzQsImV4cCI6MTY4MzM2OTQzNCwibmJmIjoxNjgzMjgzMDM0fQ.FDa4s373pE2UupmZsOeBozCOmRRcgw9bpcb_BYkmi_w"
Cookie = "experimentation_subject_id=IjI3YTdkYTg4LTQ0YTAtNGYxOS04NTlkLTRkODBjODhmNTM1MCI%3D--dbb23735860f7fe1fc0d7797c6080d2a207fc12b; accessToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjEwLCJhY3RpdmUiOiJ1YXQiLCJpYXQiOjE2ODMyODMwMzQsImV4cCI6MTY4MzM2OTQzNCwibmJmIjoxNjgzMjgzMDM0fQ.FDa4s373pE2UupmZsOeBozCOmRRcgw9bpcb_BYkmi_w; Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjcxMjY4LCJhY3RpdmUiOiJ1YXQiLCJpYXQiOjE2ODMzMzU4NTcsImV4cCI6MTY4MzQyMjI1NywibmJmIjoxNjgzMzM1ODU3fQ.o6aNn8kkI6ljQSX1rJpjDniEtVPgajtv5lNpAmOTo8A"
ContentType = "application/json"
UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
Connection = "keep-alive"


def guan_li_duan_kuo_rong_shen_qing():
    url1 = "https://bss-backend-uat.sixents.com/api/order/offline-order/create"
    body1 = {
        "serverOrderType": 3,
        "purpose": 2,
        "orderMode": 1,
        "testActive": "false",
        "userId": 71268,
        "productId": 6,
        "num": 1000,
        "duration": 1,
        "price": "1.33",
        "offlinePayDate": "2023-05-06",
        "salesMan": "洋洋",
        "salesManPhone": "18322369885",
        "instanceId": 68363,
        "status": 1,
        "unit": 3
    }

    headers1 = {"Authorization": Authorization, "Cookie": Cookie, "Content-Type": ContentType, "User-Agent": UserAgent,
               "Connection": Connection}
    print(headers1)
    response = requests.post(url=url1, headers=headers1, data=json.dumps(body1))
    jsonResponse = json.dumps(response.text)
    print(jsonResponse)


if __name__ == '__main__':
    guan_li_duan_kuo_rong_shen_qing()
