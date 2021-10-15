from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_babel import lazy_gettext

class MyForm(FlaskForm):
	email = StringField(lazy_gettext('Email'), validators=[DataRequired()])