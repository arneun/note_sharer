import sqlite3
from datetime import datetime
from note import Note


class Database:

    def __init__(self):
        self.database_name = 'storage.db'    

    def setup(self):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE notes (id_note integer, hash text, title text, note text, edit_date timestamp) ''')
        conn.commit()
        c.execute('''CREATE TABLE addresses(ip_address text)''')
        conn.commit()
        
        conn.close()

    def __get_one(self, command):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(command)

        result = c.fetchone()

        conn.commit()
        conn.close()
        return result

    def __get_all(self, command):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(command)
        result = c.fetchall()

        conn.commit()
        conn.close()
        return result


    def get_note(self, note_hash):
        self.__get_one('''SELECT hash, title, note, edit_date FROM notes WHERE hash = ? ''', (note_hasha))
    
    def execute(self, command):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(command)
        conn.commit()
        conn.close()
    
    def execute(self, command, arguments):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(command, arguments)
        conn.commit()
        conn.close()

    def executemany(self, command, arg_list):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.executemany(command, arg_list)
        conn.commit()
        conn.close()

    def get_all_notes(self):
        notesList = []
        for entry in self.__get_all('''SELECT title, hash, edit_date, note  FROM notes'''):
            notesList.append(Note(entry[0], entry[1], entry[2], entry[3] )) 
        return notesList

    def update_notes_by_hashes(self, notes):
        for note in notes:
            self.execute('''UPDATE notes SET note = ?, edit_date = ?  WHERE hash = ?''', (note.content, datetime.datetime.now().isoformat()[:19],note.start_hash))
    
    def get_notes_by_hash(self, hashes):
        notes = []
        for note_id in hashes:
            notes.append(self.get_note(note_id))
        return notes

    def get_notes_hash(self):
        notes_dict = {}
        for entry in self.__get_all('''SELECT hash, edit_date FROM notes'''):
            notesList[entry[0]] = entry[1] 
        return notes_dict

    def add_note(self, note):
        self.execute('''INSERT INTO notes (title, hash, edit_date, note) VALUES (?,?,?,?)''', (note.title, str( note.start_hash), datetime.now().isoformat()[:19], note.content) )
    
    def add_notes(self, notes):
        command = '''INSERT INTO notes (title, hash, edit_date, note) VALUES (?,?,?,?)'''
        notes_to_add = [(note.title, note.start_hash, note.edit_date, note.content)  for note in notes]
        
        self.execute(command, notes)
    
    def add_address(self, ip_addr):
        self.execute('''INSERT INTO addresses (ip_address) VALUES (?)''', (ip_addr))

    def add_addresses(self, ip_addresses):
        command = '''INSERT INTO addresses (ip_address) VALUES (?)'''
        addresses = [(i, ) for i in ip_addresses]
        
        self.executemany(command, addresses)

    def get_addresses(self):
        addresses = []
        for entry in self.__get_all('''SELECT ip_address FROM addresses'''):
            addresses.append(entry[0])
        return addresses

class Memory:
    __instance = None

    @staticmethod
    def get_instance():
        if Memory.__instance == None:
            Memory()
        return Memory.__instance
    
    def __init__(self):
        if Memory.__instance != None:
            raise Exception("Singleton! WTF happend?")
        else: 
            Memory.__instance = self
        self.addresses = []    

    
    def store_addresses(self, new_addresses):
        self.addresses = self.addresses + new_addresses
        return True
    
    def add_address(self, new_address):
        self.addresses.append(new_address)
        return True
    
    def get_addresses(self):
        return self.addresses



