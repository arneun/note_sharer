from storage.data import *
from storage.note_migration import NoteData
from connection.scanner import Scanner
from note import Note
import hashlib
from datetime import datetime
import requests
import json



class Notes:
    def __init__(self):
        self.sc = Scanner()
        self.db = NoteData()

    def get_notes_hash(self):
        hashes = []
        for note in self.get_notes():
           hashes.append(note.start_hash)
        
        return hashes

    def get_notes(self):
        return self.db.get_all_notes()

    def synchronize(self,acquired_notes, sender_ip): 
        newer_hasheds = compare_notes(acquired_notes)
        send_notes(Database.get_notes_by_hash(newer_hashes), sender_ip)

    def compare_notes(self, notes):
        stored_notes = self.db.get_notes_hash()
        newer_notes = []
        for note in notes:
            if note.start_hash in stored_notes:
                if note.edit_date < stored_notes[note.start_hash]:
                    self.db.update_note(note)
                else: newer_notes.append(note.start_hash)
        return newer_notes

    def add_note(self, note):
        self.db.add_note(note)
    
    def add_note(self, note_name, note_content):
        nt = Note(note_name, hashlib.sha256(), datetime.now(), note_content)
        self.db.add_note(nt)

    def send_notes(self, note_list, address):
        load = {'json_payload': note_list}
        r = request.post(address + "/notes", data=json.dumps(load))

    def update_note(self, note_id, note_hash, note_title, note_content):
        note = Note(note_title,note_hash, datetime.now().isoformat()[:19], note_content, note_id)
        self.db.update_note_by_id(note)
        


    def get_notes_dates(self):
        hashes = []
        dates = []
        for note in self.get_notes():
            notes.append(note.start_hash)
            dates.append(dates.edit_date)

        return (hashes, dates)

   
    def get_note_by_id(self, note_id):
        return self.db.get_note_id(note_id)


