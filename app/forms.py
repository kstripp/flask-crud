#!/usr/bin/env python

from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class NewEntry(Form):

    title = StringField('title', validators=[DataRequired()])
    body = StringField('body', validators=[DataRequired()])
