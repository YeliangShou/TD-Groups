from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class GroupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    members = StringField('Members', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[])
    submit = SubmitField('Submit')