from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt6 import QtGui
from pojo.user import User
from service import user_service
import requests
import json

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('用户注册')
        self.resize(300, 150)
        self.center()

        # 创建窗口控件
        username_label = QLabel('用户名: ')
        email_label = QLabel('邮箱：')
        password_label = QLabel('密码: ')
        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)  # 设置密码框
        self.email_edit = QLineEdit()
        login_button = QPushButton('登录')

        # 绑定登录事件
        login_button.clicked.connect(self.handle_login)

        # 创建布局并添加控件到布局中
        layout = QVBoxLayout()
        layout.addWidget(username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(email_label)
        layout.addWidget(self.email_edit)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handle_login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        email = self.email_edit.text()
        user = User()
        user.set_args(username, password, email, 1)

        # user.register()

        response = requests.get('http://localhost:8088/is_register', params=user.to_json())
        response.encoding = 'utf-8'
        new_data = json.dumps(response.text)
        is_success = int(new_data.replace('"', ''))

        if is_success == 0:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("提示")
            msg_box.setText("注册成功！")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()

        elif is_success == -1:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("提示")
            msg_box.setText("用户名已存在！")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()

        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("提示")
            msg_box.setText("密码强度过低！")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
