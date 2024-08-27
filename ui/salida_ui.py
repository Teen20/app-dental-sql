# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salida.ui'
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
        self.txtcodPro = QLineEdit(self.centralwidget)
        self.txtcodPro.setObjectName(u"txtcodPro")
        self.txtcodPro.setGeometry(QRect(60, 150, 151, 22))
        self.txtcodPro.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 190, 131, 20))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txtDescripcion = QLineEdit(self.centralwidget)
        self.txtDescripcion.setObjectName(u"txtDescripcion")
        self.txtDescripcion.setGeometry(QRect(60, 210, 151, 22))
        self.txtDescripcion.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(420, 130, 55, 20))
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(410, 190, 55, 20))
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(110, 260, 751, 261))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btnSalir = QPushButton(self.centralwidget)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(820, 530, 93, 28))
        self.btnSalir.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 1, 13);")
        self.txtFecha = QLineEdit(self.centralwidget)
        self.txtFecha.setObjectName(u"txtFecha")
        self.txtFecha.setGeometry(QRect(410, 160, 113, 22))
        self.txtFecha.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txtCantidad = QLineEdit(self.centralwidget)
        self.txtCantidad.setObjectName(u"txtCantidad")
        self.txtCantidad.setGeometry(QRect(410, 220, 121, 22))
        self.txtCantidad.setStyleSheet(u"background-color: rgb(255, 255, 255);")
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
        self.btnSalir_2 = QPushButton(self.centralwidget)
        self.btnSalir_2.setObjectName(u"btnSalir_2")
        self.btnSalir_2.setGeometry(QRect(690, 530, 93, 28))
        self.btnSalir_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 1, 13);")
        self.txtFecha_2 = QLineEdit(self.centralwidget)
        self.txtFecha_2.setObjectName(u"txtFecha_2")
        self.txtFecha_2.setGeometry(QRect(570, 160, 113, 22))
        self.txtFecha_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(580, 130, 55, 20))
        self.label_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Codigo producto ", None))
        self.txtcodPro.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.txtDescripcion.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"cantidad", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"cantidad", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Precio ", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Stock", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Categoria ", None));
        self.btnSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Pedidos", None))
        self.label_8.setText("")
        self.btnSalir_2.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.txtFecha_2.setText(QCoreApplication.translate("MainWindow", u"Fecha_Salida", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
    # retranslateUi

