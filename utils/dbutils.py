import pymysql
# import dbutils
from . import server_encrypt
from cryptography.fernet import Fernet
import base64


def create_pool():
    from DBUtils.PooledDB import PooledDB
    passwd = server_encrypt.sha256('dkyDKY1593574628')
    poll = PooledDB(
        creator=pymysql,
        maxconnections=5,
        mincached=2,
        maxcached=4,
        host='127.0.0.1',
        user='csms',
        password=passwd,
        database='csms',
        charset='utf8mb4'
    )
    return poll
