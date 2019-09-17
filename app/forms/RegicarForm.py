from wtforms import StringField, Form
from wtforms.validators import DataRequired, ValidationError, Length, Email
from app.models.vehicles import Vehicles


class RegicarForm(Form):
        vehiclePlate = StringField('vehiclePlate', validators=[DataRequired()])
        brand = StringField('brand', validators=[DataRequired()])
        email = StringField('email', validators=[DataRequired(), Length(1, 64), Email(message='invalid email address')])
        type=StringField('type',validators=[DataRequired()])

        def validate_vehiclePlate(self, field):
            if Vehicles.query.filter_by(vehiclePlate=field.data).first():
                raise ValidationError('vehiclePlate has already been used')


class DeletecarForm(Form):
    vehiclePlate = StringField('vehiclePlate', validators=[DataRequired()])

