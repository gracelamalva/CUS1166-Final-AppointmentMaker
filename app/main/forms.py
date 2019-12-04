
# import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, DateField, DateTimeField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Length

class TaskForm(FlaskForm):
    task_desc = StringField('task_desc', validators=[DataRequired()])
    task_status_completed = SelectField('Status', choices=[('todo','Todo'),('doing','Doing'),('done','Done')])
    submit = SubmitField('submit')

class AppointmentForm(FlaskForm):
    #appt_desc = StringField('appt_desc', validators=[DataRequired()])
    appt_status_completed = SelectField('Status', choices=[('upcoming','upcoming'),('doing','Doing'),('completed','Completed')])
    appt_title = StringField('appt_title')#, validators=[DataRequired()])
    appt_date = DateField('appt_date', format = '%Y-%m-%d')
    appt_start_time = StringField('appt_start_time') #in minutes
    appt_duration= StringField('appt_duration') #in minutes
    appt_location = StringField('appt_location')#, validators=[DataRequired()])
    appt_customer_name = StringField('appt_customer_name')#, validators=[DataRequired()])
    appt_notes = StringField('appt_customer_name')#, validators=[DataRequired()])
    appt_status = StringField('appt_status')#, validators=[DataRequired()])
    submit = SubmitField('submit')
