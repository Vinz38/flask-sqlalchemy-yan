from flask_login import logout_user, login_required, LoginManager, login_user
from flask import Blueprint, render_template, redirect, url_for
from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.login_manager import LoginForm


auth_bp = Blueprint("auth", __name__)

login_manager = LoginManager()
login_manager.init_app(auth_bp)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(
            User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for("auto_answer"))
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
