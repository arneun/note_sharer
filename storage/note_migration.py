from storage.data import Database
from note import Note
from datetime import datetime

class NoteData:
    def __init__(self):
        self.db = Database()

    def get_all_notes(self):
        notesList = []
        for entry in self.db.get_all('''SELECT title, hash, edit_date, note, id_note  FROM notes'''):
            notesList.append(Note(entry[0], entry[1], entry[2], entry[3], entry[4] )) 
        return notesList

    def update_notes_by_hashes(self, notes):
        for note in notes:
            self.db.execute('''UPDATE notes SET note = ?, edit_date = ?  WHERE hash = ?''', (note.content, datetime.datetime.now().isoformat()[:19],note.start_hash))
    
    def get_notes_by_hash(self, hashes):
        notes = []
        for note_id in hashes:
            notes.append(self.get_note(note_id))
        return notes

    def get_notes_hash(self):
        notes_dict = {}
        for entry in self.db.get_all('''SELECT hash, edit_date FROM notes'''):
            notesList[entry[0]] = entry[1] 
        return notes_dict

    def add_note(self, note):
        self.db.execute('''INSERT INTO notes (title, hash, edit_date, note) VALUES (?,?,?,?)''', (note.title, str( note.start_hash), datetime.now().isoformat()[:19], note.content) )
    
    def add_notes(self, notes):
        command = '''INSERT INTO notes (title, hash, edit_date, note) VALUES (?,?,?,?)'''
        notes_to_add = [(note.title, note.start_hash, note.edit_date, note.content)  for note in notes]
        
        self.db.execute(command, notes)
    





