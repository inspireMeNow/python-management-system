from utils import dbutils
from pojo.out_order import Out_Order
from pojo.in_order import In_Order
from pojo.pa_po_table import Pa_Po_Table


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
            order.set_args(row[0], row[1], row[2], row[3], row[4].strftime("%Y-%m-%d %H:%M:%S"), row[5])
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


def find_by_ocode(ocode):
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM out_table WHERE ocode=%s", (ocode,))
        row = cursor.fetchone()
        order = Out_Order()
        if row:
            order.set_args(row[0], row[1], row[2], row[3],
                           row[4].strftime("%Y-%m-%d %H:%M:%S"), row[5])
            conn.close()
            return order
        else:
            conn.close()
            return
    except Exception as e:
        print(str(e))


def find_by_icode(icode):
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM in_table WHERE icode=%s", (icode,))
        row = cursor.fetchone()
        order = In_Order()
        if row:
            order.set_args(row[0], row[1], row[2],
                           row[3].strftime("%Y-%m-%d %H:%M:%S"), row[4], row[5], row[6])
            conn.close()
            return order
        else:
            conn.close()
            return
    except Exception as e:
        print(str(e))


def delete_from_in_order(icode):
    try:
        if find_by_icode(icode) is None:
            print("该入库信息不存在!")
            return -1
        else:
            connection_poll = dbutils.create_pool()
            conn = connection_poll.connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM in_table WHERE icode=%s",
                           (icode,))
            conn.commit()
            conn.close()
            return 0
    except Exception as e:
        print(e)


def delete_from_out_order(ocode):
    try:
        if find_by_ocode(ocode) is None:
            print("该出库信息不存在!")
            return -1
        else:
            connection_poll = dbutils.create_pool()
            conn = connection_poll.connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM out_table WHERE ocode=%s",
                           (ocode,))
            conn.commit()
            conn.close()
            return 0
    except Exception as e:
        print(e)


def insert_to_in_order(in_order):
    try:
        if find_by_icode(in_order.get_in_code()) is not None:
            print("该入库信息已存在!")
            return -1
        else:
            connection_poll = dbutils.create_pool()
            conn = connection_poll.connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO in_table VALUES(%s,%s,%s,%s,%s,%s,%s)",
                           (in_order.get_in_code(), in_order.get_p_code(), in_order.get_num(), in_order.get_in_time(), in_order.get_r_code(), in_order.get_s_type(), in_order.get_u_code()))
            conn.commit()
            conn.close()
            return 0
    except Exception as e:
        print(e)


def insert_to_out_order(out_order):
    try:
        if find_by_ocode(out_order.get_out_code()) is not None:
            print("该出库信息已存在!")
            return -1
        else:
            connection_poll = dbutils.create_pool()
            conn = connection_poll.connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO out_table VALUES(%s,%s,%s,%s,%s,%s)",
                           (out_order.get_out_code(), out_order.get_p_code(), out_order.get_r_code(), out_order.get_num(), out_order.get_out_time(), out_order.get_u_code()))
            conn.commit()
            conn.close()
            return 0
    except Exception as e:
        print(e)


def update_in_order(in_order):
    try:
        if find_by_icode(in_order.get_in_code()) is None:
            print("该入库信息不存在!")
            return -1
        else:
            connection_poll = dbutils.create_pool()
            conn = connection_poll.connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE in_table SET pcode=%s,num=%s,itime=%s,rcode=%s,stype=%s,ucode=%s WHERE icode=%s",
                           (in_order.get_p_code(), in_order.get_num(), in_order.get_in_time(), in_order.get_r_code(), in_order.get_s_type(), in_order.get_u_code(), in_order.get_in_code()))
            conn.commit()
            conn.close()
            return 0
    except Exception as e:
        print(e)


def update_out_order(out_order):
    try:
        if find_by_ocode(out_order.get_out_order()) is None:
            print("该出库信息不存在!")
            return -1
        else:
            connection_poll = dbutils.create_pool()
            conn = connection_poll.connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE out_table SET pcode=%s,rcode=%s,num=%s,otime=%s,ucode=%s WHERE ocode=%s",
                           (out_order.get_p_code(), out_order.get_r_code(), out_order.get_num(), out_order.get_out_time(), out_order.get_u_code(), out_order.get_out_order()))
            conn.commit()
            conn.close()
            return 0
    except Exception as e:
        print(e)


def select_by_sty_rco(stype, rcode):
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM pa_po_table WHERE stype=%s and rcode = %s", (stype, rcode))
        row = cursor.fetchone()
        order = Pa_Po_Table()
        if row:
            order.set_args(row[0], row[1], row[2],
                           row[3], row[4])
            conn.close()
            return order
        else:
            conn.close()
            return
    except Exception as e:
        print(str(e))


def select_by_pco_rco(p_code, r_code):
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM pa_po_table WHERE pcode=%s and rcode = %s", (p_code, r_code))
        row = cursor.fetchone()
        order = Pa_Po_Table()
        if row:
            order.set_args(row[0], row[1], row[2],
                           row[3], row[4])
            conn.close()
            return order
        else:
            conn.close()
            return
    except Exception as e:
        print(str(e))


def select_by_rco(rcode):
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM pa_po_table WHERE rcode=%s", (rcode,))
        row = cursor.fetchone()
        order = Pa_Po_Table()
        if row:
            order.set_args(row[0], row[1], row[2],
                           row[3], row[4])
            conn.close()
            return order
        else:
            conn.close()
            return
    except Exception as e:
        print(str(e))


def select_by_scode(scode):
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM pa_po_table WHERE scode=%s", (scode,))
        row = cursor.fetchone()
        order = Pa_Po_Table()
        if row:
            order.set_args(row[0], row[1], row[2],
                           row[3], row[4])
            conn.close()
            return order
        else:
            conn.close()
            return
    except Exception as e:
        print(str(e))


def select_all():
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pa_po_table")
        rows = cursor.fetchall()
        orders = {}
        i = 0
        for row in rows:
            order = Pa_Po_Table()
            order.set_args(row[0], row[1], row[2],
                           row[3], row[4])
            orders[str(i)] = order.to_json()
            i += 1
        conn.close()
        return orders
    except Exception as e:
        print(str(e))
