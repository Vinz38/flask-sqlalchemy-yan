from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")

    db_sess = db_session.create_session()

    captain = User()
    captain.surname = "Scott"
    captain.name = "Ridley"
    captain.age = 21
    captain.position = "captain"
    captain.speciality = "research engineer"
    captain.address = "module_1"
    captain.email = "scott_chief@mars.org"

    user1 = User()
    user1.surname = "Ep"
    user1.name = "Kirill"
    user1.age = 16
    user1.position = "passenger"
    user1.speciality = "programmer"
    user1.address = "module_12"
    user1.email = "kirill_ep@mars.org"

    user2 = User()
    user2.surname = "Nik"
    user2.name = "Ilia"
    user2.age = 16
    user2.position = "passenger"
    user2.speciality = "programmer"
    user2.address = "module_13"
    user2.email = "ilia_nik@mars.org"

    user3 = User()
    user3.surname = "Kur"
    user3.name = "Arseniy"
    user3.age = 16
    user3.position = "passenger"
    user3.speciality = "physicist"
    user3.address = "module_52"
    user3.email = "ars@mars.org"

    job1 = Jobs()
    job1.team_leader = 1
    job1.job = "deployment of residential modules 1 and 2"
    job1.work_size = 15
    job1.collaborators = "2, 3"
    job1.start_date = datetime.datetime(2026, 3, 15)
    job1.is_finished = False

    db_sess.add(captain)
    db_sess.add(user1)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.add(job1)
    db_sess.commit()


if __name__ == '__main__':
    main()
