from utils import server_encrypt
from utils import dbutils
from pojo.user import User
from utils import check
import json
from cryptography.fernet import Fernet
import base64


def find_user(username):
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id,email,idtype FROM id_table WHERE id=%s", (username,))
        row = cursor.fetchone()
        if row:
            user = User()
            user.set_args(row[0], '', row[1], row[2])
            conn.close()
            return user
        else:
            conn.close()
            return
    except Exception as e:
        print(str(e))


def set_password(username, password):

    if find_user(username) is None:
        return -1
    elif check.check_password_strength(password) < 2 or password == '':
        return -2
    else:
        input_password = password.encode()
        new_data = server_encrypt.encrypt(input_password)
        new_data['salt'] = new_data['salt'].decode()
        new_data['password'] = new_data['password'].decode()
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE id_table SET passwd=%s WHERE id=%s",
                       (json.dumps(new_data), username))
        conn.commit()
        conn.close()
        return 0


def login(u):
    connection_poll = dbutils.create_pool()
    conn = connection_poll.connection()
    user = User()
    user = find_user(u.get_id())
    if user is None:
        return -2
    elif user.get_idtype() == 0:
        return -3
    else:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT passwd FROM id_table WHERE id=%s", (u.get_id(),))
        row = cursor.fetchone()
        new_data = json.loads(row[0].replace("'", '\"'))
        key = Fernet(base64.urlsafe_b64decode(new_data['salt']))
        if u.get_password() == key.decrypt(new_data['password'].encode()).decode():
            conn.close()
            return 0
        else:
            conn.close()
            return -1


def register(u):
    connection_poll = dbutils.create_pool()
    conn = connection_poll.connection()
    user = User()
    user = find_user(u.get_id())
    if user is None:
        if len(u.get_id()) > 8 or len(u.get_id()) < 2 or len(u.get_email()) > 20 or len(u.get_email()) < 2 or u.get_id() == '' or u.get_password() == '' or u.get_idtype() == 0 or check.check_password_strength(u.get_password()) < 2:
            return -2
        else:
            input_password = u.get_password().encode()
            new_data = server_encrypt.encrypt(input_password)
            new_data['salt'] = new_data['salt'].decode()
            new_data['password'] = new_data['password'].decode()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO id_table(id,passwd,email,idtype) VALUES(%s,%s,%s,%s)",
                (u.get_id(), json.dumps(new_data), u.get_email(), int("1")))
            conn.commit()
            conn.close()
            return 0
    else:
        conn.close()
        return -1


def set_email(username, email):

    if find_user(username) is None:
        return -1
    elif len(email) > 20 or len(email) < 2 or check.is_valid_email(email) is False or email == '':
        return -2
    else:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE id_table SET email=%s WHERE id=%s",
                       (email, username))
        conn.commit()
        conn.close()
        return 0


def delete_user(username):
    if find_user(username) is None:
        return -1
    else:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute("delete from id_table WHERE id=%s",
                       (username,))
        conn.commit()
        conn.close()
        return 0


def admin_login(u):
    connection_poll = dbutils.create_pool()
    conn = connection_poll.connection()
    user = User()
    user = find_user(u.get_id())
    if user is None:
        return -2
    elif user.get_idtype() == 0:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT passwd FROM id_table WHERE id=%s", (u.get_id(),))
        row = cursor.fetchone()
        new_data = json.loads(row[0].replace("'", '\"'))
        key = Fernet(base64.urlsafe_b64decode(new_data['salt']))
        if u.get_password() == key.decrypt(new_data['password'].encode()).decode():
            conn.close()
            return 0
        else:
            conn.close()
            return -1
    else:
        return -3


def find_all():
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id,email,idtype FROM id_table")
        rows = cursor.fetchall()
        users = {}
        i = 0
        for row in rows:
            user = User()
            user.set_args(row[0], '', row[1], row[2])
            users[str(i)] = user.to_json()
            i += 1
        conn.close()
        return users
    except Exception as e:
        print(str(e))
