# from flask import Flask, render_template, redirect, url_for, request

from app2 import app
from app2.forms import LoginForm, RegForm, SpellCheckForm
from flask import render_template, redirect, flash, url_for, request
from subprocess import check_output
from flask_login import current_user, login_user
from app2.models import User
from pylint.checkers import spelling


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Microblg')





@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('spell_check'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.uname.data).first()
        if user is None or not user.check_password(form.pword.data):
            flash('Invalid Username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect('/spell_check')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    form = RegForm()
    if request.method == 'POST':
        if form['Username'] != 'admin' or form['password'] != 'admin':
            error = "Invalid Credentials. Please Try Again."
        else:
            return redirect(url_for('spell_check'))
    return render_template('register.html', error=error, form=form)



@app.route('/spell_check')
def spell_check():
    error = None
    form = SpellCheckForm()
    if request.method == 'POST':
        stdout = check_output(['./a.out', './dictionary.txt', spelling]).decode('utf-8')
        form['outputtext'] = stdout
    return render_template('spell_check.html', error=error, form=form)