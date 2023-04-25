import pymysql
import yaml
import json

sql = "select server_no,server_mode from bss_server_number bsn where user_id=%s and server_mode=1"


def get_mysql():
    '''
    连接数据库
    @return:
    '''
    with open('./environment.yaml', 'r', encoding='utf-8') as f:
        environment = yaml.load(f.read(), Loader=yaml.FullLoader)
        return environment['mysql']['uat']


def connect():
    con = pymysql.connect(host=get_mysql()['host'], port=get_mysql()['port'], user=get_mysql()['username'],
                          passwd=get_mysql()['password'], database=get_mysql()['database'])
    cursor = con.cursor()
    cursor.execute(sql)
    users = {}
    for u in cursor.fetchall():
        users[u[0]] = u[1]
    with open('data/users.json', 'w', encoding='utf-8') as f:
        json.dump(users, f)


if __name__ == '__main__':
    print(get_mysql()['host'])
