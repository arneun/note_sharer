from storage.data import *
from note import Note

import requests
import json



class Communicator:
    def search_for_apps():
        pass

    @staticmethod
    def get_notes_hash():
        hashes = []
        for note in Communicator.get_notes():
           hashes.append(note.start_hash)
        
        return hashes

    @staticmethod
    def get_notes():
        return Database.get_all_notes()

    @staticmethod
    def welcome(addres):
        mem = Memory.get_instance()
        return mem.add_address(addres)
    
    @staticmethod
    def synchronize(acquired_notes, sender_ip): 
        newer_hasheds = compare_notes(acquired_notes)
        send_notes(Database.get_notes_by_hash(newer_hashes), sender_ip)

    @staticmethod
    def compare_notes(notes):
        stored_notes = Database.get_notes_hash()
        newer_notes = []
        for note in notes:
            if note.start_hash in stored_notes:
                if note.edit_date < stored_notes[note.start_hash]:
                    Database.update_note(note)
                else: newer_notes.append(note.start_hash)
        return newer_notes

    @staticmethod
    def send_notes(note_list, address):
        load = {'json_payload': note_list}
        r = request.post(address + "/notes", data=json.dumps(load))
        

    @staticmethod
    def get_notes_dates():
        hashes = []
        dates = []
        for note in Communicator.get_notes():
            notes.append(note.start_hash)
            dates.append(dates.edit_date)

        return (hashes, dates)
