import cv2


class Camera:
    def __init__(self, index: int = 0):
        self.capture = cv2.VideoCapture(index, cv2.CAP_AVFOUNDATION)
        if not self.capture.isOpened():
            raise RuntimeError("Kamera açılamadı. İzinleri kontrol et.")

    def read_frame(self):
        success, frame = self.capture.read()
        if not success:
            return None
        return frame

    def release(self):
        self.capture.release()