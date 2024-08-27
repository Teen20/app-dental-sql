import sys
from PyQt5.QtWidgets import QApplication
from controller.login_controller import LoginController

app =QApplication(sys.argv)

login_controller= LoginController()
login_controller.view.show()
sys.exit(app.exec_())