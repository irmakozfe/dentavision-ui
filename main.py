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
            face_status_label= self.ui.faceDetectedLabel,
            stabilization_successful_label = self.ui.stabilizationSuccessfulLabel,
            head_not_stabilized_label = self.ui.headIsNotStabilizedLabel,
            scanning_label = self.ui.scanningLabel
        )
        self.camera.start()

    def on_start_clicked(self):
        self.camera.start_scanning() 
        print("Clicked startButton")

        if self.camera.face_detected and self.camera.stabilized:
            self.ui.scanningLabel.show()
            return

        if not self.camera.face_detected:
            print("FACE NOT DETECTED")

        if self.camera.face_detected and not self.camera.stabilized:
            print("HEAD IS NOT STABILIZED") 


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
 
