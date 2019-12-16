from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app2.models import User

class LoginForm(FlaskForm):
    uname = StringField('Username', validators=[DataRequired()])
    pword = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegForm(FlaskForm):
    uname = StringField('Username', validators=[DataRequired()])
    pword = PasswordField('Password', validators=[DataRequired()])
    pword2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('pword')])
    twofa = StringField('2FA?', id='2fa')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username. ')


class SpellCheckForm(FlaskForm):
    inputtext = StringField('Input_Text', validators=[DataRequired()])
    outputtext = StringField('Check Results', validators=[DataRequired()])
    submittext = SubmitField('Submit text')
