import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.mainwindow_ui import Ui_MainWindow
from controllers.tooth_chart_controller import ToothChartController
from controllers.tooth_info_controller import ToothInfoController
 
class ControlPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
        self.ui.startButton.clicked.connect(self.on_start_clicked)

        self.tooth_info = ToothInfoController(self.ui)
        self.tooth_chart = ToothChartController(
            mouth_frame= self.ui.mouthFrame,
            on_tooth_selected= self.on_tooth_selected
        ) 

    def on_start_clicked(self):
        print("Clicked startButton")

    def on_tooth_selected(self, tooth):
        print(f"Tooth {tooth.number} is selected")
        self.tooth_info.show_tooth(tooth)
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ControlPanel()
    window.show()
    sys.exit(app.exec())
 
