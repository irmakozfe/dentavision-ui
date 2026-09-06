from core.models import HeadPosition
from core.teeth_data import TOOTH_OFFSETS_MM
 
 
def compute_tooth_target(tooth_number: int, head_position: HeadPosition) -> tuple[float, float, float]:
    dx, dy = TOOTH_OFFSETS_MM[tooth_number]
 
    x = head_position.x + dx
    y = head_position.y + dy
    z = head_position.z  # depth comes from the head, not the tooth
 
    return (x, y, z)