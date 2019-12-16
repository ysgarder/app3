from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    uname = StringField('Username', validators=[DataRequired()])
    pword = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegForm(FlaskForm):
    uname = StringField('Username', validators=[DataRequired()])
    pword = PasswordField('Password', validators=[DataRequired()])
    twofa = StringField('2FA?', id='2fa')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class SpellCheckForm(FlaskForm):
    inputtext = StringField('Input_Text', validators=[DataRequired()])
    outputtext = StringField('Check Results', validators=[DataRequired()])
    submittext = SubmitField('Submit text')
