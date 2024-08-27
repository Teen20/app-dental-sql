from PyQt5.QtWidgets import QWidget, QMessageBox, QMainWindow
from views.main_ui import main
#from views.product_management_view import ProductManagementView
#
#menu
from controller.ingreso_controller import IngresoController
from controller.pedidos_controller import PedidosController
from views.login_view import LoginView
from model.database import get_connection

class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = main()
        self.view.ingresarButton.clicked.connect(self.ingresar)
        self.view.pedidosButton.clicked.connect(self.pedidos)
        self.view.logoatButton.clicked.connect(self.logoat)

    def ingresar(self):
    
        self.show_product_management_view()   

    def pedidos(self):
       
        self.show_pedidos_view()


    def show_pedidos_view(self):
        self.pedidoscontroller = PedidosController()
        self.pedidoscontroller.view.show()
   
    def show_product_management_view(self):
        self.product_controller = IngresoController()
        self.product_controller.view.show()


    def show_menu(self):
        self.menu_controller = MenuWindow()
        self.menu_controller.view.show()
        self.close()
    
    def logoat(self):
        self.view.close()
        #self.close() 
        #self.show_login()  

    def show_login(self):
        self.login_view = LoginView()
        self.login_view.loginButton.clicked.connect(self.login)
        self.login_view.cancelButton.clicked.connect(self.cancel)
        self.login_view.show() 

    def cancel(self):
        self.login_view.close()

    def login(self):
        username = self.login_view.txtUsuario.text()
        password = self.login_view.txtContrasea.text()
        if self.authenticate(username, password):
            QMessageBox.information(self.login_view, "Login", "Login Successful")
            self.login_view.close()  
            self.show_menu()  
        else:
            QMessageBox.warning(self.login_view, "Login", "Invalid credentials")

    def authenticate(self, username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Username, Password FROM Users WHERE Username=? AND Password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        return user is not None


