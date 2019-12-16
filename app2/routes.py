# from flask import Flask, render_template, redirect, url_for, request

from app2 import app
from app2.forms import LoginForm, RegForm, SpellCheckForm
from flask import render_template, redirect, flash, url_for, request
from subprocess import check_output

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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
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