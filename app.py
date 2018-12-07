from flask import Flask, request, render_template, redirect
from flask import request
from storage.data import *
from communicator import *
from note import Note
from forms.add_note import NoteForm
from config import Config
import json


app = Flask(__name__)
app.config.from_object(Config)






@app.route('/notes', methods=['GET', 'POST'])
def get_main_page():
    form = NoteForm()
    
    if form.validate_on_submit():
        Communicator.add_note(form.note_title.data,form.note_content.data)
        return redirect('/notes')
    
    return render_template('notes.html', form=form, notes=Communicator.get_notes()) 


@app.route('/api/greet')
def greet():
    return 'hey' if Communicator.welcome(request.remote_addr) else 'sorry'    
     
@app.route('/api/hashes', methods=['GET'])
def acquire():
    return json.dumps( Communicator.get_notes_hash())
        
@app.route('/api/dates', methods=['GET'])
def notes_time(hashes): 
    return json.dumps( (hash(Communicator.get_notes_dates()), Communicator.get_notes_dates() ) )

@app.route('/api/notes', methods=['GET'])
def get_notes(): 
    return json.dumps( Communicator.get_notes() )


@app.route('/api/notes', methods=['POST'])
def add_notes():
    Communicator.synchronize(json.dumps(request.get_json()))  
    

