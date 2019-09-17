from wtforms import StringField,Form
from wtforms.validators import DataRequired


class videoForm(Form):
    videoname = StringField('videoname', validators=[DataRequired()])

class detectForm(Form):
    inputpath= StringField('inputpath', validators=[DataRequired()])
    outputpath= StringField(' outputpath', validators=[DataRequired()])
    videoname= StringField('videoname', validators=[DataRequired()])
