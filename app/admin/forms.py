##

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class FormCrearProducto(FlaskForm):

    nombreProducto = StringField('',validators=[DataRequired(),Length(max=45)])

    precio = FloatField('',validators=[DataRequired()])

    descripcion = TextAreaField('',validators=[DataRequired(),Length(max=250)])

    submit = SubmitField('crear')
    
    #solo para actualizar datos
    submitU = SubmitField('Actualizar')
