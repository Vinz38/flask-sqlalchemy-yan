from flask import Flask, render_template
from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def auto_answer():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    jobs = db_sess.query(Jobs).all()
    actions = []
    for user in users:
        is_finished = ""
        collaborators = ""
        id_work = None
        duration = datetime.datetime.now() - user.modified_date
        hours = duration.total_seconds() / 3600
        hours = round(hours, 1)
        for job in jobs:
            if user.id == job.team_leader:
                if job.is_finished == 0:
                    is_finished = "Is not finished"
                else:
                    is_finished = "Is finished"
            id_work = job.id
            collaborators = job.collaborators
            break
        action = [user.speciality,
                  f"{user.surname} {user.name}", f"{hours} hours", collaborators, is_finished]
        actions.append(action)
    return render_template('classwork-7.html', actions=actions, id_work=id_work)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
