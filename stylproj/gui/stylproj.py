import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from stylproj_auto import Ui_MainWindow

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
