import math
from PySide6.QtWidgets import QPushButton
from core.models import Tooth
from core.teeth_data import UPPER_TEETH, LOWER_TEETH, TOOTH_NAMES
 
class ToothChartController:
 
    def __init__(self, mouth_frame, on_tooth_selected=None):
        self.mouth_frame = mouth_frame
        self.on_tooth_selected = on_tooth_selected
        self.teeth = {
            number: Tooth(number=number, name=name, x=0.0, y=0.0, z=0.0)
            for number, name in TOOTH_NAMES.items()
        }
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
            UPPER_TEETH, center_x, center_y,
            radius_x, radius_y, button_size,
            start_angle=195, end_angle=345
        )
 
        self._place_teeth_on_arc(
            LOWER_TEETH, center_x, center_y,
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
            prev_btn = self.tooth_buttons[self.selected_tooth.number]
            prev_btn.setStyleSheet(self._normal_style())
 

        tooth = self.teeth[tooth_number]
        self.selected_tooth = tooth
        selected_btn = self.tooth_buttons[tooth_number]
        selected_btn.setStyleSheet(self._selected_style())
 
        if self.on_tooth_selected:
            self.on_tooth_selected(tooth)
 
    @staticmethod
    def _normal_style():
        return """
            QPushButton {
                border: 2px solid #0E7772;
                border-radius: 17px;
                background-color: white;
                color: #0E7772;
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
                border: 2px solid #0E7772;
                border-radius: 17px;
                background-color: #0E7772;
                color: white;
                font-weight: bold;
            }
        """
 
