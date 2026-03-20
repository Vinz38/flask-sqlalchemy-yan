from flask import Flask, render_template
from flask_login import login_required
from data import db_session
from data.users import User
from data.jobs import Jobs
from flask_login import LoginManager
from auth import auth_bp
from register import reg_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.register_blueprint(auth_bp)
app.register_blueprint(reg_bp)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, int(user_id))

@app.route('/')
@app.route('/main')
@login_required
def auto_answer():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    jobs = db_sess.query(Jobs).all()
    actions = []
    id_work = None
    for user in users:
        is_finished = ""
        collaborators = ""
        duration = 0
        for job in jobs:
            if user.id == job.team_leader:
                if job.is_finished == 0:
                    is_finished = "Is not finished"
                else:
                    is_finished = "Is finished"
            id_work = job.id
            collaborators = job.collaborators
            duration = job.work_size
            break
        action = [user.speciality,
                  f"{user.surname} {user.name}", f"{duration} hours", collaborators, is_finished]
        actions.append(action)
    return render_template('classwork-7.html', actions=actions, id_work=id_work)


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    app.run(port=8080, host='127.0.0.1')
