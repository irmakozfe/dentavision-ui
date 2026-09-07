"""A transparent, circular joystick for jogging X/Y motion.

Drag the knob anywhere inside the circular track; while dragging it
reports a normalized (x, y) in [-1, 1] via on_move(x, y), and snaps
back to (0, 0) on release — spring-loaded, like a real jog joystick,
not a position you set once and leave.
"""

from __future__ import annotations

import math

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPainter, QPen, QBrush, QColor
from PySide6.QtWidgets import QWidget


class JoystickWidget(QWidget):
    KNOB_RADIUS = 15
    TRACK_COLOR = "#118983"

    def __init__(self, diameter: int = 120, on_move=None, parent=None):
        super().__init__(parent)
        self.diameter = diameter
        self.on_move = on_move
        self._knob_offset = QPointF(0, 0)  
        self._dragging = False

        self.setFixedSize(diameter, diameter)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background: transparent;")

    def _center(self) -> QPointF:
        return QPointF(self.width() / 2, self.height() / 2)

    def _max_offset(self) -> float:
        return self.diameter / 2 - self.KNOB_RADIUS

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        track_rect = self.rect().adjusted(2, 2, -2, -2)
        painter.setPen(QPen(QColor(self.TRACK_COLOR), 2))
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(track_rect)

        knob_center = self._center() + self._knob_offset
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(QColor(self.TRACK_COLOR)))
        painter.drawEllipse(knob_center, self.KNOB_RADIUS, self.KNOB_RADIUS)

    def _update_from_mouse(self, pos: QPointF) -> None:
        center = self._center()
        offset = QPointF(pos.x() - center.x(), pos.y() - center.y())

        max_offset = self._max_offset()
        distance = math.hypot(offset.x(), offset.y())
        if distance > max_offset:
            scale = max_offset / distance
            offset = QPointF(offset.x() * scale, offset.y() * scale)

        self._knob_offset = offset
        self.update()

        if self.on_move is not None:
            x = offset.x() / max_offset
            y = -offset.y() / max_offset 
            self.on_move(x, y)

    def mousePressEvent(self, event):
        self._dragging = True
        self._update_from_mouse(event.position())

    def mouseMoveEvent(self, event):
        if self._dragging:
            self._update_from_mouse(event.position())

    def mouseReleaseEvent(self, event):
        self._dragging = False
        self._knob_offset = QPointF(0, 0)
        self.update()
        if self.on_move is not None:
            self.on_move(0.0, 0.0)