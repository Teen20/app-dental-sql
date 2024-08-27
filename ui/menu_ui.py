# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
import imagenes dent_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(944, 624)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.0695473, y1:0.546, x2:0.647, y2:0.540136, stop:0.169154 rgba(133, 133, 133, 237), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ingresarButton = QPushButton(self.centralwidget)
        self.ingresarButton.setObjectName(u"ingresarButton")
        self.ingresarButton.setGeometry(QRect(610, 230, 271, 61))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.ingresarButton.setFont(font)
        self.ingresarButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -80, 311, 711))
        self.label.setStyleSheet(u"image: url(:/cct/PEDIATRA.jpeg);")
        self.label.setPixmap(QPixmap(u"Imagenes/PEDIATRA.jpeg"))
        self.label.setScaledContents(True)
        self.logoatButton = QPushButton(self.centralwidget)
        self.logoatButton.setObjectName(u"logoatButton")
        self.logoatButton.setGeometry(QRect(30, 490, 131, 51))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.logoatButton.setFont(font1)
        self.logoatButton.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(660, 60, 171, 141))
        self.label_2.setStyleSheet(u"image: url(:/cct/Imagen de WhatsApp 2024-08-13 a las 20.52.17_e647f5ba.jpg);")
        self.label_2.setPixmap(QPixmap(u"Imagenes/Imagen de WhatsApp 2024-08-13 a las 20.52.17_e647f5ba.jpg"))
        self.label_2.setScaledContents(True)
        self.pedidosButton = QPushButton(self.centralwidget)
        self.pedidosButton.setObjectName(u"pedidosButton")
        self.pedidosButton.setGeometry(QRect(610, 330, 271, 61))
        self.pedidosButton.setFont(font)
        self.pedidosButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ingresarButton.setText(QCoreApplication.translate("MainWindow", u"Ingreso ", None))
        self.label.setText("")
        self.logoatButton.setText(QCoreApplication.translate("MainWindow", u"salir ", None))
        self.label_2.setText("")
        self.pedidosButton.setText(QCoreApplication.translate("MainWindow", u"Pedidos", None))
    # retranslateUi

