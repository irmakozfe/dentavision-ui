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
from vision.head_pose import estimate_head_position, estimate_head_orientation


TEAL_RGB = (20, 70, 190)

MOUTH_LANDMARK_IDS = sorted({idx for pair in mp.solutions.face_mesh.FACEMESH_LIPS for idx in pair})
MOUTH_BOX_PADDING = 6

MOUTH_LEFT_CORNER_IDX = 61
MOUTH_RIGHT_CORNER_IDX = 291

FACE_LINE_THICKNESS = 3
MOUTH_LINE_THICKNESS = 3

FACE_DETECTED_TEXT = "● FACE DETECTED"
FACE_NOT_FOUND_TEXT = "●  FACE NOT FOUND"

FACE_DETECTED_STYLE = "color: #11AC00; font-weight: 600; font-size: 11px;"
FACE_NOT_FOUND_STYLE = "color: #C83C3C; font-weight: 600; font-size: 11px;"

STABILIZATION_TOLERANCE_PX = 15

CM_PER_PIXEL = 0.025
MM_PER_PIXEL = CM_PER_PIXEL * 10

class CameraController:

    def __init__(
            self,
            parent_frame,
            header_label,
            face_status_label=None,
            stabilization_successful_label=None,
            head_not_stabilized_label=None,
            scanning_label=None,
            on_tracking_lost=None,
            on_tracking_restored=None,
            head_position=None,
            on_head_position_updated=None,
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

        self.on_tracking_lost = on_tracking_lost
        self.on_tracking_restored = on_tracking_restored
        self._selection_ok_state: bool | None = None

        self.head_position = head_position
        self.on_head_position_updated = on_head_position_updated

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

    def check_ready(self, action: str) -> bool:
        if not self.face_detected:
            print(f"Cannot {action}: face not detected")
            return False
        if not self.stabilized:
            print(f"Cannot {action}: head not stabilized")
            return False
        return True

    def start_scanning(self) -> bool:
        if not self.check_ready("start scanning"):
            return False
        self._scanning_active = True
        if self.scanning_label is not None:
            self.scanning_label.show()
        return True

    def pause_scanning(self) -> None:
        self._scanning_active = False


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
        else:
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

            mouth_width_px = mouth_x_max - mouth_x_min

            if self.head_position is not None and mouth_width_px > 0:
                mouth_left_x = landmarks.landmark[MOUTH_LEFT_CORNER_IDX].x * w
                mouth_left_y = landmarks.landmark[MOUTH_LEFT_CORNER_IDX].y * h
                mouth_right_x = landmarks.landmark[MOUTH_RIGHT_CORNER_IDX].x * w
                mouth_right_y = landmarks.landmark[MOUTH_RIGHT_CORNER_IDX].y * h

                x_mm, y_mm = estimate_head_position(
                    mouth_mid_x, mouth_mid_y, target_x, target_y, MM_PER_PIXEL
                )
                rx, ry, rz = estimate_head_orientation(
                    mouth_left_x, mouth_left_y, mouth_right_x, mouth_right_y,
                    mouth_mid_x, mouth_mid_y, x_min, x_max, y_min, y_max,
                )

                self.head_position.detected = True
                self.head_position.x = x_mm
                self.head_position.y = y_mm
                self.head_position.rx = rx
                self.head_position.ry = ry
                self.head_position.rz = rz

                if self.on_head_position_updated is not None:
                    self.on_head_position_updated()

        else:
            self._set_face_status(False)
            self._set_stabilization_status("hidden")
            if self.head_position is not None:
                self.head_position.detected = False
            cv2.putText(rgb_frame, "Face not found", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, TEAL_RGB, FACE_LINE_THICKNESS)


        if self._scanning_active and not (self.face_detected and self.stabilized):
            self._scanning_active = False
            if self.scanning_label is not None:
                self.scanning_label.hide()
            print("Scanning Paused")

        selection_ok = self.face_detected and self.stabilized
        if self._selection_ok_state is not None:
            if self._selection_ok_state and not selection_ok:
                if self.on_tracking_lost is not None:
                    self.on_tracking_lost()
            elif not self._selection_ok_state and selection_ok:
                if self.on_tracking_restored is not None:
                    self.on_tracking_restored()
        self._selection_ok_state = selection_ok

        image = QImage(rgb_frame.data, w, h, ch * w, QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(image))