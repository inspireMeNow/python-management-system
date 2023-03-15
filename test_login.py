import sys
from pojo.user import User
from service import login_service

if __name__ == "__main__":
    try:

        user = User()

        # print("用户注册：")
        # user.register()

        print("登录系统：")
        username = input("请输入你的用户名：")
        password = input("请输入你的密码：")
        user.setArg(username, password, "", 1)

        if login_service.login(user) == 0:
            print("登录成功\n")
            print("修改用户密码：")
            password = input("请输入你的新密码：")
            r_password = input("请再次输入您的密码：")
            while (r_password != password) | (len(r_password) >= 20):
                print("请核对您输入的密码并重新输入！")
                password = input("请输入你的新密码：")
                r_password = input("请再次输入您的密码：")
            login_service.set_password(user, password)


    except Exception as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    finally:
        sys.exit()
