from utils.encrypt import Encrypt
from utils import dbutils
from pojo.user import User


def find_user(user):
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id,email,idtype FROM id_table WHERE id=%s", (user,))
        row = cursor.fetchone()
        if row:
            user = User()
            user.setArg(row[0], '', row[1], row[2])
            conn.close()
            return user
        else:
            conn.close()
            return
    except Exception as e:
        print(str(e))


def set_password(user, password):
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE id_table SET passwd=%s WHERE id=%s",
                       (Encrypt.md5(password)[0:19], user.get_id()))
        conn.commit()
        print("密码修改成功!")
        conn.close()
    except Exception as e:
        print(e)


def login(u):
    connection_poll = dbutils.create_pool()
    conn = connection_poll.connection()
    user = User()
    user = find_user(u.get_id())
    if user is None:
        return -2
    else:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT passwd FROM id_table WHERE id=%s", (u.get_id(),))
        row = cursor.fetchone()
        if row[0] == Encrypt.md5(u.get_password())[0:19]:
            return 0
        else:
            return -1
    conn.close()


def register(u):
    connection_poll = dbutils.create_pool()
    conn = connection_poll.connection()
    user = User()
    user = find_user(u.get_id())
    if user is None:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO id_table(id,passwd,email,idtype) VALUES(%s,%s,%s,%s)",
            (u.get_id(), Encrypt.md5(u.get_password())[0:19], u.get_email(), int("1")))
        conn.commit()
        conn.close()
        return 0
    else:
        conn.close()
        return -1
