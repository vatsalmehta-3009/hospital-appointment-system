# create_db.py
from app import app, db
from models.facility import Facility
from models.doctor import Doctor
from models.session import Session
from models.patient import Patient
from models.appointment import Appointment

with app.app_context():
    db.create_all()
    print("Database tables created!")