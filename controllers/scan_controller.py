from vision.camera import Camera
from vision.face_tracker import FaceTracker
from core.state import HeadStabilityTracker

camera = Camera()
tracker_cv = FaceTracker()
stability = HeadStabilityTracker()

def on_frame_update():
    frame = camera.read_frame()
    if frame is None:
        return

    position = tracker_cv.detect(frame)
    is_stable = stability.update(position)

    if is_stable:
        scan_status.advance_to(ScanStage.STABILIZED)