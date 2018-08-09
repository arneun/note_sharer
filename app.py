from flask import Flask
from flask import request
from data import *
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
     
@app.route('/get_notes', methods=['GET'])
def acquire():
    return json.dumps( Communicator.get_notes())
        





