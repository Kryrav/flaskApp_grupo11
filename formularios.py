from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FormAgregarTareas (FlaskForm):
    titulo =  StringField('Titulo', validators=[DataRequired()])
    enviar  = SubmitField('Enviar')
    