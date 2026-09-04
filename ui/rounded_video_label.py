from __future__ import annotations

from PySide6.QtCore import QRectF, Qt
from PySide6.QtGui import QColor, QPainter, QPainterPath
from PySide6.QtWidgets import QLabel, QWidget

RED_RGB = (200, 60, 60)

FIXED_DOT_RADIUS = 1.5
FIXED_DOT_Y_RATIO = 0.60  

class RoundedVideoLabel(QLabel):

    def __init__(self, radius: int = 14, parent: QWidget | None = None):
        super().__init__(parent)
        self.radius = radius
        self.setAlignment(Qt.AlignCenter)

        self.setStyleSheet(f"""
            QLabel {{
                background-color: #1a1a1a;
                border-radius: {radius}px;
                color: #9aa5b1;
            }}
        """)
        self.setText("Camera off")

    def paintEvent(self, event):
        pixmap = self.pixmap()
        if pixmap is None or pixmap.isNull():
            super().paintEvent(event)
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), self.radius, self.radius)
        painter.setClipPath(path)

        scaled = pixmap.scaled(
            self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
        )
        x = (self.width() - scaled.width()) // 2
        y = (self.height() - scaled.height()) // 2
        painter.drawPixmap(x, y, scaled)

        dot_x = self.width() // 2
        dot_y = int(self.height() * FIXED_DOT_Y_RATIO)

        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(*RED_RGB))
        painter.drawEllipse(
            dot_x - FIXED_DOT_RADIUS,
            dot_y - FIXED_DOT_RADIUS,
            FIXED_DOT_RADIUS * 2,
            FIXED_DOT_RADIUS * 2,
        )