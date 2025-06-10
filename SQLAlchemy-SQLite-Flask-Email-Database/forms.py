from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    name=StringField("NAME", validators=[DataRequired('A full name is required'), Length(min=5, max=30)])
    email=StringField("NAME", validators=[DataRequired('A correct email is required'), Email()])
    message=TextAreaField("Message", validators=[DataRequired('A message is required'), Length(min=5, max=500)])
    submit=SubmitField('SEND')
    

