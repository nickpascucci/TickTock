#! /usr/bin/python

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtUiTools 

class TickTockWindow(QWidget):
    def __init__(self, parent):
        super(TickTockWindow, self).__init__(parent)
        
        # Get a loader for QT Designer forms, so we can build the main window UI
        # from it.
        loader = QtUiTools.QUiLoader() 
        main_ui_file = QFile("main.ui")
        main_ui_file.open(QFile.ReadOnly)

        self.resize(600, 400)
        self.setWindowTitle("TickTock")
        
        main_widget = loader.load(main_ui_file)
        layout = QVBoxLayout()
        layout.addWidget(main_widget)
        self.setLayout(layout)

        self.startButton = main_widget.startButton
        self.stopButton = main_widget.stopButton
        self.lcdNumber = main_widget.lcdNumber
        self.minutesSpinBox = main_widget.minutesSpinBox

        self.startButton.clicked.connect(self.start_timer)
        self.stopButton.clicked.connect(self.stop_timer)
        self.stopButton.setEnabled(False)
        self.lcdNumber.display("00:00")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeout)

        self.icon = QIcon("icon-32.png")
        self.setWindowIcon(self.icon)

        # Set warning and critical times for LCD color changes.
        self.warnTime = 3 * 60
        self.criticalTime = 1 * 60

    def start_timer(self):
        print "Timer started!"
        self.stopButton.setEnabled(True)
        self.startButton.setEnabled(False)
        self.minutesSpinBox.setEnabled(False)

        self.seconds_remaining = int(self.minutesSpinBox.value()) * 60
        self.lcdNumber.setProperty("criticalTime", "False")
        self.lcdNumber.setProperty("warnTime", "False")
        self.repolish_timer()

        self.timer.start(1000)
        self.display_time()
        
    def stop_timer(self):
        print "Timer stopped!"
        self.stopButton.setEnabled(False)
        self.startButton.setEnabled(True)
        self.minutesSpinBox.setEnabled(True)
        self.timer.stop()

    def timeout(self):
        self.seconds_remaining -= 1
        self.display_time()

    def repolish_timer(self):
        self.lcdNumber.style().unpolish(self.lcdNumber)
        self.lcdNumber.style().polish(self.lcdNumber)
            
    def display_time(self):
        if self.seconds_remaining == 0:
            self.stop_timer()
        elif self.seconds_remaining <= self.criticalTime:
            self.lcdNumber.setProperty("criticalTime", "True")
            self.repolish_timer()
        elif self.seconds_remaining <= self.warnTime:
            self.lcdNumber.setProperty("warnTime", "True")
            self.repolish_timer()

        time_string = "%02d:%02d" % (self.seconds_remaining / 60,
                                   self.seconds_remaining % 60)
        self.lcdNumber.display(time_string)
        
def main():
    app = QApplication(sys.argv)
    main_window = TickTockWindow(None)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
