# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen_qr.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#Index(6)

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_screen_qr(object):
    def setupUi(self, screen_qr):
        screen_qr.setObjectName("screen_qr")
        screen_qr.resize(720, 1280)
        screen_qr.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        screen_qr.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Australia))
        self.centralwidget = QtWidgets.QWidget(screen_qr)
        self.centralwidget.setObjectName("centralwidget")
        self.lblhotel = QtWidgets.QLabel(self.centralwidget)
        self.lblhotel.setGeometry(QtCore.QRect(210, 40, 300, 115))
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
        self.lblenter = QtWidgets.QLabel(self.centralwidget)
        self.lblenter.setGeometry(QtCore.QRect(130, 200, 391, 160))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(8)
        self.lblenter.setFont(font)
        self.lblenter.setObjectName("lblenter")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 570, 161, 161))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 740, 1300))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("border: 15px solid black;  border-radius: 35px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.lblskc.raise_()
        self.btn_goback.raise_()
        self.lblhotel.raise_()
        self.lblenter.raise_()
        self.label.raise_()
        screen_qr.setCentralWidget(self.centralwidget)

        self.retranslateUi(screen_qr)
        QtCore.QMetaObject.connectSlotsByName(screen_qr)

        self.btn_goback.clicked.connect(self.go_back)

    def retranslateUi(self, screen_qr):
        _translate = QtCore.QCoreApplication.translate
        screen_qr.setWindowTitle(_translate("screen_qr", "screen_qr"))
        self.lblhotel.setText(_translate("screen_qr", "<html><head/><body><p><img src=\":/Cllix logo/cllix-logo_300-115.png\"/></p></body></html>"))
        self.lblskc.setText(_translate("screen_qr", "<html><head/><body><p><img src=\":/SKCLogo/SKC_240-114.jpg\"/></p></body></html>"))
        self.btn_goback.setText(_translate("screen_qr", "Go back"))
        self.lblenter.setText(_translate("screen_qr", "Scan your QR code"))
        self.label.setText(_translate("screen_qr", "<html><head/><body><p><img src=\":/QR code/qr-code-scan-icon.png\"/></p></body></html>"))

    def go_back(self):
        self.parent().setCurrentIndex(0)

import screens.SKC_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen_qr = QtWidgets.QMainWindow()
    ui = Ui_screen_qr()
    ui.setupUi(screen_qr)
    screen_qr.show()
    sys.exit(app.exec_())