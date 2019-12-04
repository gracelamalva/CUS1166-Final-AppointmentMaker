
#from flask import url_for
from app import db




class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_desc = db.Column(db.String(128), index=True)
    task_status = db.Column(db.String(128))

class Appointment(db.Model):
    appt_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    appt_title = db.Column(db.String)
    appt_date = db.Column(db.Date, nullable = False)
    appt_start_time = db.Column(db.String)
    appt_duration = db.Column(db.Integer) #in minutes
    appt_location = db.Column(db.String)
    appt_customer_name = db.Column(db.String)
    appt_notes = db.Column(db.String)
    appt_status = db.Column(db.String(128))
