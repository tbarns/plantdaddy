from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PlantSearchForm(FlaskForm):
    query = StringField('Search for a plant', validators=[DataRequired()])
    submit = SubmitField('Search')
