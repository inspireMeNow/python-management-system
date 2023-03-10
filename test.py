import sys
from pojo.user import User


if __name__ == "__main__":
    try:
        
        user=User()

        print("用户注册：")
        user.register()

        print("登录系统：")
        user=user.login()
        
        if(user!=None):
            print("修改用户密码：")
            password=input("请输入你的新密码：")
            str=input("请再次输入您的密码：")
            while((str!=password)|(len(str)>=20)):
                print("请核对您输入的密码并重新输入！")
                password=input("请输入你的新密码：")
                str=input("请再次输入您的密码：")
            user.setPassword(password)

        
    except Exception as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    finally:
        sys.exit()