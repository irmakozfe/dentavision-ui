#Tooth numbers (FDI notation) and names
import math
UPPER_TEETH = [18, 17, 16, 15, 14, 13, 12, 11, 21, 22, 23, 24, 25, 26, 27, 28]
LOWER_TEETH = [48, 47, 46, 45, 44, 43, 42, 41, 31, 32, 33, 34, 35, 36, 37, 38]
 
TOOTH_NAMES = {
    18: "Upper Right Third Molar", 17: "Upper Right Second Molar", 16: "Upper Right First Molar",
    15: "Upper Right Second Premolar", 14: "Upper Right First Premolar", 13: "Upper Right Canine",
    12: "Upper Right Lateral Incisor", 11: "Upper Right Central Incisor",
    21: "Upper Left Central Incisor", 22: "Upper Left Lateral Incisor", 23: "Upper Left Canine",
    24: "Upper Left First Premolar", 25: "Upper Left Second Premolar", 26: "Upper Left First Molar",
    27: "Upper Left Second Molar", 28: "Upper Left Third Molar",
    48: "Lower Right Third Molar", 47: "Lower Right Second Molar", 46: "Lower Right First Molar",
    45: "Lower Right Second Premolar", 44: "Lower Right First Premolar", 43: "Lower Right Canine",
    42: "Lower Right Lateral Incisor", 41: "Lower Right Central Incisor",
    31: "Lower Left Central Incisor", 32: "Lower Left Lateral Incisor", 33: "Lower Left Canine",
    34: "Lower Left First Premolar", 35: "Lower Left Second Premolar", 36: "Lower Left First Molar",
    37: "Lower Left Second Molar", 38: "Lower Left Third Molar",
}


ARCH_WIDTH_MM = 45.0   # left-right half-width of the arch at its widest tooth
ARCH_HEIGHT_MM = 8.0   # how far the curve rises/falls from the centerline

_UPPER_ANGLE_RANGE = (195,345)
_LOWER_ANGLE_RANGE = (165, 15)

def _arc_offsets(tooth_numbers: list[int], angle_range: tuple[float, float], y_sign: int) -> dict[int, tuple[float, float]]:
    start_angle, end_angle = angle_range
    count = len(tooth_numbers)
    offsets = {}
    for i, tooth_number in enumerate(tooth_numbers):
        angle_deg = start_angle + (end_angle - start_angle) * i / (count - 1)
        angle_rad = math.radians(angle_deg)
        dx = ARCH_WIDTH_MM * math.cos(angle_rad)
        dy = y_sign * ARCH_HEIGHT_MM * abs(math.sin(angle_rad))
        offsets[tooth_number] = (dx, dy)
    return offsets
 
 
TOOTH_OFFSETS_MM: dict[int, tuple[float, float]] = {
    **_arc_offsets(UPPER_TEETH, _UPPER_ANGLE_RANGE, y_sign=+1),
    **_arc_offsets(LOWER_TEETH, _LOWER_ANGLE_RANGE, y_sign=-1),
}
 




