import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
from dotenv import load_dotenv


load_dotenv() 

# Get the environment variables
database_url = os.getenv('DATABASE_URL')

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {"databaseURL": database_url})

ref = db.reference("Students")

data = {
    "321654": {
        "name": "Murtaza Hassan",
        "major": "Robotics",
        "starting_year": 2017,
        "total_attendance": 7,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34",
    },
    "852741": {
        "name": "Emly Blunt",
        "major": "Economics",
        "starting_year": 2021,
        "total_attendance": 12,
        "standing": "B",
        "year": 1,
        "last_attendance_time": "2022-12-11 00:54:34",
    },
    "963852": {
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34",
    },
    "1741510": {
        "name": "Mohit Kumar",
        "major": "Computer Science",
        "starting_year": 2021,
        "total_attendance": 7,
        "standing": "A",
        "year": 4,
        "last_attendance_time": "2021-12-11 00:54:34",
    },
    "17245": {
        "name": "Tony stark",
        "major": "Aeronautics",
        "starting_year": 2021,
        "total_attendance": 1,
        "standing": "C",
        "year": 2,
        "last_attendance_time": "2021-12-01 00:54:34",
    }
}

for key, value in data.items():
    ref.child(key).set(value)
