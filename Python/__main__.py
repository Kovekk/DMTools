import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import QtWidgets
from start_window import StartWindow
from pc_window import PcWindow

def main():
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    startWindow = StartWindow(widget)
    pcWindow = PcWindow(widget)
    widget.addWidget(startWindow)
    widget.addWidget(pcWindow)
    widget.setGeometry(-1300, 200, 764, 483)
    widget.show()
    sys.exit(app.exec())



if __name__ == "__main__":
    main()