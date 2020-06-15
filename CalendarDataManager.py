"""This class manages data that pulled from Google calendar and provide data for GUI"""

# -----------------------------------------------------------------------------------------------------------------------
# Name:       CalendarDataManager.py
# Purpose:    This class pulls calendar data from Google calendar and store it in a list, for later use on GUI
# Author:     Yiding Han
# Created:    6/12/2020
# TODO:       Add function body
# Note:
# -----------------------------------------------------------------------------------------------------------------------

from datetime import datetime,timedelta, timezone

class CalendarDataManager(object):

    event_list = [] #class attribute
    #get data from google calendar
    def get_calendar_data(url):
        pass
    #parse data to gui, each timeslot(list memeber) as a button
    def parse_to_gui(event_list):
        pass

