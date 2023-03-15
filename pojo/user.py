class User:
    __id = ''
    __password = ''
    __email = ''
    __idtype = 1

    def __init__(self):
        pass

    def setArg(self, username, password, email, idtype):
        self.__id = username
        self.__password = password
        self.__email = email
        self.__idtype = idtype

    def get_id(self):
        return self.__id

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    def get_idtype(self):
        return self.__idtype

    def print(self):
        print(self.__id + "\n" + self.__password + "\n" +
              self.__email + "\n" + f'{self.__idtype}')
