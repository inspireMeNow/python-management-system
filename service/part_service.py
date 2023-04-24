from utils import dbutils
from pojo.part import Part


def find_by_code(p_code):
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM part_table WHERE pcode=%s", (p_code,))
        row = cursor.fetchone()
        part = Part()
        if row:
            part.set_p_code(p_code)
            part.set_args(row[1], row[2], row[3],
                          row[4].strftime("%Y-%m-%d %H:%M:%S"), row[5], row[6], row[7])
            conn.close()
            return part
        else:
            conn.close()
            return
    except Exception as e:
        print(str(e))


def delete_by_code(p_code):
    try:
        if find_by_code(p_code) is None:
            print("该配件不存在!")
            return -1
        else:
            connection_poll = dbutils.create_pool()
            conn = connection_poll.connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM part_table WHERE pcode=%s",
                           (p_code,))
            conn.commit()
            conn.close()
            return 0
    except Exception as e:
        print(e)


def update_by_code(part):
    try:
        if part == None:
            return -2
        if find_by_code(part.get_p_code()) is None:
            print("该配件不存在!")
            return -1
        else:
            connection_poll = dbutils.create_pool()
            conn = connection_poll.connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE part_table SET " +
                           "pname = %s," +
                           "ptype = %s," +
                           "manufacture = %s," +
                           "protime = %s," +
                           "Warrantytime = %s," +
                           "info = %s," +
                           "size = %s " +
                           "WHERE pcode = %s", (part.get_p_name(), part.get_p_type(), part.get_manufacture(), part.get_protime(), part.get_warranty_time(), part.get_info(), part.get_size(), part.get_p_code()))
            conn.commit()
            conn.close()
            return 0
    except Exception as e:
        print(e)


def find_all():
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM part_table")
        rows = cursor.fetchall()
        parts = {}
        i = 0
        for row in rows:
            part = Part()
            part.set_p_code(row[0])
            part.set_args(row[1], row[2], row[3],
                          row[4].strftime("%Y-%m-%d %H:%M:%S"), row[5], row[6], row[7])
            parts[str(i)] = part.to_json()
            i += 1
        conn.close()
        return parts
    except Exception as e:
        print(str(e))


def insert(part):
    try:
        if part == None:
            return -2
        if find_by_code(part.get_p_code()) is None:
            connection_poll = dbutils.create_pool()
            conn = connection_poll.connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO part_table VALUES(%s,%s,%s,%s,%s,%s,%s,%s)", (part.get_p_code(), part.get_p_name(
            ), part.get_p_type(), part.get_manufacture(), part.get_protime(), part.get_warranty_time(), part.get_info(), part.get_size()))
            conn.commit()
            conn.close()
            return 0
        else:
            print("该配件已存在!")
            return -1
    except Exception as e:
        print(e)
