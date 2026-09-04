import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.mainwindow_ui import Ui_MainWindow
from controllers.tooth_chart_controller import ToothChartController
from controllers.tooth_info_controller import ToothInfoController
from controllers.camera_controller import CameraController

class ControlPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # rightBottomPanel - STATUS: temporary hidden
        self.ui.stabilizationSuccessfulLabel.hide()
        self.ui.scanningLabel.hide()
        self.ui.headIsNotStabilizedLabel.hide()
 
        self.ui.startButton.clicked.connect(self.on_start_clicked)

        self.tooth_info = ToothInfoController(self.ui)
        self.tooth_chart = ToothChartController(
            mouth_frame= self.ui.mouthFrame,
            on_tooth_selected= self.on_tooth_selected
        ) 

        self.camera = CameraController(
            parent_frame= self.ui.rightTopPanel,
            header_label= self.ui.headPositionLabel,
            face_status_label= self.ui.faceDetectedLabel
        )
        self.camera.start()

    def on_start_clicked(self):
        print("Clicked startButton")

    def on_tooth_selected(self, tooth):
        print(f"Tooth {tooth.number} is selected")
        self.tooth_info.show_tooth(tooth)

    def closeEvent(self, event):
        self.camera.stop()
        return super().closeEvent(event)
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ControlPanel()
    window.show()
    sys.exit(app.exec())
 
