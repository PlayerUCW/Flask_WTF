from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired


class EmAcForm(FlaskForm):
    id = StringField('ID астронавта', validators=[DataRequired()])
    pw = PasswordField('Пароль астронавта', validators=[DataRequired()])
    cid = StringField('ID капитана', validators=[DataRequired()])
    cpw = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')

class FileForm(FlaskForm):
    file = FileField('Добавить картинку', validators=[DataRequired()])
    submit = SubmitField('Загрузить')