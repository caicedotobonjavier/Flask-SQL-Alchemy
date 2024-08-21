from flask_wtf import FlaskForm
#
from wtforms.validators import DataRequired
#
from wtforms import StringField, BooleanField, DateField, SubmitField, IntegerField, EmailField


class PersonaForm(FlaskForm):
    nombres = StringField('Nombres', validators=[DataRequired()])
    apellidos = StringField('Apellidos', validators=[DataRequired()])
    edad = IntegerField('Edad', validators=[DataRequired()])
    activo = BooleanField('Activo', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha Nacimiento', validators=[DataRequired()])
    email = EmailField('Correo Electronico', validators=[DataRequired()])
    enviar = SubmitField('Enviar')