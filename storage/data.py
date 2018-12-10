import sqlite3
from datetime import datetime
from note import Note


class Database:

    def __init__(self):
        self.database_name = 'storage.db'    

    def setup(self):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE notes (id_note INTEGER PRIMARY KEY NOT NULL, hash TEXT, title TEXT, note TEXT, edit_date TIMESTAMP) ''')
        conn.commit()
        c.execute('''CREATE TABLE addresses(ip_address TEXT, auth_token TEXT, access_token TEXT)''')
        conn.commit()
        
        conn.close()

    def get_one_where(self, command, arguments):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(command, arguments)

        result = c.fetchone()
        
        conn.commit()
        conn.close()
        return result

  

    def get_one(self, command):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(command)

        result = c.fetchone()

        conn.commit()
        conn.close()
        return result

    def get_all(self, command):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(command)
        result = c.fetchall()

        conn.commit()
        conn.close()
        return result


    def execute(self, command):
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute(command)
        conn.commit()
        conn.close()
    
    def execute_args(self, command, arguments):
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

        

