import sys
from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow  
from ui.mainwindow_ui import Ui_MainWindow
from controllers.tooth_chart_controller import ToothChartController
from controllers.tooth_info_controller import ToothInfoController
from controllers.camera_controller import CameraController
from controllers.tooth_target_controller import ToothTargetController
from core.models import HeadPosition


class ControlPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # rightBottomPanel Status temporary hidden
        self.ui.stabilizationSuccessfulLabel.hide()
        self.ui.scanningLabel.hide()
        self.ui.headIsNotStabilizedLabel.hide()

        self.ui.startButton.clicked.connect(self.on_start_clicked)

        self.stabilization_error_label = QLabel("STABILIZATION ERROR", self.ui.centerPanel)
        self.stabilization_error_label.setAlignment(Qt.AlignCenter)
        self.stabilization_error_label.setStyleSheet("""
            QLabel {
                background-color: #C83C3C;
                color: white;
                font-weight: bold;
                font-size: 13px;
                border-radius: 8px;
                padding: 6px 14px;
            }
        """)
        self.stabilization_error_label.adjustSize()
        self.stabilization_error_label.move(
            (self.ui.centerPanel.width() - self.stabilization_error_label.width()) // 2, 10
        )
        self.stabilization_error_label.hide()

        self.head_position = HeadPosition()
        self.tooth_info = ToothInfoController(self.ui)
        self.tooth_target = ToothTargetController(self.ui, self.head_position)
        self.tooth_chart = ToothChartController(
            mouth_frame=self.ui.mouthFrame,
            on_tooth_selected=self.on_tooth_selected,
            can_select=self.can_select_tooth,
        )

        self.camera = CameraController(
            parent_frame=self.ui.rightTopPanel,
            header_label=self.ui.headPositionLabel,
            face_status_label=self.ui.faceDetectedLabel,
            stabilization_successful_label=self.ui.stabilizationSuccessfulLabel,
            head_not_stabilized_label=self.ui.headIsNotStabilizedLabel,
            scanning_label=self.ui.scanningLabel,
            on_tracking_lost=self.on_tracking_lost,          
            on_tracking_restored=self.on_tracking_restored,  
        )
        self.camera.start()

    def on_start_clicked(self):
        print("Clicked startButton")
        self.camera.start_scanning()

    def can_select_tooth(self) -> bool:
        return self.camera.check_ready("select tooth")

    def on_tooth_selected(self, tooth):
        print(f"Tooth {tooth.number} is selected")
        self.tooth_info.show_tooth(tooth)
        self.tooth_target.show_target_for(tooth)

    def on_tracking_lost(self):

        print("Tracking lost: no tooth selection")
        self.tooth_chart.clear_selection()
        self.tooth_info.clear()
        self.tooth_target.clear()
        self.stabilization_error_label.show()
        self.ui.startButton.setEnabled(False)

    def on_tracking_restored(self):
        self.stabilization_error_label.hide()
        self.ui.startButton.setEnabled(True)

    def closeEvent(self, event):
        self.camera.stop()
        return super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ControlPanel()
    window.show()
    sys.exit(app.exec())