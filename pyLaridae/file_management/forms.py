# -*- coding: utf-8 -*-
"""File Management forms."""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired


class AddFileForm(FlaskForm):
    """File Upload form."""

    file = FileField(validators=[FileRequired()])
    file_name = StringField("File Name", validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(AddFileForm, self).__init__(*args, **kwargs)

    def validate(self):
        """Validate the form."""
        initial_validation = super(AddFileForm, self).validate()
        if not initial_validation:
            return False
