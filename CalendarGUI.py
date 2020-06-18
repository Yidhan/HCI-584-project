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
import sys
import os
from EventHandler import EventHandler
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QCalendarWidget,QListWidget


class CalendarApp(QMainWindow):
    def __init__(self):
        self.eventHandler = EventHandler()
        super(CalendarApp, self).__init__()
        self.load_ui()

    def BindEventsHandler(self):
        btn = self.window.findChild(QPushButton, 'refreshPushButton')
        btn.clicked.connect(self.eventHandler.refreshPushButton_clicked)

        btn = self.window.findChild(QPushButton, 'bookPushButton')
        btn.clicked.connect(self.eventHandler.bookPushButton_cliked)

        self.calWidget = self.window.findChild(QCalendarWidget, 'calendarWidget')
        self.calWidget.selectedDate().connect(self.eventHandler.clickOnDate)

        self.QListWidget = self.window.findchild(QListWidget, 'listWidget')
        self.QListWidget.connect(self.eventHandler.clickOnDate)


    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file, self)
        ui_file.close()
        self.BindEventsHandler()
        self.window.show()


if __name__ == "__main__":
    app = QApplication([])
    widget = CalendarApp()
    sys.exit(app.exec_())
