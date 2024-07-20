# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
# Index(0)


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_screen_main(object):
    def setupUi(self, screen_main):
        screen_main.setObjectName("screen_main")
        screen_main.resize(720, 1280)
        screen_main.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        screen_main.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Australia))
        self.centralwidget = QtWidgets.QWidget(screen_main)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_keypickup = QtWidgets.QPushButton(self.centralwidget)
        self.btn_keypickup.setGeometry(QtCore.QRect(40, 300, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_keypickup.setFont(font)
        self.btn_keypickup.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_keypickup.setStyleSheet("background-color: #01ac9a; border-radius: 20px; QPushButton::pressed {background-color: #00ac9a;}")
        self.btn_keypickup.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Australia))
        self.btn_keypickup.setObjectName("btn_keypickup")
        self.btn_keydropoff = QtWidgets.QPushButton(self.centralwidget)
        self.btn_keydropoff.setGeometry(QtCore.QRect(380, 300, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_keydropoff.setFont(font)
        self.btn_keydropoff.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_keydropoff.setAutoFillBackground(False)
        self.btn_keydropoff.setStyleSheet("background-color:#ffbe04; border-radius: 20px;")
        self.btn_keydropoff.setObjectName("btn_keydropoff")
        self.btn_admin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_admin.setGeometry(QtCore.QRect(40, 660, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_admin.setFont(font)
        self.btn_admin.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_admin.setStyleSheet("background-color: #f24962; border-radius: 20px;")
        self.btn_admin.setObjectName("btn_admin")
        self.btn_help = QtWidgets.QPushButton(self.centralwidget)
        self.btn_help.setGeometry(QtCore.QRect(380, 660, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_help.setFont(font)
        self.btn_help.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_help.setAutoFillBackground(False)
        self.btn_help.setStyleSheet("background-color:#2160b9; border-radius: 20px;")
        self.btn_help.setObjectName("btn_help")
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
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 740, 1300))
        self.frame.setStyleSheet("border: 15px solid black; border-radius: 35px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.lblhotel.raise_()
        self.lblskc.raise_()
        self.btn_keydropoff.raise_()
        self.btn_keypickup.raise_()
        self.btn_help.raise_()
        self.btn_admin.raise_()
        self.btn_goback.raise_()
        screen_main.setCentralWidget(self.centralwidget)

        self.retranslateUi(screen_main)
        QtCore.QMetaObject.connectSlotsByName(screen_main)

    def retranslateUi(self, screen_main):
        _translate = QtCore.QCoreApplication.translate
        screen_main.setWindowTitle(_translate("screen_main", "screen_main"))
        self.btn_keypickup.setText(_translate("screen_main", "Key Pick-Up"))
        self.btn_keydropoff.setText(_translate("screen_main", "Key Drop-Off"))
        self.btn_admin.setText(_translate("screen_main", "Admin"))
        self.btn_help.setText(_translate("screen_main", "Help"))
        self.lblhotel.setText(_translate("screen_main", "<html><head/><body><p><img src=\":/Cllix logo/cllix-logo_300-115.png\"/></p></body></html>"))
        self.lblskc.setText(_translate("screen_main", "<html><head/><body><p><img src=\":/SKCLogo/SKC_240-114.jpg\"/></p></body></html>"))
        self.btn_goback.setText(_translate("screen_main", "Go back"))
        
import screens.SKC_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen_main = QtWidgets.QMainWindow()
    ui = Ui_screen_main()
    ui.setupUi(screen_main)
    screen_main.show()
    sys.exit(app.exec_())