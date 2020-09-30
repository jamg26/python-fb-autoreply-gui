# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gamebot.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import fbchat
import requests
import random
from time import sleep
from fbchat import Client
from fbchat.models import *
import mysql.connector
import os
import _thread
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jamg(object):

    def setupUi(self, jamg):
        global logs
        jamg.setObjectName("jamg")
        jamg.resize(333, 319)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(jamg.sizePolicy().hasHeightForWidth())
        jamg.setSizePolicy(sizePolicy)
        jamg.setMinimumSize(QtCore.QSize(333, 319))
        jamg.setMaximumSize(QtCore.QSize(333, 319))
        self.centralwidget = QtWidgets.QWidget(jamg)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 311, 151))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox.sizePolicy().hasHeightForWidth())

        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setObjectName("groupBox")

        self.u_name = QtWidgets.QLineEdit(self.groupBox)
        self.u_name.setGeometry(QtCore.QRect(20, 40, 161, 20))
        self.u_name.setObjectName("u_name")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 158, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 135, 13))
        self.label_2.setObjectName("label_2")

        self.u_name_2 = QtWidgets.QLineEdit(self.groupBox)
        self.u_name_2.setGeometry(QtCore.QRect(20, 80, 161, 20))
        self.u_name_2.setObjectName("u_name_2")
        self.u_name_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_btn = QtWidgets.QPushButton(self.groupBox)
        self.login_btn.setGeometry(QtCore.QRect(20, 110, 61, 23))
        self.login_btn.setObjectName("login_btn")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 311, 141))
        self.groupBox_2.setObjectName("groupBox_2")

        logs = QtWidgets.QTextEdit(self.groupBox_2)
        logs.setGeometry(QtCore.QRect(10, 20, 291, 111))
        logs.setObjectName("textEdit")
        logs.setReadOnly(True)

        jamg.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(jamg)
        self.statusbar.setObjectName("statusbar")
        jamg.setStatusBar(self.statusbar)

        self.control_box = QtWidgets.QGroupBox(self.centralwidget)
        self.control_box.setGeometry(QtCore.QRect(10, 10, 311, 151))
        self.control_box.setObjectName("control_box")

        self.auto_reply_text = QtWidgets.QLineEdit(self.control_box)
        self.auto_reply_text.setGeometry(QtCore.QRect(10, 40, 151, 21))
        self.auto_reply_text.setObjectName("auto_reply_text")

        self.auto_reply_lbl = QtWidgets.QLabel(self.control_box)
        self.auto_reply_lbl.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.auto_reply_lbl.setObjectName("auto_reply_lbl")

        self.auto_reply_btn = QtWidgets.QPushButton(self.control_box)
        self.auto_reply_btn.setGeometry(QtCore.QRect(170, 40, 41, 21))
        self.auto_reply_btn.setObjectName("auto_reply_btn")

        self.control_box.hide()
        self.retranslateUi(jamg)
        QtCore.QMetaObject.connectSlotsByName(jamg)

        # login button clicked
        self.login_btn.clicked.connect(self.f_login)

        # Set button reply
        self.auto_reply_btn.clicked.connect(self.setReply)

        # on enter
        self.u_name_2.returnPressed.connect(self.f_login)

    def retranslateUi(self, jamg):
        _translate = QtCore.QCoreApplication.translate
        jamg.setWindowTitle(_translate("jamg", "PyBatibot"))
        self.groupBox.setTitle(_translate("jamg", "Login"))
        self.label.setText(_translate("jamg", "Username"))
        self.label_2.setText(_translate("jamg", "Password"))
        self.login_btn.setText(_translate("jamg", "Login"))
        self.groupBox_2.setTitle(_translate("jamg", "Logs"))
        self.control_box.setTitle(_translate("jamg", "Control"))
        self.auto_reply_lbl.setText(_translate("jamg", "AutoReply"))
        self.auto_reply_btn.setText(_translate("jamg", "Set"))

    def f_auth(self, u, p):
        global client
        global active_sub
        sub = subscription(u)
        if sub == "active":
            active_sub = 1
            try:
                client = JamgGamebot(u, p)
                _thread.start_new_thread(client.listen, ())
                self.control_box.show()
                self.u_logs("Logged in success")
            except fbchat.models.FBchatUserError:
                self.u_logs("Login failed")
                self.control_box.hide()
                self.groupBox.show()
        else:
            active_sub = 0
            logs.append("Your account is not active")
            self.groupBox.show()

    def f_login(self):
        self.u_logs("Logging in ... Please wait")
        self.groupBox.hide()
        u = self.u_name.text()
        p = self.u_name_2.text()
        _thread.start_new_thread(self.f_auth, (u, p))

    def u_logs(self, msg):
        logs.append(f'{msg}')

    def setReply(self):
        reply = self.auto_reply_text.text()
        JamgGamebot.reply = reply
        self.u_logs(f'Reply has been changed to {reply}')


class JamgGamebot(Client):

    reply = ""
    thread_id = ""
    thread_type = ThreadType.USER

    def post_msg(self, msg):
        client.send(Message(text=f"{msg}"),
                    thread_id=self.thread_id, thread_type=self.thread_type)

    def onMessage(self, author_id, message_object, thread_id, thread_type, metadata, msg, **kwargs):
        self.thread_id = thread_id
        logs = Ui_jamg()
        if self.reply != "":
            if thread_type == self.thread_type:
                if author_id != self.uid:
                    client.setTypingStatus(
                        TypingStatus.TYPING, thread_id=self.thread_id, thread_type=self.thread_type)
                    sleep(2)
                    self.post_msg(self.reply)


my_db = mysql.connector.connect(
    host="35.187.240.251",
    user="jamg",
    passwd="jamuel26",
    database="bot"
)
my_cursor = my_db.cursor()


def subscription(user):
    my_cursor.execute(f"SELECT * FROM subs WHERE user='{user}'")
    my_result = my_cursor.fetchall()
    res = list(my_result)
    for x in res:
        res = x[2]
    return res


def main():
    logs.append("Facebook auto reply v1.1")
    logs.append("https://jamgph.com")
    url = "https://php.jamgph.com/cron.php?activatebot=jamgph.com"
    r = requests.get(url)
    res = r.text.rstrip()
    if res == "true":
        pass
    else:
        logs.append("Check your internet connection")
        exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jamg = QtWidgets.QMainWindow()
    ui = Ui_jamg()
    ui.setupUi(jamg)
    jamg.show()
    main()
    sys.exit(app.exec_())
