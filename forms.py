from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators
from wtforms.fields.core import FloatField
from wtforms.fields.simple import FileField
from wtforms.validators import DataRequired, NumberRange


class MealForm(FlaskForm):
    article = StringField('article', validators=[DataRequired()])
    form = StringField('form', validators=[DataRequired()])
    meat = StringField('meat', validators=[DataRequired()])
    salad1 = StringField('salad1', validators=[DataRequired()])
    salad2 = StringField('salad2', validators=[DataRequired()])
    sauce = StringField('sauce', validators=[DataRequired()])
    price = FloatField('price', validators=[DataRequired()])
