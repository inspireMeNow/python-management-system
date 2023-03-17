import pymysql
# import dbutils
from . import encrypt


def create_pool():
    from DBUtils.PooledDB import PooledDB
    passwd = encrypt.md5("dkyDKY159357")
    poll = PooledDB(
        creator=pymysql,
        maxconnections=5,
        mincached=2,
        maxcached=4,
        host='localhost',
        user='root',
        password=passwd,
        database='csms',
        charset='utf8mb4'
    )
    return poll
