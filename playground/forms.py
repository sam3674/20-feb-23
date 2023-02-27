from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo,NumberRange

# #example in the web
# class RegistrationForm(FlaskForm):
#     username = StringField('Username',
#                            validators=[DataRequired(), Length(min=2, max=20)])
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password',
#                                      validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up')



#for schedule page
class AddNewTaskForm(FlaskForm):
    AskTaskName = StringField('TaskName'
                              ,validators=[DataRequired(), Length(min=0,max=20)])
    AskStartTime = IntegerField('Start Time',validators=[
         NumberRange(min=0, max=32) ],default=0)
    AskEndTime = IntegerField('End Time',validators=[ 
        NumberRange(min=0, max=32)],default=0 )

    user_add = SubmitField('add new task')
    user_delete = SubmitField('delete the task')






# #example
# class LoginForm(FlaskForm):
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')