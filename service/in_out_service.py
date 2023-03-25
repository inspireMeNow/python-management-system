from utils import dbutils
from pojo.out_order import Out_Order
from pojo.in_order import In_Order


def find_all_out_order():
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM out_table")
        rows = cursor.fetchall()
        orders = {}
        i = 0
        for row in rows:
            order = Out_Order()
            order.set_args(row[0], row[1], row[2], row[3], row[4], row[5])
            orders[str(i)] = order.to_json()
            i += 1
        conn.close()
        return orders
    except Exception as e:
        print(str(e))


def find_all_in_order():
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM in_table")
        rows = cursor.fetchall()
        orders = {}
        i = 0
        for row in rows:
            order = In_Order()
            order.set_args(row[0], row[1], row[2],
                           row[3].strftime("%Y-%m-%d %H:%M:%S"), row[4], row[5], row[6])
            orders[str(i)] = order.to_json()
            i += 1
        conn.close()
        return orders
    except Exception as e:
        print(str(e))
