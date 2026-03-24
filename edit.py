from flask_login import logout_user, login_required, LoginManager, login_user
from flask import Blueprint, render_template, redirect, url_for, request, abort
from flask_login import current_user
from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.login_manager import LoginForm
from forms.login_job import JobForm

edit_bp = Blueprint("edit", __name__)

login_manager = LoginManager()
login_manager.init_app(edit_bp)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)

@edit_bp.route('/edit/<int:job_id>', methods=['GET', 'POST'])
@login_required
def edit_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)

    if not job:
        abort(404)

    if current_user.id != job.team_leader and current_user.id != 1:
        abort(403)

    form = JobForm()

    if request.method == 'GET':
        form.team_leader.data = job.team_leader
        form.job.data = job.job
        form.work_size.data = job.work_size
        form.collaborators.data = job.collaborators
        form.is_finished.data = job.is_finished

    if form.validate_on_submit():
        job.team_leader = form.team_leader.data
        job.job = form.job.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.is_finished = form.is_finished.data

        db_sess.commit()
        return redirect('/main')

    return render_template('login_job.html', form=form, title="Редактирование работы")
