# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen_pick.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
# Index(1)


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_screen_pick(object):
    def setupUi(self, screen_pick):
        screen_pick.setObjectName("screen_pick")
        screen_pick.resize(720, 1280)
        screen_pick.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        screen_pick.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Australia))
        self.centralwidget = QtWidgets.QWidget(screen_pick)
        self.centralwidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Australia))
        self.centralwidget.setObjectName("centralwidget")
        self.btn_pin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pin.setGeometry(QtCore.QRect(40, 300, 640, 300))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_pin.setFont(font)
        self.btn_pin.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_pin.setStyleSheet("background-color: #01ac9a; border-radius: 15px;")
        self.btn_pin.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Anguilla))
        self.btn_pin.setObjectName("btn_pin")
        self.lblhotel = QtWidgets.QLabel(self.centralwidget)
        self.lblhotel.setGeometry(QtCore.QRect(210, 40, 300, 115))
        self.lblhotel.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Anguilla))
        self.lblhotel.setObjectName("lblhotel")
        self.lblskc = QtWidgets.QLabel(self.centralwidget)
        self.lblskc.setGeometry(QtCore.QRect(240, 1040, 240, 114))
        self.lblskc.setObjectName("lblskc")
        self.btn_goback = QtWidgets.QPushButton(self.centralwidget)
        self.btn_goback.setGeometry(QtCore.QRect(290, 1165, 140, 100))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_goback.setFont(font)
        self.btn_goback.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_goback.setStyleSheet("background-color: #f24962; border-radius: 15px;")
        self.btn_goback.setObjectName("btn_goback")
        self.btn_qrcode = QtWidgets.QPushButton(self.centralwidget)
        self.btn_qrcode.setGeometry(QtCore.QRect(40, 660, 640, 300))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_qrcode.setFont(font)
        self.btn_qrcode.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_qrcode.setStyleSheet("background-color: #01ac9a; border-radius: 15px;")
        self.btn_qrcode.setObjectName("btn_qrcode")
        self.lblretrival = QtWidgets.QLabel(self.centralwidget)
        self.lblretrival.setGeometry(QtCore.QRect(130, 200, 481, 60))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(26)
        self.lblretrival.setFont(font)
        self.lblretrival.setObjectName("lblretrival")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 740, 1300))
        self.frame.setStyleSheet("border: 15px solid black; border-radius: 35px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.lblskc.raise_()
        self.btn_pin.raise_()
        self.btn_goback.raise_()
        self.lblhotel.raise_()
        self.btn_qrcode.raise_()
        self.lblretrival.raise_()
        screen_pick.setCentralWidget(self.centralwidget)

        self.retranslateUi(screen_pick)
        QtCore.QMetaObject.connectSlotsByName(screen_pick)

        # Connect button signals to methods
        self.btn_pin.clicked.connect(self.open_screen_pin)
        self.btn_qrcode.clicked.connect(self.open_screen_qr)
        self.btn_goback.clicked.connect(self.go_back)

    def retranslateUi(self, screen_pick):
        _translate = QtCore.QCoreApplication.translate
        screen_pick.setWindowTitle(_translate("screen_pick", "screen_pick"))
        self.btn_pin.setText(_translate("screen_pick", "Enter Pin"))
        self.lblhotel.setText(_translate("screen_pick", "<html><head/><body><p><img src=\":/Cllix logo/cllix-logo_300-115.png\"/></p></body></html>"))
        self.lblskc.setText(_translate("screen_pick", "<html><head/><body><p><img src=\":/SKCLogo/SKC_240-114.jpg\"/></p></body></html>"))
        self.btn_goback.setText(_translate("screen_pick", "Go back"))
        self.btn_qrcode.setText(_translate("screen_pick", "Scan QR Code"))
        self.lblretrival.setText(_translate("screen_pick", "Select the key retrival method"))

    def open_screen_pin(self):
        self.parent().setCurrentIndex(5)

    def open_screen_qr(self):
        self.parent().setCurrentIndex(6)

    def go_back(self):
        self.parent().setCurrentIndex(0)

import screens.SKC_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen_pick = QtWidgets.QMainWindow()
    ui = Ui_screen_pick()
    ui.setupUi(screen_pick)
    screen_pick.show()
    sys.exit(app.exec_())
