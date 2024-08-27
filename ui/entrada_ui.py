# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entrada.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)
import imagenes dent_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(945, 621)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.487, y1:1, x2:0.478, y2:0.636364, stop:0.402985 rgba(133, 133, 133, 237), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.productTable = QTableWidget(self.centralwidget)
        if (self.productTable.columnCount() < 7):
            self.productTable.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.productTable.setObjectName(u"productTable")
        self.productTable.setGeometry(QRect(100, 240, 711, 261))
        self.productTable.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 80, 91, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.idproductoInput = QLineEdit(self.centralwidget)
        self.idproductoInput.setObjectName(u"idproductoInput")
        self.idproductoInput.setGeometry(QRect(210, 80, 211, 22))
        self.idproductoInput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 120, 111, 21))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.nombreInput = QLineEdit(self.centralwidget)
        self.nombreInput.setObjectName(u"nombreInput")
        self.nombreInput.setGeometry(QRect(210, 120, 211, 22))
        self.nombreInput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 160, 111, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btnSalir = QPushButton(self.centralwidget)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(710, 530, 93, 28))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.btnSalir.setFont(font1)
        self.btnSalir.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(120, 530, 93, 28))
        self.addButton.setFont(font1)
        self.addButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(520, 120, 111, 21))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(520, 160, 111, 21))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 10, 851, 51))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(520, 80, 111, 21))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.idcategoriaInput = QLineEdit(self.centralwidget)
        self.idcategoriaInput.setObjectName(u"idcategoriaInput")
        self.idcategoriaInput.setGeometry(QRect(620, 80, 201, 22))
        self.idcategoriaInput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stockInput = QLineEdit(self.centralwidget)
        self.stockInput.setObjectName(u"stockInput")
        self.stockInput.setGeometry(QRect(620, 160, 201, 22))
        self.stockInput.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.idpresentacionInput = QLineEdit(self.centralwidget)
        self.idpresentacionInput.setObjectName(u"idpresentacionInput")
        self.idpresentacionInput.setGeometry(QRect(210, 160, 211, 22))
        self.idpresentacionInput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.BuscarButton = QPushButton(self.centralwidget)
        self.BuscarButton.setObjectName(u"BuscarButton")
        self.BuscarButton.setGeometry(QRect(590, 530, 93, 28))
        self.BuscarButton.setFont(font1)
        self.BuscarButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(470, 530, 93, 28))
        self.editButton.setFont(font1)
        self.editButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.newButton = QPushButton(self.centralwidget)
        self.newButton.setObjectName(u"newButton")
        self.newButton.setGeometry(QRect(350, 530, 93, 28))
        self.newButton.setFont(font1)
        self.newButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.idcapacidadInput = QLineEdit(self.centralwidget)
        self.idcapacidadInput.setObjectName(u"idcapacidadInput")
        self.idcapacidadInput.setGeometry(QRect(210, 200, 211, 22))
        self.idcapacidadInput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(90, 200, 111, 21))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.precioInput = QLineEdit(self.centralwidget)
        self.precioInput.setObjectName(u"precioInput")
        self.precioInput.setGeometry(QRect(620, 120, 201, 22))
        self.precioInput.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.addButton_2 = QPushButton(self.centralwidget)
        self.addButton_2.setObjectName(u"addButton_2")
        self.addButton_2.setGeometry(QRect(240, 530, 93, 28))
        self.addButton_2.setFont(font1)
        self.addButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.productTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"idproducto", None));
        ___qtablewidgetitem1 = self.productTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"nombre", None));
        ___qtablewidgetitem2 = self.productTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"idpresentacion", None));
        ___qtablewidgetitem3 = self.productTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"idcapacidad", None));
        ___qtablewidgetitem4 = self.productTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"idcategoria", None));
        ___qtablewidgetitem5 = self.productTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"precio", None));
        ___qtablewidgetitem6 = self.productTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"stock", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Presentacion", None))
        self.btnSalir.setText(QCoreApplication.translate("MainWindow", u"salir ", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Agregar ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Categoria ", None))
        self.BuscarButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.newButton.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Capacidad", None))
        self.addButton_2.setText(QCoreApplication.translate("MainWindow", u"Salida", None))
    # retranslateUi

