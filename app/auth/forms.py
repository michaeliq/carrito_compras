from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import EmailField

class UserForm(FlaskForm):
    
    email = EmailField('',validators=[DataRequired(),Length(max=50)])
    password = PasswordField('',validators=[DataRequired()])
    submit = SubmitField('login')
