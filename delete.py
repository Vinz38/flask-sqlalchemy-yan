from flask_login import logout_user, login_required, LoginManager, login_user
from flask import Blueprint, render_template, redirect, url_for, request, abort
from flask_login import current_user
from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.login_manager import LoginForm
from forms.login_job import JobForm

delete_bp = Blueprint("delete", __name__)

login_manager = LoginManager()
login_manager.init_app(delete_bp)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


@delete_bp.route('/delete/<int:job_id>', methods=['GET', 'POST'])
@login_required
def delete_job(job_id):
    
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)

    if not job:
        abort(404)

    if current_user.id != job.team_leader and current_user.id != 1:
        abort(403)
        
    db_sess.delete(job)
    db_sess.commit()
    return redirect('/main')