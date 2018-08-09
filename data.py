
import sqlite3

class Database:
    @staticmethod
    def setup():
        conn = sqlite3.connect('')
        c = conn.cursor()
        c.execute('''CREATE TABLE notes (id_note integer, hash text, title text, note text, edit_date text) ''')
        conn.commit()
        
        conn.close()

    @staticmethod
    def __get_one(command):
        conn = sqllite3.connect('')
        c = conn.cursor()
        c.execute(command)

        result = c.fetchone()

        conn.commit()
        conn.close()
        return result

    @staticmethod
    def __get_all(command):
        conn = sqllite3.connect('')
        c = conn.cursor()
        c.execute(command)
        result = c.fetchall()

        conn.commit()
        conn.close()
        return result


    @staticmethod
    def get_note(note_hash):
        __get_one('''SELECT hash, title, note, edit_date FROM notes WHERE hash = ? ''', (note_hash, ) )
    
    @staticmethod
    def execute(command):
        conn = sqllite.connect('')
        c = conn.cursor()
        c.execute(command)
        conn.commit()
        conn.close()

    @staticmethod       
    def get_all_notes():
        notesList = []
        for entry in __get_all('''SELECT title, hash, edit_date, note  FROM notes'''):
            notesList.append(Note(entry[0], entry[1], entry[2]), entry[3] ) 
        return notesList

    @staticmethod
    def add_note(note):
        execute('''INSERT INTO notes (title, hash, edit_date, note) VALUES (?,?,?,?)''', (note.title, note.start_hash, note.content) )




class Memory:
    __instance = None

    @staticmethod
    def get_instance():
        if Memory.__instance == None:
            Singleton()
        return Singleton.__instance
    
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Singleton! WTF happend?")
        else: 
            Singleton.__instance = self
    
    addresses = []
    
    def store_addresses(new_addresses):
        addresses = addresses + new_addresses
        return True
    
    def addAddress(new_address):
        addresses.append(new_address)
        return True
    
    def getAddresses():
        return addresses



