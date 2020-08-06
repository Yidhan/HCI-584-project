# Appointment Booking System Desktop App for Doctor's office
This appointment booking application is designed for patients and staff from doctor's office. Patients can check out available date and timeslots on the app by date, and request a booking by sending the request as an email. The staff in the doctor's office will review the booking requests sent to their email address, and then perform the booking manually. 

1) main.py: imports from the CalendarGUI module(CalendarGUI.py)
2) Calendar.py: imports from EventHandler module(EventHandler.py) 
3) EventHandler: module that handler all user actions(EventHandler.py)

# Requirements
- Python (3.7 or higher)
- pyside2 (5.13.2 or higher)
- setuptools (47.3.0 or higher)
- google-api-core (1.20.1 or higher)
- google-api-python-client (1.9.3 or higher)
- google-auth (1.17.2 or higher)
- google-auth-httplib2 (0.0.4 or higher)
- google-auth-oauthlib (0.4.1 or higher)
- googleapis-common-protos (1.52.0 or higher)
- yagmail (0.11.224 or higher)

# Installation
For Main.py
- Use pip to install the required third party packages `pip install -r requirements.txt`

# Usage
Describe how to run your app
- `Main.py`: in the project root folder type in terminal `python Main.py` to run the app
- A User interface window will appear, interact with it by selecting dates on the calendar,book an appointment as desired

# Known issues
- The app needs the gmail credentials file from the admin google calendar to be able to pull the event data to view. This could be a problem since the credentials could be tampered with.
- Could have provided more feedback with each step, or a help session with the app.

