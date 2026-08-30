import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.mainwindow_ui import Ui_MainWindow
 
 
class ControlPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
        self.ui.startButton.clicked.connect(self.on_start_clicked)
 
    def on_start_clicked(self):
        print("Clicked startButton")
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ControlPanel()
    window.show()
    sys.exit(app.exec())
 
