from flask import Flask, request, render_template
from flask import request
from storage.data import *
from communicator import *
from note import Note
import json


app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello, World!'




@app.route('/notes', methods=['GET'])
def get_main_page():
    return render_template('notes.html', notes=Communicator.get_notes()) 
@app.route('/notes', methods=['POST'])
def send_note():
    print(request.form['note_name'],request.form['note_content'])
    Communicator.add_note(request.form['note_name'],request.form['note_content'])

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
    

