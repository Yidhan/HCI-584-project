# Developer's Guide 

## Overview 
This is an appointment booking system designed for doctor’s offices and patients. Patients can check out available date and time on the app, which will pull event information from the administration Google calendar, and request a booking by sending an email through the app using yagmail API. The staff in the doctor's office will review the booking requests on their Gmail account and then perform the booking on Google calendar manually.

## Condensed version of the final(!) planning specs, i.e. which parts of the initial specs are actually currently implemented.
Specs - 
- Admin sets a range of dates and blocks of time on their Google calendar account.
- App reads the data from google calendar- patients can click on a date and see the availability printed out on a list. 
- Patients can book directly on the app— select a timeslot on the list, and click “Book”, then filled out the popped out form, and click “Send” to send the request as an email.
- After patients click "Send" on the app, the popped out window will disappear and user is back to the main window of the app. There will be an feedback message on the main window indicating if the messages has been sent successfully or not(“Success” or “Fail”)
- Admin can perform changes and cancellations on google calendar

## Install/deployment/admin issues:
Currently the app uses two APIs, both need configuration/authorization. 
1.	To be able to “pull” the calendar events from the desired google calendar, you need to have a Google account with Google Calendar enabled. Then, turn on the Google Calendar API on this page, step1(Click here)In resulting dialog click DOWNLOAD CLIENT CONFIGURATION and save the file ‪credentials.json‬ to your working directory. Get the calendar ID from the calendar you want to use, in your google account, it should end with @group.calendar.google.com, here is instructions on how to find it. Next, update the ‘calendarId’ local variable in EventHandler.py –> clickOnDate() to be your own calendar ID. Now you can pull data from your Google calendar and show it on the GUI.‬
2.	To be able to send request email from the app to the admin email on the user’s behalf, first, you need to set up your admin email, simply update the variable “admin_email” in EventHandler.py –>sendEmail() to be your desired email address. You will also need a separate Gmail that your want the message to send from, aka App Gmail account. Then, in the same function, update the input of yag = yagmail.SMTP(“the App Gmail account”, “Gmail app password”). You can set up you Gmail app password in your account, here is how. Now you can send email from the app to the desired admin email account by clicking ‘send’ on the GUI.

##User interaction and flow through your code ("walkthrough")
The whole program workflow is based on user interaction with the GUI, when users:
1.	Click on any date on the Calendar Widget on the main window - clickOnDate() in EventHandler class/module is called. it will record the date that is selected, and pull calendar data from Google calendar account on that date, then add the data to List Widget to display. This function will also filter the events based on time. For example, if the selection date is today, it will also add the events that’s not yet happen compared to current time to the List Widget. If users choose a past date (date earlier than today), it will display an error message “Invalid date”, etc. 

2.	Click on one of the timeslot on the List Widget and then click on the “Book” push button on the main window – bookPushButton_clicked() in EventHandler class/module is called. Info window will pop out on top of the main window, in the meantime, the main window will be disabled. This function also checks if the event selected is “bookable”, for example, only events with status “Available” will show the info window. The title in the list and events that are booked are not “bookable” this way. 

3. 	Fill in the Name, email, and reason for visit text boxes in the new window, and then click “Send” push button – sendPushButton_clicked() in EventHandler class/module is called, inside the function, it will call getUserInfo() in the same class, to update self.user_info variable, which is user’s input information, and then call sendEmail(), which will use self.user_info as content of the email.

4.	Clicks on “Cancel” push button – cancelPushButton_clicked() is called, which will hide the info window, and enable the main window again for the users to select another date.

## Known Issues: 
Minor: The info window will not clear if the user filled in info before and tried to book again, but I think it is not a big problem since the user is likely to reuse the information for another booking.

## Future work:
1.	To send an Google calendar event invite to the admin calendar and Gmail would be cool, since the admin can choose to accept or decline the request directly and update the calendar. I was not able to make it work because all invites would have been sent from the dummy app email, not from the user’s account, so there is no way they can know the results of the request, unless the admin send a confirmation email manually.

2.	More user friendly features could be added such as looking up events in a range of dates instead of just one day, i.e. 8/1-8/10. More filters could be added, i.e. only show the events that’s “Available”, or only show the events that’s between 10am – 2pm. These feature would be nice to have in the future. 
