# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
#import imagenes dent_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(343, 549)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.487, y1:1, x2:0.478, y2:0.636364, stop:0.402985 rgba(133, 133, 133, 237), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 151, 121))
        self.label.setStyleSheet(u"border-image: url(:/cct/Imagen de WhatsApp 2024-07-01 a las 22.24.56_ee4dc190.jpg);\n"
"border-image: url(:/cct/Imagen de WhatsApp 2024-08-13 a las 20.52.17_e647f5ba.jpg);")
        self.label.setPixmap(QPixmap(u"Imagenes/Imagen de WhatsApp 2024-08-13 a las 20.52.17_e647f5ba.jpg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 230, 41, 41))
        self.label_2.setStyleSheet(u"border-image: url(:/cct/8666609_user_icon.png);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setPixmap(QPixmap(u"Imagenes/8666609_user_icon.png"))
        self.label_2.setScaledContents(True)
        self.txtUsuario = QLineEdit(self.centralwidget)
        self.txtUsuario.setObjectName(u"txtUsuario")
        self.txtUsuario.setGeometry(QRect(100, 240, 181, 21))
        self.txtUsuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 310, 41, 41))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-image: url(:/cct/8666757_lock_security_icon.png);")
        self.label_3.setPixmap(QPixmap(u"Imagenes/8666757_lock_security_icon.png"))
        self.label_3.setScaledContents(True)
        self.txtContrasea = QLineEdit(self.centralwidget)
        self.txtContrasea.setObjectName(u"txtContrasea")
        self.txtContrasea.setGeometry(QRect(100, 320, 181, 21))
        self.txtContrasea.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(190, 420, 101, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(60, 420, 101, 31))
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.label.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/cct/Imagen de WhatsApp 2024-08-13 a las 20.52.17_e647f5ba.jpg\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"iniciar ", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"salir ", None))
    # retranslateUi

