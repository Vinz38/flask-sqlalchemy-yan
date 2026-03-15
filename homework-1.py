from data import db_session
from data.users import User


db_name = input()

db_session.global_init(f"db/{db_name}")
db_sess = db_session.create_session()

users = db_sess.query(User).filter(User.age < 18).all()

for user in users:
    print(f"<Colonist> {user.id} {user.surname} {user.name} {user.age} years")
