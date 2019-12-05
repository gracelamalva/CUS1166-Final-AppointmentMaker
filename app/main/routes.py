from flask import render_template,  redirect, url_for, flash
from app.main import bp
from app import db
from app.main.forms import TaskForm, AppointmentForm, AppointmentSearchForm
from app.models import Task, Appointment
from datetime import datetime as dt
from datetime import timedelta

# Main route of the applicaitons.
@bp.route('/', methods=['GET','POST'])
def index():
    return render_template("main/index.html")

#  Route for viewing and adding new tasks.
@bp.route('/todolist', methods=['GET','POST'])
def todolist():
    form = TaskForm()

    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.
        new_task = Task()
        new_task.task_desc =  form.task_desc.data
        new_task.task_status = form.task_status_completed.data

        db.session.add(new_task)
        db.session.commit()

        # Redirect to this handler - but without form submitted - gets a clear form.
        return redirect(url_for('main.todolist'))

    todo_list = db.session.query(Task).all()

    return render_template("main/todolist.html",todo_list = todo_list,form= form)


# Route for removing a task
@bp.route('/todolist/remove/<int:task_id>', methods=['GET','POST'])
def remove_task(task_id):

    # Query database, remove items
    Task.query.filter(Task.task_id == task_id).delete()
    db.session.commit()

    return redirect(url_for('main.todolist'))


# Route for editing a task
@bp.route('/todolist/edit/<int:task_id>', methods=['GET','POST'])
def edit_task(task_id):
    form = TaskForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.

        current_task = Task.query.filter_by(task_id=task_id).first_or_404()
        current_task.task_desc =  form.task_desc.data
        current_task.task_status = form.task_status_completed.data

        db.session.add(current_task)
        db.session.commit()
        # After editing, redirect to the view page.
        return redirect(url_for('main.todolist'))

    # get task for the database.
    current_task = Task.query.filter_by(task_id=task_id).first_or_404()

    # update the form model in order to populate the html form.
    form.task_desc.data =     current_task.task_desc
    form.task_status_completed.data = current_task.task_status

    return render_template("main/todolist_edit_view.html",form=form, task_id = task_id)


#  Route for viewing and adding new appointments.
@bp.route('/appointments', methods=['GET','POST'])
def appointments():

    form = AppointmentForm()
    searchform = AppointmentSearchForm()

    if searchform.validate_on_submit():
        search = searchform.search.data
        return redirect(url_for('main.search_results'))
        
    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.
        new_appt = Appointment()
        new_appt.appt_title =  form.appt_title.data
        new_appt.appt_date =  form.appt_date.data
        new_appt.appt_start_time =  form.appt_start_time.data
        new_appt.appt_duration  =  form.appt_duration.data
        new_appt.appt_location =  form.appt_location.data
        new_appt.appt_customer_name =  form.appt_customer_name.data
        new_appt.appt_notes = form.appt_notes.data
        new_appt.appt_status = form.appt_status_completed.data
        print(new_appt.appt_title)


        db.session.add(new_appt)
        db.session.commit()
        flash('your appointment has been created')
        # Redirect to this handler - but without form submitted - gets a clear form.
        return redirect(url_for('main.appointments'))

    appointments = db.session.query(Appointment).all()

    return render_template("main/appointment.html",appointments = appointments, searchform = searchform,form= form)


# Route for removing an appointment
@bp.route('/appointments/remove/<int:appt_id>', methods=['GET','POST'])
def remove_appointment(appt_id):

    # Query database, remove items
    Appointment.query.filter(Appointment.appt_id == appt_id).delete()
    db.session.commit()

    return redirect(url_for('main.appointments'))


# Route for editing a task
@bp.route('/appointments/edit/<int:appt_id>', methods=['GET','POST'])
def edit_appointment(appt_id):

    form = AppointmentForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.

        current_appt = Appointment.query.filter_by(appt_id = appt_id).first_or_404()

        current_appt.appt_title =  form.appt_title.data
        current_appt.appt_date =  form.appt_date.data
        current_appt.appt_start_time =  form.appt_start_time.data
        current_appt.appt_duration  =  form.appt_duration.data
        current_appt.appt_location =  form.appt_location.data
        current_appt.appt_customer_name =  form.appt_customer_name.data
        current_appt.appt_notes = form.appt_notes.data
        current_appt.appt_status = form.appt_status_completed.data

        #current_appt.appt_desc =  form.appt_desc.data
        #current_appt.appt_status = form.appt_status_completed.data

        db.session.add(current_appt)
        db.session.commit()
        # After editing, redirect to the view page.
        return redirect(url_for('main.appointments'))

    # get task for the database.
    current_appt = Appointment.query.filter_by(appt_id = appt_id).first_or_404()

    # update the form model in order to populate the html form.
    form.appt_title.data = current_appt.appt_title
    form.appt_date.data = current_appt.appt_date
    form.appt_start_time.data = current_appt.appt_start_time
    form.appt_duration.data = current_appt.appt_duration
    form.appt_location.data = current_appt.appt_location
    form.appt_customer_name.data = current_appt.appt_customer_name
    form.appt_notes.data = current_appt.appt_notes
    form.appt_status_completed.data = current_appt.appt_status

    return render_template("main/appointments_edit_view.html",form=form, appt_id = appt_id)

#filter today
@bp.route('/filter_appointments', methods=['GET','POST'])
def filter_appointments():
    form = AppointmentForm()
    searchform = AppointmentSearchForm()

    appointments = db.session.query(Appointment).filter_by(appt_date = dt.today())

    return render_template("main/appointment.html",appointments = appointments, form = form, searchform = searchform)


@bp.route('/filter_appointments_overdue', methods=['GET','POST'])
def filter_appointments_overdue():
    form = AppointmentForm()
    searchform = AppointmentSearchForm()

    appointments = db.session.query(Appointment).filter_by(appt_status= "overdue")

    return render_template("main/appointment.html",appointments = appointments, form = form, searchform = searchform)

@bp.route('/filter_appointments_completed', methods=['GET','POST'])
def filter_appointments_completed():
    form = AppointmentForm()
    searchform = AppointmentSearchForm()

    appointments = db.session.query(Appointment).filter_by(appt_status= "completed")

    return render_template("main/appointment.html",appointments = appointments, form = form, searchform = searchform)

@bp.route('/filter_appointments_thisweek', methods=['GET','POST'])
def filter_appointments_thisweek():

    form = AppointmentForm()
    searchform = AppointmentSearchForm()
    """
    today = dt.today()
    thisweek = today + dt.timedelta(days =7)
    appointments = db.session.query(Appointment).filter_by(thisweek)
    """

    appointments = Appointment.query.filter_by(appt_status= 'this week')

    return render_template("main/appointment.html",appointments = appointments, form = form, searchform = searchform)


@bp.route('/search', methods=['GET','POST'])
def search_results():

    appointments = db.session.query(Appointment).all()
    searchform = AppointmentSearchForm()
    form = AppointmentForm

    if searchform.select == "title":
        appointments = Appointment.query.filter(Appointment.appt_title.like(searchform.search.data + "%")).all()
        #results = Appointment.query.filter_by(title = )
        return render_template("main/appointment.html", appointments=appointments, form = form, searchform = searchform)
 
    if searchform.select == "customer name":
        results = Appointment.query.filter(Appointment.appt_customer_name.like(search + "%")).all()
        #results = Appointment.query.filter_by(title = )
        return render_template("main/appointment.html", appointments=appointments, form = form, searchform = searchform)

 
    return render_template("main/appointment.html", appointments=appointments, form = form, searchform = searchform)