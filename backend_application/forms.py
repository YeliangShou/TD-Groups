from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class GroupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    members = StringField('Members', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[])
    submit = SubmitField('Submit')

class TransForm(FlaskForm):
    owner = StringField('Owner', validators=[DataRequired()])
    cost = StringField('Cost', validators=[DataRequired()])
    owings = StringField('Owings', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[])
    submit = SubmitField('Submit')