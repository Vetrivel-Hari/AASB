import time
import base64
from datetime import datetime
from pymongo import MongoClient
from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r'/api/*': {'origin': 'http://127.0.0.1:3000'}})

cluster = MongoClient("mongodb+srv://aas:hackathon@aas.2kkkz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["SAS"]

student = db["Student"]
faculty = db["Faculty"]
hall = db["Hall"]
timetable = db["Timetable"]
timing = db["Timing"]


def checkCoordinate(latitude, longitude, hall_id):
    hall_details = hall.find_one({"Hall_id": hall_id})
    print(hall_details)

    x = [0 for _ in range(4)]
    y = [0 for _ in range(4)]

    c = 0
    for i in hall_details['Corners']:
        x[c] = float(hall_details['Corners']['C' + str(c + 1)]['Latitude'])
        y[c] = float(hall_details['Corners']['C' + str(c + 1)]['Longitude'])
        c = c + 1

    print(x)
    print(y)

    xmin = min(x)
    xmax = max(x)

    ymin = min(y)
    ymax = max(y)

    if latitude >= xmin and latitude <= xmax:
        if longitude >= ymin and longitude <= ymax:
            return True
        return False

    return False


class Attendance(Resource):
    def get(self):
        return {"Message": "Hello, World"}

    @cross_origin(supports_credentials=True)
    def post(self):
        rollno = request.form["rollno"]
        latitude = request.form["latitude"]
        longitude = request.form["longitude"]
        image = request.form['image']

        print("---------------------------SAVING IMAGE-------------------------------------")
        #Save image
        image = image[image.index(",")+1: ]
        print(image)
        decodeit = open(rollno + ".jpg", 'wb')
        decodeit.write(base64.b64decode((image)))
        decodeit.close()
        print("---------------------------GUESS IMAGE IS SAVED-------------------------------------")

        #Get current students details
        student_details = student.find_one({"Rollno": rollno})

        #Get the time at which the student has requested for Attendance
        t = str(time.strftime("%H:%M"))
        current_hour = int("09")#int(t[: t.index(":")])
        current_minutes = int("20")#int(t[t.index(":") + 1:])

        #Get the timetable of the student
        student_class = timetable.find_one({"Class": rollno[0:4]})

        #Get the current weekday
        current_day = str(datetime.today().strftime('%A'))


        class_timing = timing.find_one()
        for i in class_timing.keys():
            if(i != "_id"):
                start = class_timing[i]["Start"]
                end = class_timing[i]["End"]

                hour = int(start[ : start.index(":")])
                minutes = int(start[start.index(":") + 1 : ])

                if((hour == current_hour) and (minutes + 10 >= current_minutes) and (current_minutes >= minutes)):
                    print(i, "Present in the class")
                    current_course = student_class['Schedule'][str(current_day)][i]['Course_id']
                    current_hall = student_class['Schedule'][str(current_day)][i]['Hall_id']

                    print(current_course)
                    print(current_hall)

                    #Check if the student is within the class
                    if(checkCoordinate(float(latitude), float(longitude), "SCL")):
                        #if face matches
                        #Put attendance
                        student.find_one_and_update(
                            {"Rollno": rollno},
                            {"$set":
                                 {"Courses." + current_course: student_details['Courses'][current_course] + 1}
                             }, upsert=True
                        )

                        return {"message": "You May Get Attendance"}
                        pass
                    else:
                        return {"message": "Out of Class ROOM"}

        return {"message": "Late to Class"}


'''
x = {
    "Rollno" : "20PC40",
    "Courses": {
        "20XC41": 0,
        "20XC42": 0,
        "20XC43": 0,
        "20XC44": 0,
        "20XC45": 0,
        "20XC46": 0,
        "20XC47": 0,
        "20XC48": 0,
    }
}

post_id = student.insert_one(x).inserted_id

print(post_id)
'''

@app.route("/")
def index():
    return "Welcome Back!"

api.add_resource(Attendance, "/api/attendance")

if __name__ == "__main__":
    app.run(debug=True)

