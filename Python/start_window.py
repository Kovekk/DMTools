from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from PyQt6 import uic
import sys

class StartWindow(QWidget):
    
    def __init__(self, qtstackedwidget):
        super().__init__()
        uic.loadUi("ui_files/DMTools_home.ui", self)
        widget_stack = qtstackedwidget

        self.start_btn.clicked.connect(lambda: self.change_page(widget_stack, 1))



    def change_page(self, widget, index_num):
        widget.setCurrentIndex(index_num)







