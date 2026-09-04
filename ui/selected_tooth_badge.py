from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget

from core.models import Tooth


class SelectedToothBadge(QWidget):
 
    CIRCLE_SIZE = 61

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.number_label = QLabel(self)
        self.number_label.setFixedSize(self.CIRCLE_SIZE, self.CIRCLE_SIZE)
        self.number_label.setAlignment(Qt.AlignCenter)
        self.number_label.setStyleSheet(f"""
            QLabel {{
                background-color: #0E7772;
                color: white;
                border-radius: {self.CIRCLE_SIZE // 2}px;
                font-size: 24px;
                font-style: italic;
                font-weight: semi-bold;
            }}
        """)

        self.name_label = QLabel(self)
        self.name_label.setStyleSheet("""
            QLabel {
                color: #5C646A;
                font-style: italic;
                font-weight:semi-bold;
                font-size: 15px;
            }
        """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)
        layout.addWidget(self.number_label)
        layout.addWidget(self.name_label)
        layout.addStretch()

    def set_tooth(self, tooth: Tooth) -> None:
        self.number_label.setText(str(tooth.number))
        self.name_label.setText(tooth.name)

    def clear(self) -> None:
        self.number_label.setText("")
        self.name_label.setText("")