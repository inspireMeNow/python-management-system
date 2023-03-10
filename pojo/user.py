from utils.encrypt import Encrypt
from utils.dbutils import dbutils


class User:
    __id = ''
    __password = ''
    __email = ''
    __idtype = 1

    def __init__(self):
        pass

    def setArg(self, id, password, email, idtype):
        self.__id = id
        self.__password = password
        self.__email = email
        self.__idtype = idtype

    def findUser(self, id):
        try:
            connection_poll = dbutils.create_pool()
            conn = connection_poll.connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id,email,idtype FROM id_table WHERE id=%s", (id,))
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

    def Print(self):
        print(self.__id+"\n"+self.__password+"\n" +
              self.__email+"\n"+f'{self.__idtype}')

    def setPassword(self, password):
        try:
            connection_poll = dbutils.create_pool()
            conn = connection_poll.connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE id_table SET passwd=%s WHERE id=%s",
                           (Encrypt.md5(password)[0:19], self.__id))
            conn.commit()
            print("密码修改成功!")
            conn.close()
        except Exception as e:
            print(e)

    def login(self):
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        user = User()
        user = user.findUser(self.__id)
        if (user == None):
            return -2
        else:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT passwd FROM id_table WHERE id=%s", (user.__id,))
            row = cursor.fetchone()
            if row[0] == Encrypt.md5(self.__password)[0:19]:
                return 0
            else:
                return -1
        conn.close()

    def register(self):
        connection_poll = dbutils.create_pool()
        conn = connection_poll.connection()
        user = User()
        user = user.findUser(self.__id)
        if (user == None):
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO id_table(id,passwd,email,idtype) VALUES(%s,%s,%s,%s)", (self.__id, Encrypt.md5(self.__password)[0:19], self.__email, int("1")))
            conn.commit()
            conn.close()
            return 0
        else:
            conn.close()
            return -1
