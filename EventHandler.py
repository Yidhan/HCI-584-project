"""This is the class that Handles all the GUI events(button pressed). It handles users actions on GUI. """

# -----------------------------------------------------------------------------------------------------------------------
# Name:       EventHandler.py
# Purpose:    This class handles the GUI events, it handles user actions on GUI.
# Author:     Yiding Han
# Created:    6/12/2020
# TODO:       Add function body
# Note:       Handles GUI events and interacts with google calendar API directly
# -----------------------------------------------------------------------------------------------------------------------
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from dateutil import tz
from PySide2.QtWidgets import QDialog

class EventHandler(object):

    def __init__(self, calUI):
        self.calUI = calUI
        pass

        # If modifying these scopes, delete the file token.pickle.
        SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
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
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('calendar', 'v3', credentials=creds)

    #when book button is clicked
    def bookPushButton_cliked(self):
        self.calUI.CreateInfoDialog()


    #when book button is clicked
    #need to fill in the body
    def refreshPushButton_clicked(self):
        print("Page is refreshed")


    #This function is called when any date on the GUI calendar is clicked
    #it will record the date that is selected,
    #and pull calendar data from Google calendar account using Dr's calendarID and credentials,
    #then print out and return the events list(availablity)
    def clickOnDate(self):
        self.calUI.QListWidget.clear()
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
            print("Invalid date, please try again!")
            return events_list
        #no matter what, end_time is 23:59:59 of selected_date
        end_time = datetime.datetime(selected_date.year(), selected_date.month(), selected_date.day(), 23, 59, 59)

        #print out title for the results
        print('Availabilities for', selected_date.month(), '/', selected_date.day(), '/', selected_date.year())

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
            print('No availability found.')
        #if events list is not empty, for every event in the list, get its'dateTime' and 'summary' in the dictionary list
        for event in events:
            start = event['start'].get('dateTime')
            s = start +' '+ event['summary']
            #append all results to events_list and print it
            events_list.append(s)
            print(s)
            self.calUI.QListWidget.addItem(s)
        return events_list
