
from PySide2.QtWidgets import QApplication
from CalendarGUI import CalendarApp
import sys

app = QApplication([])
app.quitOnLastWindowClosed()
#app.setQuitOnLastWindowClosed()
mainWindow = CalendarApp()
sys.exit(app.exec_())