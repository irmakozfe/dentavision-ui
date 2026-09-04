from core.models import Tooth
from ui.selected_tooth_badge import SelectedToothBadge
 
 
class ToothInfoController:

    def __init__(self, ui):
        self._empty_widgets = [ui.toothIconLabel, ui.noToothSelected, ui.selectATooth]
 
        self.badge = SelectedToothBadge(ui.leftPanel)
        self.badge.setGeometry(10, 55, 260, 61)
        self.badge.hide()
 
        self.clear()
 
    def show_tooth(self, tooth: Tooth) -> None:
        for widget in self._empty_widgets:
            widget.hide()
        self.badge.set_tooth(tooth)
        self.badge.adjustSize()
        self.badge.show()
 
    def clear(self) -> None:
        self.badge.hide()
        for widget in self._empty_widgets:
            widget.show()
 


