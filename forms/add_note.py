

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NoteForm(FlaskForm):
    note_title= StringField('Note Title', validators=[DataRequired()])
    note_content= StringField('Note Content', validators=[DataRequired()])
    submit = SubmitField('Submit Note')

