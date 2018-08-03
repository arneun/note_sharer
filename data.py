
import sqlite3

class Database:
    def setup():
        conn = sqlite3.connect('')
        c = conn.cursor()
        c.execute(''' CREATE TABLE notes (hash text, title text, note text, edit_date text) ''')
        
        conn.commit()
        conn.close()





class Memory:
    __instance = None

    @staticmethod
    def getInstance():
        if Memory.__instance == None:
            Singleton()
        return Singleton.__instance
    
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Singleton! WTF happend?")
        else: 
            Singleton.__instance = self
    
    addresses = []
    
    def storeAddresses(new_addresses):
        addresses = addresses + new_addresses
        return True
    
    def addAddress(new_address):
        addresses.append(new_address)
        return True
    
    def getAddresses():
        return addresses



