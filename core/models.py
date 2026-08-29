from dataclasses import dataclass, field

@dataclass
class Tooth:
    number:int
    name:str
    x:float
    y:float
    z:float

    def move_x(self,amount):
        self.x += amount

    def move_y(self,amount):
        self.y += amount

    def move_z(self,amount):
        self.z += amount    

    def position(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)
        

@dataclass
class Joint:
     name:str
     angle:float
     min_angle: float = -180.0
     max_angle: float = 180.0

     def set_angle(self, value:float):
        self.angle = max(self.min_angle, min(self.max_angle, value))

     def increment(self, step:float):
         self.set_angle(self.angle + step)

     def decrement(self, step:float):
         self.set_angle(self.angle - step)


@dataclass
class RobotArm: 
    joints: list[Joint] = field(default_factory=lambda: [
        Joint(name=f"J{i}" ) for i in range(1,7)
    ])

    def get_joint(self, name: str) -> Joint:
        for j in self.joints:
            if j.name == name:
                return j
        raise ValueError(f"Joint not found: {name}")

@dataclass
class DentalArch:
    teeth: dict[int, Tooth] = field(default_factory= dict)

    def get_tooth(self,number:int) -> Tooth:
        if number not in self.teeth:
            raise KeyError(f"Invalid tooth number: {number}")
        return self.teeth[number]

    def add_tooth(self, tooth:Tooth):
        self.teeth[tooth.number] = tooth

@dataclass
class HeadPosition:
    detected: bool = False
    x: float = 0.0 
    y: float = 0.0
    z: float = 0.0