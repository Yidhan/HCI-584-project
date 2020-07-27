Bug sheet

6/17
1. To fix: EventHandler class, function clickOnDate: fix "now"(startMin) to be date clicked starting from 0:00?
6/20
Bug 1 fixed.

6/21
2. close The pop-up infoWindow will automatically exit the running program, which is not expected
3. close the main window will not close the infoWindow,and the program still runs
4. when the pop-up info window shows up, I can still use the main window to look up dates, when it shouldn’t, the pop-up window should have the priority, and the main window should be blocked at this time.

Bugs 2,3,4 fixed by adding features to the popup window(made it frameless and stay on top), hide when send button is clicked.git 

5. Gmail API won't work with credentials and tokens. May try another method to use GoogleCalendar API and use another email address to "insert events", thus creating an event and send an invite to admin for review.
Will call this method2 and work in another branch. 


Bug 5 fixed with yagmail

6. If user book another appt, the former info will accumulate with the new, and sent together as email.
example: 
Selected time: 2020-07-23T13:00:00-07:00 Available
Patient name: e3r
Patient email: erewr
Reason for visit: rerwSelected time: 2020-07-23T13:00:00-07:00 Available
Patient name: e3r
Patient email: erewr
Reason for visit: rerw


7. "Success" label from former booking won't disappear when click on another date to book another one

Bug 6 & 7 fixed.

8. Other ppl with the project file can't run it successfully(authorization problem)
fixed?

9. When the app runs, it automatically selects "today" on calendar(selected, highlighted), but the List widget has nothing to display(should have displayed today's events)
fixed

10. When the selection is "today", the events are sorted by the end time of the events, for example, if now is 2:30pm, the 2:00-3:00 event would still show up in the list, but it should not since the start time < current time. 
fixed, added more filter when added to list widget.