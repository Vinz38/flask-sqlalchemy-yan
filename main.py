from flask import Flask, render_template
from flask_login import login_required
from data import db_session
from data.users import User
from data.jobs import Jobs
from flask_login import LoginManager
from auth import auth_bp
from register import reg_bp
from delete import delete_bp
from edit import edit_bp
from add import add_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.register_blueprint(auth_bp)
app.register_blueprint(reg_bp)
app.register_blueprint(edit_bp)
app.register_blueprint(delete_bp)
app.register_blueprint(add_bp)

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
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    jobs = db_sess.query(Jobs).all()
    actions = []
    for job in jobs:
        name = ""
        if_finished = ""
        for user in users:
            if user.id == job.team_leader:
                name = f"{user.surname} {user.name}"
                break
        if job.is_finished:
            if_finished = "Is finished"
        else:
            if_finished = "Is not finished"
        action = [job.job, name, job.work_size, job.collaborators, if_finished, job.id]
        actions.append(action)
    return render_template('classwork-7.html', actions=actions)


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    app.run(port=8080, host='127.0.0.1')
