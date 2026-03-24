from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    team_leader = IntegerField("id директора отдела", validators=[DataRequired()])
    job = StringField("Название работы", validators=[DataRequired()])
    work_size = IntegerField("Размер работы", validators=[DataRequired()])
    collaborators = StringField("Состав команды", validators=[DataRequired()])
    is_finished = BooleanField("Работа завершена?")
    submit = SubmitField("Создать")
