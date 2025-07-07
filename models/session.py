from models import db

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clinic_id = db.Column(db.Integer, db.ForeignKey('facility.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    max_tokens = db.Column(db.Integer, nullable=False)

    clinic = db.relationship('Facility', backref='sessions')
    doctor = db.relationship('Doctor', backref='sessions') 