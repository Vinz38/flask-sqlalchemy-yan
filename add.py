from flask import Blueprint, render_template, redirect
from data import db_session
from data.jobs import Jobs
from forms.login_job import JobForm


add_bp = Blueprint('add', __name__)

@add_bp.route("/add", methods=['GET', 'POST'])
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        print(form.team_leader.data)
        job = Jobs(team_leader=form.team_leader.data,
                   job=form.job.data,
                   work_size=form.work_size.data,
                   collaborators=form.collaborators.data)
        db_sess.add(job)
        db_sess.commit()
        return redirect('/main')
    return render_template('login_job.html', title='Создание работы', form=form)