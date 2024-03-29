from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from PyQt6 import uic
import sys

class PcWindow(QWidget):

    def __init__(self, qtstackedwidget):
        super().__init__()
        uic.loadUi("ui_files/DMTools_pc.ui", self)
        widget_stack = qtstackedwidget
        # campaign_info = campaign_json

        self.vault_menu_btn.clicked.connect(lambda: self.change_page(widget_stack, 0))
        self.npc_menu_btn.clicked.connect(lambda: self.change_page(widget_stack, 2))

    def change_page(self, widget, index_num):
        widget.setCurrentIndex(index_num)
