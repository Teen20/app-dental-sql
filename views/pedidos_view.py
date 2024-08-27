from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class Pedidos_View(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/pedidos.ui',self)