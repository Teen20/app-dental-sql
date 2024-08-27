# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pedidos.ui'
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
        MainWindow.resize(946, 624)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.487, y1:1, x2:0.478, y2:0.636364, stop:0.402985 rgba(133, 133, 133, 237), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 120, 111, 16))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.idpedidoInput = QLineEdit(self.centralwidget)
        self.idpedidoInput.setObjectName(u"idpedidoInput")
        self.idpedidoInput.setGeometry(QRect(60, 150, 151, 22))
        self.idpedidoInput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 190, 131, 20))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.idproductoInput = QLineEdit(self.centralwidget)
        self.idproductoInput.setObjectName(u"idproductoInput")
        self.idproductoInput.setGeometry(QRect(60, 210, 151, 22))
        self.idproductoInput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(310, 120, 55, 20))
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(310, 180, 55, 20))
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pedidosTable = QTableWidget(self.centralwidget)
        if (self.pedidosTable.columnCount() < 6):
            self.pedidosTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.pedidosTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.pedidosTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.pedidosTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.pedidosTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.pedidosTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.pedidosTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.pedidosTable.setObjectName(u"pedidosTable")
        self.pedidosTable.setGeometry(QRect(180, 250, 601, 261))
        self.pedidosTable.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btnSalir = QPushButton(self.centralwidget)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(580, 540, 93, 28))
        self.btnSalir.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 1, 13);")
        self.fechapedidoInput = QLineEdit(self.centralwidget)
        self.fechapedidoInput.setObjectName(u"fechapedidoInput")
        self.fechapedidoInput.setGeometry(QRect(310, 150, 171, 22))
        self.fechapedidoInput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.idclienteInput = QLineEdit(self.centralwidget)
        self.idclienteInput.setObjectName(u"idclienteInput")
        self.idclienteInput.setGeometry(QRect(310, 210, 171, 22))
        self.idclienteInput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 30, 591, 51))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(720, 10, 181, 131))
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-image: url(:/cct/Imagen de WhatsApp 2024-08-13 a las 20.52.17_e647f5ba.jpg);")
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(190, 540, 93, 28))
        self.addButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 1, 13);")
        self.nombreInput = QLineEdit(self.centralwidget)
        self.nombreInput.setObjectName(u"nombreInput")
        self.nombreInput.setGeometry(QRect(560, 150, 141, 22))
        self.nombreInput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(570, 120, 55, 20))
        self.label_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(570, 180, 55, 20))
        self.label_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cantidadInput = QLineEdit(self.centralwidget)
        self.cantidadInput.setObjectName(u"cantidadInput")
        self.cantidadInput.setGeometry(QRect(560, 210, 141, 22))
        self.cantidadInput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(450, 540, 93, 28))
        self.deleteButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 1, 13);")
        self.reporte = QPushButton(self.centralwidget)
        self.reporte.setObjectName(u"reporte")
        self.reporte.setGeometry(QRect(320, 540, 93, 28))
        self.reporte.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 1, 13);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Id Pedido", None))
        self.idpedidoInput.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Id Producto", None))
        self.idproductoInput.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Id cliente", None))
        ___qtablewidgetitem = self.pedidosTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"idpedido", None));
        ___qtablewidgetitem1 = self.pedidosTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"fechapedido ", None));
        ___qtablewidgetitem2 = self.pedidosTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"idcliente", None));
        ___qtablewidgetitem3 = self.pedidosTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"idproducto", None));
        ___qtablewidgetitem4 = self.pedidosTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"cantidad", None));
        ___qtablewidgetitem5 = self.pedidosTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"nombre", None));
        self.btnSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Pedidos", None))
        self.label_8.setText("")
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.nombreInput.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.cantidadInput.setText("")
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.reporte.setText(QCoreApplication.translate("MainWindow", u"Reporte", None))
    # retranslateUi

