from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class EditNoteForm(FlaskForm):
    note_title= StringField('Note Title', validators=[DataRequired()])
    note_content= StringField('Note Content', widget=TextArea(),validators=[DataRequired()])
    submit = SubmitField('Submit Note')

