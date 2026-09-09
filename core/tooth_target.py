from core.models import HeadPosition
from core.teeth_data import TOOTH_OFFSETS_MM, TOOTH_DEPTH_OFFSETS_MM

def compute_tooth_target(tooth_number, head_position):
    dx, dy = TOOTH_OFFSETS_MM[tooth_number]
    dz = TOOTH_DEPTH_OFFSETS_MM[tooth_number]
    x = head_position.x + dx
    y = head_position.y + dy
    z = head_position.z + dz
    return (x, y, z)