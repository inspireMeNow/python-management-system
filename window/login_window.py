from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from pojo.user import User

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Login')
        self.resize(300, 150)

        # 创建窗口控件
        title_label = QLabel('用户登录')
        username_label = QLabel('用户名: ')
        password_label = QLabel('密码: ')
        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)  # 设置密码框
        login_button = QPushButton('登录')

        # 绑定登录事件
        login_button.clicked.connect(self.handle_login)

        # 创建布局并添加控件到布局中
        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        user=User()
        user.setArg(username,password,'',1)

        # user.register()

        user=user.login()


