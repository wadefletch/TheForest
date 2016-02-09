from flask.ext.wtf import Form
from wtforms import BooleanField, StringField
from wtforms.validators import DataRequired


class DefaultForm(Form):
    field1 = StringField('Field 1', validators=[DataRequired()])
    field2 = BooleanField('Field 2')
