from wtforms import Form, StringField, FloatField
from wtforms.validators import Length,  DataRequired


class SearchForm(Form):
    query=StringField(validators=[DataRequired(),Length(min=1,max=30)])
