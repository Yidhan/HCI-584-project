# HCI-584-project

## Appointment Booking System Desktop App Using Google Calendar API

### Target User:
Doctor’s office staff and Patients

### Task Description:
Designing an appointment booking system for doctor’s offices and patients. Patients can check out available date and time on the app, and request a booking through Google calendar API as invitations. The staff in the doctor's office will review the booking requests via google calendar and then perform the booking by accepting or declining the invitation on Google calendar. 

### Workflow and User interaction:
- Admin sets a range of dates and blocks of time (on weekdays, 1 hour blocks 9am to 5pm) on their google calendar account
- App reads the data from google calendar (patient portal)--patients can click on a date and see the availablity printed out. 
- Both patients and the doctor's office can see what's available or booked.
- Admin can perform changes and cancellations on google calendar
- Patients can book directly on the app--send an update event request.
- When patients click "book" on the app, the time slot selected gets "reservered" automatically (statues changed to "book" or simply disappeared on calendar)
- Refresh the calendar data on patient portal by click "Refresh" or every certain time

### Possible external mechanisms to be used:
- Google Calendar API
- GUI design package PyQt 

### GUI:
Desktop app, only for patients. Doctor’s office portal is on their google account.

### Data Flow
CalendarGUI----(bind with)-----> EventHandler----(get data from and updates)--->Dr.Google calendar account
CalendarData(optional)---format data???
