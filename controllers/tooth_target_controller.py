from core.models import HeadPosition, Tooth
from core.tooth_target import compute_tooth_target
 
 
class ToothTargetController:
 
    def __init__(self, ui, head_position: HeadPosition):
        self.ui = ui
        self.head_position = head_position
 
    def show_target_for(self, tooth: Tooth) -> None:
        x, y, z = compute_tooth_target(tooth.number, self.head_position)
        self.ui.labelX.setText(f"{x:.1f}")
        self.ui.labelY.setText(f"{y:.1f}")
        self.ui.labelZ.setText(f"{z:.1f}")
 
    def clear(self) -> None:
        self.ui.labelX.setText("-")
        self.ui.labelY.setText("-")
        self.ui.labelZ.setText("-")
 


