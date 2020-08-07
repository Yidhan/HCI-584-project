'''This module Handles all the GUI events(button pressed). It handles users actions on GUI. '''

from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from dateutil import tz
from PySide2.QtWidgets import QPlainTextEdit,QLabel
import yagmail


class EventHandler(object):
    '''This class handles all user actions on the CalendarGUI'''
    def __init__(self, calUI):
        self.calUI = calUI
        self.user_info = ''
        self.user_name = ''
        self.user_email = ''
        self.user_selection = ''

        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first time.
        # If modifying these scopes, delete the file token.pickle.
        SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

        creds = None

        if os.path.exists('tokenCal.pickle'):
            with open('tokenCal.pickle', 'rb') as token:
                creds = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
            with open('tokenCal.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('calendar', 'v3', credentials=creds)


    def bookPushButton_cliked(self):
        '''This function is called when the book push button is clicked on GUI,
        it will record which timeslot the user clicked on, and opens the pop-up window for user info

        Args:
            none

        Returns:
            none

        '''

        array = self.calUI.QListWidget.selectedItems()
        s = array[0].text()
        summary = s.split()[3]
        # Only when the selected timeslot is 'Available',
        # the dialog window will open when hit 'Book'
        if summary == 'Available':
            self.calUI.showInfoDialog()


    def sendPushButton_clicked(self):
        '''This function is called when the send pushbutton is clicked on GUI,
        it will show the main window again to the user, and gather user info from the pop-up window,
        send it as an email to the admin for a booking request

        Args:
            none

        Returns:
            none
        '''

        self.calUI.setEnabled(True) #re-enable main window when 'send' is hit
        self.calUI.infoDialog.hide() #hide popup window when 'send' is hit
        self.getUserInfo() #get user info from infoDialog(pop-up window user input)
        self.sendEmail() #wrap the user info and send it as an email to admin email address
        self.user_info = '' #clear user_info string after each 'send'

    def cancelPushButton_clicked(self):
        '''This fucntion is called when user hit cancel push button on the pop-up window,
        it will hide the pop-up window and re-show the main window

        Args:
            none

        Returns:
            none
        '''

        self.calUI.infoDialog.hide() #hide popup window
        self.calUI.setEnabled(True) #enable main window


    def clickOnDate(self):
        '''This function is called when any date on the GUI calendar is clicked,
        it will record the date that is selected,
        and pull calendar data from Google calendar account using Dr's calendarID
         and credentials,then add the data to QListWidget.

        Args:
            none

        Returns:
            none

        '''

        self.calUI.QListWidget.clear() #clear the QListWidget on GUI
        self.calUI.findChild(QLabel, 'feedbackLabel').clear() #clear feedback label
        events_list = []
        selected_date = self.calUI.calWidget.selectedDate()

        now_time = datetime.datetime.now()
        # if selected_date is today, show events from now to 11:59pm today
        if (now_time.year == selected_date.year() and now_time.month == selected_date.month()
                and now_time.day == selected_date.day()):
            start_time = now_time
        # else, show events from 0:00am to 11:59pm today
        elif (selected_date.year() >= now_time.year and selected_date.month() >= now_time.month
              and selected_date.day() > now_time.day):
            start_time = datetime.datetime(selected_date.year() , selected_date.month(), selected_date.day(), 0, 0, 1)
        else:
            # Selected a previous date, print error message, reset list
            self.calUI.QListWidget.addItem("Invalid date, please try again!")
        #no matter what, end_time is 23:59:59 of selected_date
        end_time = datetime.datetime(selected_date.year(), selected_date.month(), selected_date.day(), 23, 59, 59)

        title = "Availabilities for "+ str(selected_date.month())+ "/"+ str(selected_date.day())+ "/"+ str(selected_date.year())

        tzinfo = tz.gettz('America/Los_Angeles')
        start_time = start_time.astimezone(tzinfo)
        end_time = end_time.astimezone(tzinfo)

        #call service.events().list to set up calendar ID and start and end time
        events_result = self.service.events().list(
            calendarId='iastate.edu_0s2c32mjtkthhlefe3le63lgms@group.calendar.google.com',
            timeMin=start_time.isoformat(), timeMax=end_time.isoformat(),
            maxResults=10, singleEvents=True, orderBy='startTime').execute()

        #store all valid events in a list
        events = events_result.get('items', [])

        #check if events list is empty, print No availability found if is empty.
        if not events:
            self.calUI.QListWidget.addItem('No availability found.')
            return
        #if events list is not empty, for every event in the list, get its'dateTime' and 'summary' in the dictionary list
        self.calUI.QListWidget.addItem(title)
        for event in events:
            start = event['start'].get('dateTime')
            start_hour = int(start[11:-12])
            now_hour = int(now_time.hour)
            start_date = int(start[8:10])
            now_date = int(now_time.day)

            end = event['end'].get('dateTime')
            time_slot = start[11:-9] +' - '+end[11:-9]
            s = time_slot +' '+ event['summary']

            if (start_date == now_date) & (start_hour == now_hour):
                continue
            #append all results to events_list and add to QListWidget
            else:
                events_list.append(s)
                self.calUI.QListWidget.addItem(s) # add events to QListWidget


    def getUserInfo(self):
        '''
        This function reads user's time date selection, and their input data from the infoWindow
        The variables like self.users_info,self.user_name, etc will be updated and will be used to send email for booking request

        Args:
            none

        Returns:
            none
        '''
        select_widget = self.calUI.QListWidget
        array1= select_widget.selectedItems()
        selected_date = self.calUI.calWidget.selectedDate() #get selected Date
        date = str(selected_date.month()) +'/'+ str(selected_date.day()) +'/' +str(selected_date.year()) #convert the selected date to a more readable format
        self.user_info += 'Selected time: ' + date + ' ' + array1[0].text() #add selected time to user_info
        self.user_name = self.calUI.infoDialog.findChild(QPlainTextEdit, 'nameTextEdit').toPlainText()
        self.user_info = self.user_info + '\n' + 'Patient name: ' + self.user_name # add user name to user_info
        self.user_email = self.calUI.infoDialog.findChild(QPlainTextEdit, 'emailTextEdit').toPlainText()
        self.user_info = self.user_info + '\n' + 'Patient email: '+ self.user_email # add user email to user_info
        self.user_reason = self.calUI.infoDialog.findChild(QPlainTextEdit, 'reasonTextEdit').toPlainText()
        self.user_info = self.user_info + '\n' + 'Reason for visit: ' + self.user_reason #add user reason to user_info


    def sendEmail(self):
        '''This function sends the user data as an email to admin email address

        Args:
            none

        Returns:
            none

        '''
        yag = yagmail.SMTP("drcalendarapp2020@gmail.com", "jffscsedqfhauzmg")
        admin_email = 'yidingh@iastate.edu'
        msg = yag.send(to=admin_email, subject='Appointment Request from: '+ self.user_name, contents=self.user_info)

        #set feedbackLabel to Success or Failed to give user feedback after they hit send
        feedbackLabel= self.calUI.findChild(QLabel,'feedbackLabel')
        if msg == False:
            feedbackLabel.setText("Failed!")
            feedbackLabel.setStyleSheet('color: red')
        else:
            feedbackLabel.setText("Success!")
            feedbackLabel.setStyleSheet('color: green')





