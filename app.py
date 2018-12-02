from flask import Flask
from flask import request
from storage.data import *
from communicator import *
from note import Note
import json

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/greet')
def greet():
    return 'hey' if Communicator.welcome(request.remote_addr) else 'sorry'    
     
@app.route('/hashes', methods=['GET'])
def acquire():
    return json.dumps( Communicator.get_notes_hash())
        
@app.route('/dates', methods=['GET'])
def notes_time(hashes): 
    return json.dumps( (hash(Communicator.get_notes_dates()), Communicator.get_notes_dates() ) )

@app.route('/notes', methods=['GET'])
def get_notes(): 
    return json.dumps( Communicator.get_notes() )


@app.route('/notes', methods=['POST'])
def add_notes():
    Communicator.synchronize(json.dumps(request.get_json()))  
    

