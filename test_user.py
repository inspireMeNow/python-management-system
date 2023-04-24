import sys
from pojo.login import Login
from service import login_service
import json
import requests

if __name__ == "__main__":
    try:
        # # test search user
        # data = {'id': 'dky' }
        # response = requests.get('http://localhost:8088/search_user', params=data)
        # response.encoding = 'utf-8'
        # new_data = json.dumps(response.text)
        # print(json.loads(new_data))

        # test update password
        data = {'id': 'dky', 'password': 'DKY357896'}
        response = requests.get('http://localhost:8088/set_password', params=data)
        response.encoding = 'utf-8'
        new_data = json.dumps(response.text)
        print(new_data)

        # # test update email
        # data = {'id': 'dky', 'email': 'sadsf@qq.com'}
        # response = requests.get('http://localhost:8088/set_email', params=data)
        # response.encoding = 'utf-8'
        # new_data = json.dumps(response.text)
        # print(new_data)

        # # test login
        # data = {'id': 'wqqqqq', 'password': 'DKY123456'}
        # response = requests.get('http://localhost:8088/is_login', params=data)
        # response.encoding = 'utf-8'
        # new_data = json.dumps(response.text)
        # print(new_data)

        # # test register
        # data = {'id': 'ssss', 'password': 'passssssss', 'email': 'cossss@ds.com', 'idtype': 1}
        # response = requests.get('http://localhost:8088/is_register', params=data)
        # response.encoding = 'utf-8'
        # new_data = json.dumps(response.text)
        # print(new_data)

        # user = Login()

        # # print("用户注册：")
        # # user.register()

        # print("登录系统：")
        # username = input("请输入你的用户名：")
        # password = input("请输入你的密码：")
        # user.set_args(username, password, "", 1)

        # if login_service.login(user) == 0:
        #     print("登录成功\n")
        #     print("修改用户密码：")
        #     password = input("请输入你的新密码：")
        #     r_password = input("请再次输入您的密码：")
        #     while (r_password != password) | (len(r_password) >= 20):
        #         print("请核对您输入的密码并重新输入！")
        #         password = input("请输入你的新密码：")
        #         r_password = input("请再次输入您的密码：")
        #     login_service.set_password(user, password)


    except Exception as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    finally:
        sys.exit()
