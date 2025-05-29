from database import db
from errors import ClassroomNotExist, ClassroomAlreadyReserved
import requests

class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    classroom_id = db.Column(db.Integer, nullable=False)
    classroom_name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    start_time = db.Column(db.String(10), nullable=False)
    end_time = db.Column(db.String(10), nullable=False)

    def __init__(self, classroom_id, classroom_name, date, start_time, end_time):
        self.classroom_id = classroom_id
        self.classroom_name =  classroom_name
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def to_dict(self):
        return {
            "id": self.id,
            "classroom_id": self.classroom_id,
            "classroom_name": self.classroom_name,
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time
        }
    
def addBooking(data):
    classroom_id = data["classroom_id"]

    res = requests.get(f"http://localhost:5000/turmas/{classroom_id}")
    if res.status_code != 200:
        raise ClassroomNotExist('Sala de aula não encontrada.')
    
    classroom = res.json()
    if classroom['reserved'] == True:
        raise ClassroomAlreadyReserved('Essa sala de aula já está reservada.')

    booking = Booking(
        classroom_id=classroom_id,
        classroom_name=classroom['name'],
        date=data["date"],
        start_time=data["start_time"],
        end_time=data["end_time"]
    )

    body = {
        "name": classroom['name'],
        "professor_id": classroom['professor_id'],
        "active": classroom['active'],
        "reserved": True
    }
    requests.put(f"http://localhost:5000/turmas/{classroom_id}", json=body)
    
    db.session.add(booking)
    db.session.commit()

def getBookings():
    bookings = Booking.query.all()
    return [booking.to_dict() for booking in bookings]
