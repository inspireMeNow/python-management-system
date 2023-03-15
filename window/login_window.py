from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt6 import QtGui
from pojo.user import User
from service import login_service


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('系统登录')
        self.resize(300, 150)
        self.center()

        # 创建窗口控件
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
        layout.addWidget(username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(password_label)
        layout.addWidget(self.password_edit)
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
        user = User()
        user.setArg(username, password, '', 1)

        # user.register()

        is_success = login_service.login(user)

        if is_success == 0:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("提示")
            msg_box.setText("登录成功！")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()

        elif is_success == -1:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("提示")
            msg_box.setText("用户名或密码错误！")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()

        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("提示")
            msg_box.setText("用户名不存在!")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
