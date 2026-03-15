from data import db_session
from data.users import User


db_name = input()

db_session.global_init(f"db/{db_name}")
db_sess = db_session.create_session()

users = db_sess.query(User).filter(
    User.address == "module_1" and "engineer" not in User.speciality and "engineer" not in User.position).all()

for user in users:
    print(f"{user.id}")
