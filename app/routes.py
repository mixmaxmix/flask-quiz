from os import name
from wtforms.widgets.core import Option
from app import app, db
from flask import Flask, render_template, url_for, request, redirect
from werkzeug.urls import url_parse
from app.models import User
from app.forms import LoginForm, Question, RegistrationForm, quizes, categs
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/')
@app.route('/dashboard')
def index():
    return render_template("index.html", user=current_user, quizes=quizes, categs=categs)

@app.route('/reg', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('reg.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return 'Вы ввели неправильный логин/пароль!'
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("login.html", form=form)
    
@app.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)

@app.route('/quiz/<int:id>')
@login_required
def quiz(id):
    return render_template("quiz.html", user=current_user, questions_list=quizes[id]['questions'], id=id)

@app.route('/sumbitquiz/<int:id>', methods=['POST', 'GET'])
@login_required
def submit(id):
    correct_count = 0
    if request.method == 'POST':
        for question in quizes[id]['questions']:
            question_id = str(question.q_id)
            print(request.get_data())
            selected_option = request.form[question_id]
            print(selected_option)
            correct_option = question.get_correct_option()
            if selected_option == correct_option:
                correct_count = correct_count + 1

        correct_count = str(correct_count)
        print(correct_count)
    return render_template("sumbitquiz.html", user=current_user, correct_count=correct_count)

@app.route('/settings')
@login_required
def settings():
    return render_template("settings.html", user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')