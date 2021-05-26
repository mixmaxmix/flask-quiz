from wtforms.widgets.core import Option
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, form
from wtforms.validators import InputRequired, Email, Length, DataRequired, ValidationError, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Псевдоним', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class RegistrationForm(FlaskForm):
    username = StringField('Псевдоним', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Псевдоним занят')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Почта занята')

class Question(FlaskForm):
    q_id = -1
    question = ""
    option1 = ""
    option2 = ""
    option3 = ""
    correctOption = -1

    def __init__(self, q_id, question, option1, option2, option3, correctOption):
        self.q_id = q_id
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.correctOption = correctOption

    def get_correct_option(self):
        if self.correctOption == 1:
            return self.option1
        elif self.correctOption == 2:
            return self.option2
        elif self.correctOption == 3:
            return self.option3

q1 = Question(1, "What is?", "y", "s", "a", 1)
q2 = Question(2, "What is?", "y", "s", "a", 3)
q3 = Question(3, "What is?", "y", "s", "a", 2)

questions_list = [q1, q2, q3]