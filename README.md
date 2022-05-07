# AUTOMATED ATTENDANCE SYSTEM

#### TEAM : INCOGNITO
#### TEAM MEMBERS : 
#### 20PC16 - HARISH NARAYAN B
#### 20PC22 - NAVIN KRISHNA T
#### 20PC37 - VETRIVEL M D

NOTE : Two repositories are used for the project. One for the frontend and another for the backend. Their links are given below.<br>
FRONTEND : https://github.com/Vetrivel-Hari/Automatic-Attendance-System-Frontend-.git <br>
BACKEND : https://github.com/Vetrivel-Hari/Automatic-Attendance-System-Backend-.git <br>

## SOLUTION PROPOSED
The objective of the solution is to reduce proxying, reduce time and effort taken to record the attendance.
The above mentioned objective is achieved by :
<ul>
  <li>Verifying and authenticating the student identity</li>
  <li>Veryfing the current location of the student</li>
</ul>
<b> Verification and authentication of student identity </b> is achieved using the <b> facial recognition </b> of the student along with
their roll number. <br>
<b> Student's current location </b> is verified by collecting their current <b> latitude </b> and <b> longitude </b> coordinates. <br>

## BACKEND

### WORKING
This repo contains the flask application that handles the working of backend in the automated attendance system.

#### API ENDPOINTS
###### /api/attendance (POST) : 
This api endpoint receives the roll number of the student, current latitude and longitude, image of the student and timestamp when the
request was made. With the given timestamp and the roll number of the student, the hall and course code along with the faculty for which attendance needs to be recorded is identified with the help of timetable stored in the database.



### APIs USED
<ul>
  <li>ImageKit.io</li>
  <li>facepplib</li>
  <li>pymongo</li>
</ul>

### TOOLS USED
<ul>
  <li>Python Flask</li>
  <li>MongoDB</li>
</ul>

### DEPLOYMENT - HEROKU
Hosted Link : https://automatic-attendance-system-3.herokuapp.com/api/attendance

### FUTURE UPDATES
Dedicated web app for faculty, so that any classroom or attendance changes can be recorded manually.
