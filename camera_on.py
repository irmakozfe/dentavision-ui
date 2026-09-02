import cv2
from vision.camera import Camera
from vision.face_tracker import FaceTracker
 
camera = Camera()
tracker = FaceTracker()
 
while True:
    frame = camera.read_frame()
    if frame is None:
        break
 
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = tracker.face_mesh.process(rgb_frame)
 
    if results.multi_face_landmarks:
        h, w, _ = frame.shape
        landmarks = results.multi_face_landmarks[0]
 
        xs = [lm.x * w for lm in landmarks.landmark]
        ys = [lm.y * h for lm in landmarks.landmark]
 
        x_min, x_max = int(min(xs)), int(max(xs))
        y_min, y_max = int(min(ys)), int(max(ys))
 
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
        cv2.putText(frame, "FACE DETECTED", (x_min, y_min - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    else:
        cv2.putText(frame, "Face not found", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
 
    cv2.imshow("DentaVision Cam", frame)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
camera.release()
cv2.destroyAllWindows()