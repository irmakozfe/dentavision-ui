from enum import Enum,auto 

class Jaw(Enum):
    MAXILLA = "maxilla"
    MANDIBULA = "mandibula"

class ScanStage(Enum):
    IDLE = auto() #1
    FACE_DETECTED= auto() #2 
    STABILIZED= auto() #3
    JOINTS_MOVING= auto() #4
    SCANNING_STARTED= auto() #5