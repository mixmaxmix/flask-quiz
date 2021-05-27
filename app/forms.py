from wtforms.widgets.core import Option
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
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

class Question():
    q_id = -1
    question = ""
    option1 = ""
    option2 = ""
    option3 = ""
    option4 = ""
    correctOption = -1

    def __init__(self, q_id, question, option1, option2, option3, option4, correctOption):
        self.q_id = q_id
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correctOption = correctOption

    def get_correct_option(self):
        if self.correctOption == 1:
            return self.option1
        elif self.correctOption == 2:
            return self.option2
        elif self.correctOption == 3:
            return self.option3
        elif self.correctOption == 4:
            return self.option4

# q1 = Question(1, "What is?", "y", "s", "a", 1)
# q2 = Question(2, "What is?", "y", "s", "a", 1)
# q3 = Question(3, "What is?", "y", "s", "a", 1)


quizes = [
    {
    'title':"Война 1812 года",
    'description':"Лично маэстро Панасенков сделал этот тест для вас!",
    'questions': [
        Question(1, "В июне 1807 года Наполеон нанес русской армии поражение под?", "Фридландом", "Ватерлоо", "Тильзитом", "Егерсдорфом", 1),
        Question(2, "В 1807 г. был заключен мир?", "Парижский", "Тильзитский", "Берлинский", "Ништадтский", 2),
        Question(3, "По Тильзитскому мирному договору Россия?", "потеряла Молдавию", "уступила Валахию", "вступила вместе с Францией в войну со Швецией", "была вынуждена присоединиться к континентальной блокаде Англии", 4)
    ],
    'background': "linear-gradient(116deg, #8271E8 0%, rgba(130, 113, 232, 0.5) 100%), url(https://cdn24.img.ria.ru/images/96130/54/961305484_0:282:2509:1693_600x0_80_0_0_2bbfbeb8cb97b2c909c62b8e0c28c659.jpg)"
    },
    {
    'title':"Тест на обобщёные темы",
    'description':"Знать всё на свете нереально, но я, мечту свою лелея, решил проблему гениально — Я подключаюсь к Тесту",
    'questions': [
        Question(1, "Сколько континентов на планете Земля?", "7", "8", "6", "9", 4),
        Question(2, "Когда началась Вторая мировая война?", "1939", "1941", "1938", "1945", 1),
        Question(3, "Самый большой водопад в мире?", "Ниагарский водопад", "Игуасу", "Анхель", "Виктория", 3),
        Question(4, "Какой самый большой океан в мире?", "Тихий океан", "Индийский океан", "Северный Ледовитый океан", "Атлантический океан", 1),
        Question(5, "Сколько планет в солнечной системе?", "10", "9", "7", "8", 4),
        Question(6, "Самая горячая планета в солнечной системе?", "Меркурий", "Венера", "Юпитер", "Нептун", 2),
        Question(7, "Какой город является столицей Америки?", "Вашингтон", "Нью-Йорк", "Лос-Анджелес", "Даллас", 1),
    ],
    'background': "linear-gradient(116deg, #21145a 0%, rgba(33, 20, 90, 0.5) 100%), url(https://cdn25.img.ria.ru/images/153372/55/1533725536_112:0:1889:1333_1920x0_80_0_0_cad9d16705cdaa334188794363a504e0.jpg)"
    },
    {
    'title':"Литературный тест",
    'description':"Многогранный тест по литературе",
    'questions': [
        Question(1, "Сколько континентов на планете Земля ?", "7", "8", "6", "9", 4),
        Question(2, "Сколько континентов на планете Земля ?", "7", "8", "6", "9", 4),
        Question(3, "Сколько континентов на планете Земля ?", "7", "8", "6", "9", 4)
    ],
    'background': "linear-gradient(116deg, #C98827 0%, rgba(90, 62, 20, 0.5) 100%), url(https://tatmitropolia.ru/www/news2017/4/Starye-knigi-Makro-595.jpg)"
    },
    {
    'title':"Насколько ты знаешь Гамида?",
    'description':"Обаятельный, решимый, добрый и просто красивый преподаватель IThub",
    'questions': [
        Question(1, "Сколько континентов на планете Земля ?", "7", "8", "6", "9", 4),
        Question(2, "Сколько континентов на планете Земля ?", "7", "8", "6", "9", 4),
        Question(3, "Сколько континентов на планете Земля ?", "7", "8", "6", "9", 4)
    ],
    'background': "linear-gradient(116deg, #68A9E4 0%, rgba(104, 169, 228, 0.5) 100%), url(https://sun9-36.userapi.com/impg/c858320/v858320484/1d8467/LAVXKv3G_WQ.jpg?size=1440x2160&quality=96&sign=c3eebad7c18e6b6f6c7022cc9fd9bcfa&type=album)"
    }
]

categs = [
    {
        'title':"Лучшие тесты",
        'quizes':[
            0,
            1
        ]
    },
    {
        'title':"Научные тесты",
        'quizes':[
            0,
            1,
            2
        ]
    },
    {
        'title':"Тест про Голливудских актеров",
        'quizes':[
            3
        ]
    }
]