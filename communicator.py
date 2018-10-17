from data import *
from note import Note

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
    def get_notes_dates():
        hashes = []
        dates = []
        for note in Communicator.get_notes():
            notes.append(note.start_hash)
            dates.append(dates.edit_date)

        return (hashes, dates)
