import mediapipe as mp 
from core.models import HeadPosition

class FaceTracker: 
    def __init__(self):
        self.face_mesh= mp.solutions.face_mesh.FaceMesh(
            static_image_mode = False,
            max_num_faces=1
        )

    def detect(self,frame)->HeadPosition:
        results = self.face_mesh.process(frame)
        if not results.multi_face_landmarks:
            return HeadPosition(detected=False)

        landmarks = results.multi_face_landmarks[0]
        nose_tip = landmarks.landmark[1]

        return HeadPosition(
            detected=True,
            x=nose_tip.x,
            y=nose_tip.y,
            z=nose_tip.z
        )
    
