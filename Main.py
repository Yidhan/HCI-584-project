'''This file is to run the program'''

from PySide2.QtWidgets import QApplication
from CalendarGUI import CalendarApp
import sys

app = QApplication([])
app.quitOnLastWindowClosed()
mainWindow = CalendarApp()
sys.exit(app.exec_())