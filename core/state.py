#session-based info
from dataclasses import dataclass
from enums import ScanStage
from models import HeadPosition

@dataclass
class ScanStatus:
    stage: ScanStage = ScanStage.IDLE # stage burda bir attribute, type ScanStage, default deger IDLE

    @property
    def face_detected(self) -> bool:
        return self.stage.value >= ScanStage.FACE_DETECTED.value

    @property
    def stabilization_successful(self)-> bool:
        return self.stage.value >= ScanStage.STABILIZED.value

    @property
    def scanning_started(self) -> bool:
        return self.stage.value >= ScanStage.SCANNING_STARTED.value
    
@dataclass
class HeadStabilityTracker:
    threshold: float = 2.0
    required_stable_frames: int = 30
    last_position: HeadPosition | None = None
    stable_frame_count: int = 0

    def update(self, new_position: HeadPosition) -> bool:
        if self.last_position is None:
            self.last_position = new_position
            self.stable_frame_count = 0
            return False

        distance = self._distance(self.last_position, new_position)

        if distance <= self.threshold:
            self.stable_frame_count += 1
        else:
            self.stable_frame_count = 0

        self.last_position = new_position
        return self.stable_frame_count >= self.required_stable_frames

    def _distance(self, a: HeadPosition, b: HeadPosition) -> float:
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2) ** 0.5