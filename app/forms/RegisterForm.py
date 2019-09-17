

from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User






class RegisterForm(Form):
    email = StringField('email', validators=[DataRequired(), Length(1, 64), Email(message='invalid email address')])
    nickname=StringField('nickname',validators= [DataRequired(),Length(2,10,message='At least 2 words')])
    password =PasswordField('password',validators=[DataRequired(),Length(6,20)])

   # def validate_email(self,field):
   #     if User.query.filter_by(email=field.data).first():
   #         raise ValidationError('email address has already been used')
   # def validate_nickname(self,field):
   #     if User.query.filter_by(nickname=field.data).first():
   #         raise ValidationError('nickname exists')

