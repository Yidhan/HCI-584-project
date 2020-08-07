''' The module contains the GUI classes that interact directly with user.
This is the patient GUI where patients look up available time slots and request booking.'''

import os
from EventHandler import EventHandler
from PySide2.QtCore import QFile, Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QDialog, QPushButton, QCalendarWidget,QListWidget


class InfoWindow(QDialog):
    '''This class is the infoWindow class, which contains the pop-up window GUI,
     it appears when the user click on Book button on MainWindow. It will ask the users to fill in their personal info for booking
     This class inherited QDialog class'''
    def __init__(self):
        '''This function calls the parents class and load newWidow.ui


        Args:
            none

        Returns:
            none
        '''
        super(InfoWindow, self).__init__()
        self.load_ui()

    def load_ui(self):
        '''Load the newWindow.ui file and show it on screen.

        Args:
            none

        Returns:
            none

        '''
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
    '''This class contains the CalendarApp class(main window), it inherits the QMainWindow class in Pyside2'''
    def __init__(self):
        ''' This function calls parents class, initialize infoWindow, load main window UI,
        and call the clickOnDate function in eventHandler to get today's event list upon opening the GUI

        Args:
            none

        Returns:
            none
        '''
        self.eventHandler = EventHandler(self)
        super(CalendarApp, self).__init__()
        self.infoDialog = InfoWindow()
        self.load_ui()
        self.eventHandler.clickOnDate()

    def showInfoDialog(self):
        '''Shows the pop-up infoWindow when the called (upon bookPushbutton is clicked)

        Args:
            none

        Returns:
            none

        '''
        self.setEnabled(False) #set main window to disable when showing the popup window
        self.infoDialog.show() # show popup info window


    #Bindind the UI components to listener(eventhandler)
    def BindEventsHandler(self):
        '''Binds the UI components to its listener - functions in EventHandler class

        Args:
            none

        Returns:
            none

        '''
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
        '''Load the mainWindow.ui file and show it on screen.

        Args:
            none

        Returns:
            none

        '''
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "mainWindow.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file, self)
        ui_file.close()
        self.BindEventsHandler()
        self.window.show()


