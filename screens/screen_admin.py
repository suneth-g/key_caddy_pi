# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen_admin1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#Index(7)

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_screen_admin(object):
    def setupUi(self, screen_admin,iot_handler):
        screen_admin.setObjectName("screen_admin")
        screen_admin.resize(720, 1280)
        screen_admin.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        screen_admin.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Australia))
        self.centralwidget = QtWidgets.QWidget(screen_admin)
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
        self.lblenter.setGeometry(QtCore.QRect(210, 181, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(32)
        self.lblenter.setFont(font)
        self.lblenter.setObjectName("lblenter")
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
        self.btn_loadkeys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_loadkeys.setGeometry(QtCore.QRect(80, 310, 561, 100))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_loadkeys.setFont(font)
        self.btn_loadkeys.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_loadkeys.setStyleSheet("background-color: #f24962; border-radius: 15px;")
        self.btn_loadkeys.setObjectName("btn_loadkeys")
        self.btn_all = QtWidgets.QPushButton(self.centralwidget)
        self.btn_all.setGeometry(QtCore.QRect(80, 450, 561, 100))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_all.setFont(font)
        self.btn_all.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_all.setStyleSheet("background-color: #f24962; border-radius: 15px;")
        self.btn_all.setObjectName("btn_all")
        self.btn_occupied = QtWidgets.QPushButton(self.centralwidget)
        self.btn_occupied.setGeometry(QtCore.QRect(80, 590, 561, 100))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_occupied.setFont(font)
        self.btn_occupied.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_occupied.setStyleSheet("background-color: #f24962; border-radius: 15px;")
        self.btn_occupied.setObjectName("btn_occupied")
        self.frame.raise_()
        self.lblskc.raise_()
        self.btn_goback.raise_()
        self.lblhotel.raise_()
        self.lblenter.raise_()
        self.btn_loadkeys.raise_()
        self.btn_all.raise_()
        self.btn_occupied.raise_()
        screen_admin.setCentralWidget(self.centralwidget)

        self.retranslateUi(screen_admin)
        QtCore.QMetaObject.connectSlotsByName(screen_admin)

        self.btn_all.clicked.connect(self.open_all)
        self.btn_loadkeys.clicked.connect(lambda: self.load_keys(self))
        self.btn_occupied.clicked.connect(self.open_all_accupied)
        self.btn_goback.clicked.connect(self.load_main)

    def retranslateUi(self, screen_admin):
        _translate = QtCore.QCoreApplication.translate
        screen_admin.setWindowTitle(_translate("screen_admin", "MainWindow"))
        self.lblhotel.setText(_translate("screen_admin", "<html><head/><body><p><img src=\":/Cllix logo/cllix-logo_300-115.png\"/></p></body></html>"))
        self.lblskc.setText(_translate("screen_admin", "<html><head/><body><p><img src=\":/SKCLogo/SKC_240-114.jpg\"/></p></body></html>"))
        self.btn_goback.setText(_translate("screen_admin", "Go back"))
        self.lblenter.setText(_translate("screen_admin", "Admin module"))
        self.btn_loadkeys.setText(_translate("screen_admin", "Load keys"))
        self.btn_all.setText(_translate("screen_admin", "Open all bins"))
        self.btn_occupied.setText(_translate("screen_admin", "Open all no show bins"))

    def load_main(self):
        self.parent().setCurrentIndex(0)

    def load_keys(self,db_cursor):
        print("loadkeys")
        self.parent().setCurrentIndex(8)

    def open_all(self):
        print("openall")
    
    def open_all_accupied(aelf):
        print("open occupied")

    def db_fetch(self):
        try:
#            insert_query_bookings = """INSERT INTO bookings("keyName", "keyPinCode", "note", "pickupNote", "roomKeyRfid", "checkinDate", "checkoutDate", "binNo", "status") values (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING "keyId";"""
#            val_bookings = (payload["keyName"], payload["keyPinCode"], payload["note"], payload["pickupNote"], payload["roomKeyRfid"], payload["checkinDate"]+" 10:00:00", payload["checkoutDate"]+" 14:00:00", bin, True)
#            self.cursor.execute(insert_query_bookings, val_bookings)
#            key_id = self.cursor.fetchone()
#            self.conn.commit()
#            update_query_bins = """UPDATE bins SET "inUse" = true WHERE "binNo" = %s;"""
#            self.cursor.execute(update_query_bins, bin)
#            self.conn.commit()
#            return bin[0], key_id[0], True
            print("test")
        except Exception as error:
            print(f"Failed to insert record into iot_payloads table: {error}")
#            return bin,"", False

import screens.SKC_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen_admin = QtWidgets.QMainWindow()
    ui = Ui_screen_admin()
    ui.setupUi(screen_admin)
    screen_admin.show()
    sys.exit(app.exec_())
