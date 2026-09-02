import math
from PySide6.QtWidgets import QPushButton
 
 
class ToothChartController:
 
    UPPER_TEETH = [18, 17, 16, 15, 14, 13, 12, 11, 21, 22, 23, 24, 25, 26, 27, 28]
    LOWER_TEETH = [48, 47, 46, 45, 44, 43, 42, 41, 31, 32, 33, 34, 35, 36, 37, 38]
 
    def __init__(self, mouth_frame, on_tooth_selected=None):
        self.mouth_frame = mouth_frame
        self.on_tooth_selected = on_tooth_selected
        self.tooth_buttons = {}
        self.selected_tooth = None
 
        self._create_chart()
 
    def _create_chart(self):
        width = self.mouth_frame.width()
        height = self.mouth_frame.height()
 
        center_x = width / 2
        center_y = height / 2
        radius_x = width / 2 - 30
        radius_y = height / 2 - 30
        button_size = 34

        self._place_teeth_on_arc(
            self.UPPER_TEETH, center_x, center_y,
            radius_x, radius_y, button_size,
            start_angle=195, end_angle=345
        )
 
        self._place_teeth_on_arc(
            self.LOWER_TEETH, center_x, center_y,
            radius_x, radius_y, button_size,
            start_angle=165, end_angle=15
        )
 
    def _place_teeth_on_arc(self, tooth_numbers, cx, cy, rx, ry, size,
                              start_angle, end_angle):
        count = len(tooth_numbers)
        for i, tooth_num in enumerate(tooth_numbers):
            angle_deg = start_angle + (end_angle - start_angle) * i / (count - 1)
            angle_rad = math.radians(angle_deg)
 
            x = cx + rx * math.cos(angle_rad) - size / 2
            y = cy + ry * math.sin(angle_rad) - size / 2
 
            button = QPushButton(str(tooth_num), self.mouth_frame)
            button.setGeometry(int(x), int(y), size, size)
            button.setStyleSheet(self._normal_style())
            button.clicked.connect(lambda checked, n=tooth_num: self._handle_click(n))
            button.show()
 
            self.tooth_buttons[tooth_num] = button
 
    def _handle_click(self, tooth_number):

        if self.selected_tooth is not None:
            prev_btn = self.tooth_buttons[self.selected_tooth]
            prev_btn.setStyleSheet(self._normal_style())
 

        self.selected_tooth = tooth_number
        selected_btn = self.tooth_buttons[tooth_number]
        selected_btn.setStyleSheet(self._selected_style())
 
        if self.on_tooth_selected:
            self.on_tooth_selected(tooth_number)
 
    @staticmethod
    def _normal_style():
        return """
            QPushButton {
                border: 2px solid #118983;
                border-radius: 17px;
                background-color: white;
                color: #118983;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e8f5f0;
            }
        """
 
    @staticmethod
    def _selected_style():
        return """
            QPushButton {
                border: 2px solid #118983;
                border-radius: 17px;
                background-color: #118983;
                color: white;
                font-weight: bold;
            }
        """
 
