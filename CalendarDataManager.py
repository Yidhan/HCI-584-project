"""This class manages data that pulled from Google calendar and provide data for GUI"""

# -----------------------------------------------------------------------------------------------------------------------
# Name:       CalendarDataManager.py
# Purpose:    This class pulls calendar data from Google calendar and store it in a list, for later use on GUI
# Author:     Yiding Han
# Created:    6/12/2020
# TODO:       Add function body
# Note:       Not in use
# -----------------------------------------------------------------------------------------------------------------------

from datetime import datetime,timedelta, timezone

class CalendarDataManager(object):

    event_list = [] #class attribute

    #get all calendar data from google calendar
    def get_all_data(self):
        pass

    def get_data_of_date_range(self,date_time):
        pass
    def check_time_on_date(self,specific_time):
        pass
