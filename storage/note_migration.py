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
            self.db.execute_args('''UPDATE notes SET note = ?, edit_date = ?  WHERE hash = ?''', (note.content, datetime.datetime.now().isoformat()[:19],note.start_hash))
   
    def update_note_by_id(self, note):
        self.db.execute_args('''UPDATE notes SET title = ?, edit_date = ?, note = ? WHERE id_note = ? ''',(note.title, note.edit_date,note.content, note.number)  )

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

    def get_note_id(self, id_note):
        row = self.db.get_one_where('''SELECT title, hash, edit_date, note, id_note FROM notes WHERE id_note = (?) ''', (id_note))
        return Note(row[0],row[1],row[2], row[3], row[4])


    def add_note(self, note):
        self.db.execute_args('''INSERT INTO notes (title, hash, edit_date, note) VALUES (?,?,?,?)''', (note.title, str( note.start_hash), datetime.now().isoformat()[:19], note.content) )
    
    def add_notes(self, notes):
        command = '''INSERT INTO notes (title, hash, edit_date, note) VALUES (?,?,?,?)'''
        notes_to_add = [(note.title, note.start_hash, note.edit_date, note.content)  for note in notes]
        
        self.db.execute_many(command, notes)
    
    def get_note_hash(self, note_hash):
        self.db.get_one('''SELECT id_note, hash, title, note, edit_date FROM notes WHERE hash = ? ''', (note_hasha))
    





