from __future__ import annotations

import cv2
import math
import mediapipe as mp
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap

from ui.rounded_video_label import RoundedVideoLabel
from vision.camera import Camera
from vision.face_tracker import FaceTracker
from ui.rounded_video_label import RoundedVideoLabel, RED_DOT_Y_AXIS


TEAL_RGB = (20, 70, 190)

MOUTH_LANDMARK_IDS = sorted({idx for pair in mp.solutions.face_mesh.FACEMESH_LIPS for idx in pair})
MOUTH_BOX_PADDING = 6

FACE_LINE_THICKNESS = 3
MOUTH_LINE_THICKNESS = 3

FACE_DETECTED_TEXT = "● FACE DETECTED"
FACE_NOT_FOUND_TEXT = "●  FACE NOT FOUND"

FACE_DETECTED_STYLE = "color: #11AC00; font-weight: 600; font-size: 11px;"
FACE_NOT_FOUND_STYLE = "color: #C83C3C; font-weight: 600; font-size: 11px;"

STABILIZATION_TOLERANCE_PX = 30

class CameraController:

    def __init__(
            self, 
            parent_frame,
            header_label, 
            face_status_label=None,
            stabilization_successful_label=None,
            head_not_stabilized_label=None, 
            scanning_label=None,
            interval_ms: int = 30
        ):
        self.video_label = RoundedVideoLabel(radius=14, parent=parent_frame)
        self._position_label(parent_frame, header_label)

        self.face_status_label = face_status_label
        self._face_detected_state: bool | None = None

        self.stabilization_label = stabilization_successful_label
        self.head_not_stabilized_label = head_not_stabilized_label
        self._stabilization_state: str | None = None 

        self.scanning_label= scanning_label
        self._scanning_active: bool = False

        self.camera: Camera | None = None
        self.tracker: FaceTracker | None = None

        self.timer = QTimer()
        self.timer.timeout.connect(self._update_frame)
        self.interval_ms = interval_ms

    def _position_label(self, parent_frame, header_label) -> None:
        margin = 10
        top = header_label.geometry().bottom() + margin
        self.video_label.setGeometry(
            margin,
            top,
            parent_frame.width() - 2 * margin,
            parent_frame.height() - top - margin,
        )
        self.video_label.show()

    @property
    def face_detected(self) -> bool:
        return bool(self._face_detected_state)

    @property
    def stabilized(self) -> bool:
        return self._stabilization_state == "stabilized" 

    def start_scanning(self) -> bool:
        if self.face_detected and self.stabilized:
            self._scanning_active = True
            if self.scanning_label is not None:
                self.scanning_label.show()
            return True

        if not self.face_detected:
            print("Can not start scanning: face not detected")
        if not self.stabilized:
            print("Can not start scanning: head is not stabilized")
        return False


    def _set_face_status(self, face_found: bool) -> None:
        if self.face_status_label is None or self._face_detected_state == face_found:
            return
        self._face_detected_state = face_found
        if face_found:
            self.face_status_label.setText(FACE_DETECTED_TEXT)
            self.face_status_label.setStyleSheet(FACE_DETECTED_STYLE)
        else:
            self.face_status_label.setText(FACE_NOT_FOUND_TEXT)
            self.face_status_label.setStyleSheet(FACE_NOT_FOUND_STYLE)

    def _set_stabilization_status(self, state:str) -> None:
        if self._stabilization_state == state:
            return
        self._stabilization_state = state

        if state == "stabilized":
            if self.stabilization_label is not None:
                self.stabilization_label.show()
            if self.head_not_stabilized_label is not None:
                self.head_not_stabilized_label.hide()
        elif state == "not_stabilized":
            if self.stabilization_label is not None:
                self.stabilization_label.hide()
            if self.head_not_stabilized_label is not None:
                self.head_not_stabilized_label.show()
        else:  # "hidden"
            if self.stabilization_label is not None:
                self.stabilization_label.hide()
            if self.head_not_stabilized_label is not None:
                self.head_not_stabilized_label.hide()       

    def start(self) -> None:
        if self.camera is not None:
            return
        self.camera = Camera()
        self.tracker = FaceTracker()
        self._set_face_status(False)
        self._set_stabilization_status("hidden")
        self.timer.start(self.interval_ms)

    def stop(self) -> None:
        self.timer.stop()
        if self.camera is not None:
            self.camera.release()
            self.camera = None
        self.tracker = None
        self.video_label.setPixmap(QPixmap())
        self.video_label.setText("Camera off")
        self._set_face_status(False)
        self._set_stabilization_status("hidden")

        if self._scanning_active:
            self._scanning_active = False
            if self.scanning_label is not None:
                self.scanning_label.hide()
            print("Scanning Paused")

    def _update_frame(self) -> None:
        frame = self.camera.read_frame()
        if frame is None:
            self.stop()
            return

        frame = cv2.flip(frame, 1)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape

        results = self.tracker.face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            self._set_face_status(True)

            landmarks = results.multi_face_landmarks[0]

            xs = [lm.x * w for lm in landmarks.landmark]
            ys = [lm.y * h for lm in landmarks.landmark]

            x_min, x_max = int(min(xs)), int(max(xs))
            y_min, y_max = int(min(ys)), int(max(ys))

            cv2.rectangle(rgb_frame, (x_min, y_min), (x_max, y_max), TEAL_RGB, FACE_LINE_THICKNESS)
            cv2.putText(rgb_frame, "FACE DETECTED", (x_min, y_min - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, TEAL_RGB, FACE_LINE_THICKNESS)

            mouth_xs = [landmarks.landmark[i].x * w for i in MOUTH_LANDMARK_IDS]
            mouth_ys = [landmarks.landmark[i].y * h for i in MOUTH_LANDMARK_IDS]

            mouth_x_min = max(0, int(min(mouth_xs)) - MOUTH_BOX_PADDING)
            mouth_x_max = min(w - 1, int(max(mouth_xs)) + MOUTH_BOX_PADDING)
            mouth_y_min = max(0, int(min(mouth_ys)) - MOUTH_BOX_PADDING)
            mouth_y_max = min(h - 1, int(max(mouth_ys)) + MOUTH_BOX_PADDING)

            cv2.rectangle(rgb_frame, (mouth_x_min, mouth_y_min), (mouth_x_max, mouth_y_max), TEAL_RGB, MOUTH_LINE_THICKNESS)
            cv2.putText(rgb_frame, "MOUTH", (mouth_x_min, mouth_y_min - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, TEAL_RGB, MOUTH_LINE_THICKNESS)

            mouth_mid_x = (mouth_x_min + mouth_x_max) // 2
            mouth_mid_y = (mouth_y_min + mouth_y_max) // 2

            target_x = w // 2
            target_y = int(h * RED_DOT_Y_AXIS)
            distance = math.hypot(mouth_mid_x - target_x, mouth_mid_y-target_y)

            if distance <= STABILIZATION_TOLERANCE_PX:
                self._set_stabilization_status("stabilized")
            else:
                self._set_stabilization_status("not_stabilized")  

        else:
            self._set_face_status(False)
            self._set_stabilization_status("hidden")
            cv2.putText(rgb_frame, "Face not found", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, TEAL_RGB, FACE_LINE_THICKNESS)


        if self._scanning_active and not (self.face_detected and self.stabilized):
            self._scanning_active = False
            if self.scanning_label is not None:
                self.scanning_label.hide()
            print("Scanning Paused")

        image = QImage(rgb_frame.data, w, h, ch * w, QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(image))