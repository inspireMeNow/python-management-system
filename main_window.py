# Form implementation generated from reading ui file '/home/duan/Github/management-system/mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication,QMessageBox
from utils import encrypt
import ssl,socket
from pojo.user import User
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(parent=self.tab)
        self.label.setGeometry(QtCore.QRect(340, 130, 131, 61))
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.tab)
        self.label_3.setGeometry(QtCore.QRect(240, 210, 81, 41))
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(parent=self.tab)
        self.label_2.setGeometry(QtCore.QRect(250, 270, 71, 41))
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton.setGeometry(QtCore.QRect(320, 340, 171, 41))
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 210, 171, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(320, 270, 171, 41))
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 440, 171, 41))
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(260, 210, 71, 41))
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(350, 70, 131, 61))
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(250, 150, 81, 41))
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(260, 270, 71, 41))
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.comboBox = QtWidgets.QComboBox(parent=self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(330, 330, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_11 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(230, 320, 101, 51))
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(250, 380, 81, 41))
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(330, 150, 171, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.tab_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(330, 210, 171, 41))
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.tab_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(330, 270, 171, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.tab_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(330, 380, 171, 41))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 340, 171, 41))
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(250, 270, 71, 41))
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(340, 130, 131, 61))
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(240, 210, 81, 41))
        font = QtGui.QFont()
        font.setFamily("文鼎ＰＬ简中楷")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(320, 210, 171, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 270, 171, 41))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(parent=MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtGui.QAction(parent=MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtGui.QAction(parent=MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtGui.QAction(parent=MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtGui.QAction(parent=MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtGui.QAction(parent=MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtGui.QAction(parent=MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtGui.QAction(parent=MainWindow)
        self.action_9.setObjectName("action_9")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_6)
        self.menu_2.addAction(self.action_8)
        self.menu_2.addAction(self.action_9)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_3)
        self.menu_3.addAction(self.action_4)
        self.menu_3.addAction(self.action_5)
        self.menu_3.addAction(self.action_7)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "库存管理系统"))
        self.label.setText(_translate("MainWindow", "用户登录"))
        self.label_3.setText(_translate("MainWindow", "用户名："))
        self.label_2.setText(_translate("MainWindow", "密码："))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "登录"))
        self.pushButton_3.setText(_translate("MainWindow", "注册"))
        self.label_7.setText(_translate("MainWindow", "密码："))
        self.label_8.setText(_translate("MainWindow", "用户注册"))
        self.label_9.setText(_translate("MainWindow", "用户名："))
        self.label_10.setText(_translate("MainWindow", "邮箱："))
        self.comboBox.setItemText(0, _translate("MainWindow", "员工"))
        self.label_11.setText(_translate("MainWindow", "用户类型："))
        self.label_12.setText(_translate("MainWindow", "验证码："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "注册"))
        self.pushButton_2.setText(_translate("MainWindow", "登录"))
        self.label_4.setText(_translate("MainWindow", "密码："))
        self.label_5.setText(_translate("MainWindow", "登录"))
        self.label_6.setText(_translate("MainWindow", "用户名："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "管理员"))
        self.menu.setTitle(_translate("MainWindow", "选项"))
        self.menu_2.setTitle(_translate("MainWindow", "工具"))
        self.menu_3.setTitle(_translate("MainWindow", "关于"))
        self.action.setText(_translate("MainWindow", "重置"))
        self.action_3.setText(_translate("MainWindow", "帮助"))
        self.action_4.setText(_translate("MainWindow", "隐私政策"))
        self.action_5.setText(_translate("MainWindow", "关于"))
        self.action_6.setText(_translate("MainWindow", "退出"))
        self.action_7.setText(_translate("MainWindow", "鸣谢"))
        self.action_8.setText(_translate("MainWindow", "测试连接"))
        self.action_9.setText(_translate("MainWindow", "疑难解答"))
        self.action_8.triggered.connect(self.test_connection)
        self.action_7.triggered.connect(self.thanks)
        self.action_6.triggered.connect(self.close)
        self.pushButton.clicked.connect(self.is_login)
        self.pushButton_3.clicked.connect(self.is_register)
        self.action_5.triggered.connect(self.about)

    def is_login(self):
        try:
            user = User()
            user.set_args(self.lineEdit_3.text(), encrypt.md5(self.lineEdit_4.text())[0:19], '', 1)
            host = 'localhost'
            port = 8888
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.load_verify_locations(cafile="server/cert/cert.pem")
            # context.check_hostname=False

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                with context.wrap_socket(sock, server_hostname=host) as s:
                    s.connect((host, port))
                    send_data = {'key': 'is_login', 'value': user.to_json()}
                    s.send(json.dumps(send_data).encode())
                    # receive data from the server
                    data = s.recv(1024)
                    print(str(data))
                    if data.decode() == '0':
                        dialog('登录成功，即将进入首页！')
                    elif data.decode() == '-1':
                        dialog('用户名或密码错误！')
                    else:
                        dialog('该用户不存在!')
                    s.close()

        except Exception as e:
            dialog('连接失败!')
    
    def is_register(self):
        try:
            user = User()
            user.set_args(self.lineEdit_5.text(), encrypt.md5(self.lineEdit_6.text())[0:19], self.lineEdit_7.text(), 1)
            host = 'localhost'
            port = 8888
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.load_verify_locations(cafile="server/cert/cert.pem")
            # context.check_hostname=False

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                with context.wrap_socket(sock, server_hostname=host) as s:
                    s.connect((host, port))
                    send_data = {'key': 'is_register', 'value': user.to_json()}
                    s.send(json.dumps(send_data).encode())
                    # receive data from the server
                    data = s.recv(1024)
                    print(str(data))
                    if data.decode() == '0':
                        dialog('注册成功，即将进入登录界面！')
                    elif data.decode() == '-1':
                        dialog('用户名已存在！')
                    else:
                        dialog('注册信息不符合要求!')
                    s.close()

        except Exception as e:
            dialog('连接失败!')

    def close(self):
        QApplication.quit()
        sys.exit()

    def thanks(self):
        dialog(
            '- 编写人员：    \n    - @duan-dky\n- 使用的开源库：    \n    - hashlib    \n    - PyQT6    \n    - socket    \n    - http    \n    - json    \n    - request')

    def about(self):
        dialog('')

    def test_connection(self):
        try:
            host = 'localhost'
            port = 8888
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.load_verify_locations(cafile="server/cert/cert.pem")
            # context.check_hostname=False

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                with context.wrap_socket(sock, server_hostname=host) as s:
                    s.connect((host, port))
                    send_data = {'key': '', 'value': ''}
                    s.send(json.dumps(send_data).encode())
                    # receive data from the server
                    data = s.recv(1024)
                    print(data.decode())
                    dialog('连接成功！')
                    s.close()

        except Exception as e:
            dialog('连接失败,请检查网络！')


def dialog(string):
    msg = QMessageBox()
    msg.setGeometry(240, 210, 81, 41)
    msg.setText(string)
    msg.setWindowTitle('提示')
    msg.setFixedSize(500, 200)
    msg.exec()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
