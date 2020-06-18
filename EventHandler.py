"""This is the class that Handles all the GUI events(button pressed). It handles users actions on GUI. """

# -----------------------------------------------------------------------------------------------------------------------
# Name:       EventHandler.py
# Purpose:    This class handles the GUI events, it handles user actions on GUI.
# Author:     Yiding Han
# Created:    6/12/2020
# TODO:       Add function body
# Note:
# -----------------------------------------------------------------------------------------------------------------------
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class EventHandler(object):

    def __init__(self):
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
        print("You are booked!")


    #when book button is clicked
    def refreshPushButton_clicked(self):
        print("Page is refreshed")


    def clickOnDate(self):
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        end_of_day = (datetime.datetime.utcnow() + datetime.timedelta(hours=24)).isoformat() + 'Z'
        print('Availabilities for the next 24 hours')
        events_result = self.service.events().list(
            calendarId='iastate.edu_0s2c32mjtkthhlefe3le63lgms@group.calendar.google.com', timeMin=now,
            timeMax=end_of_day, maxResults=100, singleEvents=True,
            orderBy='startTime').execute()
        events = events_result.get('items', [])
        events_list=[]
        if not events:
            print('No availability found.')
        for event in events:
            start = event['start'].get('dateTime')
            s = start + event['summary']
            events_list.append(s)
            print(s)
        return events_list
