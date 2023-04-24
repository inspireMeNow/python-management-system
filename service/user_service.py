from utils import dbutils
from pojo.user import User


def select_all_user():
    try:
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_table")
        rows = cursor.fetchall()
        users = {}
        i = 0
        for row in rows:
            user = User()
            user.set_args(row[0], row[1], row[2], row[3])
            users[str(i)] = user.to_json()
            i += 1
        conn.close()
        return users
    except Exception as e:
        print(str(e))
