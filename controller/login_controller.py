from PyQt5.QtWidgets import QMessageBox
from views.login_view import LoginView
from model.database import get_connection
from controller.ingreso_controller import IngresoController
from controller.menu_controller import MenuWindow
class LoginController:
    def __init__(self):
        self.view = LoginView()
        self.view.loginButton.clicked.connect(self.login)
        self.view.cancelButton.clicked.connect(self.cancel)

    def cancel(self):
        self.view.close()

    def login(self):
        username = self.view.txtUsuario.text()
        password = self.view.txtContrasea.text()
        if self.authenticate(username, password):
            QMessageBox.information(self.view, "Login", "Login Successful")
            self.view.close()  
            self.show_menu()  


        else:
            QMessageBox.warning(self.view, "Login", "Invalid credentials")

    def authenticate(self, username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Username,Password FROM Users WHERE Username=? AND Password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        return user is not None
    
    def show_menu(self):
        self.menu_controller=MenuWindow()
        self.menu_controller.view.show()