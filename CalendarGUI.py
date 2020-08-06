"""This is the GUI class that when interact directly with user. User interactions include looking up available time
and request booking. """

# -----------------------------------------------------------------------------------------------------------------------
# Name:       CalendarGUI.py
# Purpose:    This is the patient GUI where patients look up available time slots and request booking.
# Author:     Yiding Han
# Created:    6/17/2020
# TODO:       Add functions
# Note:       Use PyQT to develop GUI later
# ---------

import os
from EventHandler import EventHandler
from PySide2.QtCore import QFile, Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QDialog, QPushButton, QCalendarWidget,QListWidget


class InfoWindow(QDialog):
    def __init__(self):
        super(InfoWindow, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "newWindow.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()
        #set popup window to be frameless, so users don't accidentally click on close
        self.setWindowFlag(Qt.FramelessWindowHint)
        #set popup window to stay on top of the main window when it is showing
        self.setWindowFlags(self.windowFlags()^Qt.WindowStaysOnTopHint)

class CalendarApp(QMainWindow):
    def __init__(self):
        self.eventHandler = EventHandler(self)
        super(CalendarApp, self).__init__()
        self.infoDialog = InfoWindow()
        self.load_ui()
        self.eventHandler.clickOnDate()

    #call when bookPushbotton is clicked
    def showInfoDialog(self):
        #set main window to disable when showing the popup window
        self.setEnabled(False)
        # show popup info window
        self.infoDialog.show()

    #Bindind the UI components to listener(eventhandler)
    def BindEventsHandler(self):

        btn = self.window.findChild(QPushButton, 'bookPushButton')
        btn.clicked.connect(self.eventHandler.bookPushButton_cliked)

        self.calWidget = self.window.findChild(QCalendarWidget, 'calendarWidget')
        self.calWidget.selectionChanged.connect(self.eventHandler.clickOnDate)
        self.QListWidget = self.window.findChild(QListWidget, 'listWidget')

        btn = self.infoDialog.findChild(QPushButton, 'sendButton')
        btn.clicked.connect(self.eventHandler.sendPushButton_clicked)

        btn = self.infoDialog.findChild(QPushButton, 'cancelButton')
        btn.clicked.connect(self.eventHandler.cancelPushButton_clicked)


    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "mainWindow.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file, self)
        ui_file.close()
        self.BindEventsHandler()
        self.window.show()

    def closeEvent(self, event):
        pass

'''if __name__ == "__main__":

    app = QApplication([])
    app.quitOnLastWindowClosed()
#    app.setQuitOnLastWindowClosed()
    mainWindow = CalendarApp()
    sys.exit(app.exec_())
'''