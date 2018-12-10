from storage.data import Database



class AddressData:
    def __init__(self):
        self.db = Database()

    def add_address(self, ip_addr, auth_token):
        self.db.execute_args('''INSERT INTO addresses (ip_address) VALUES (?)''', (ip_addr))

    def add_addresses(self, ip_addresses, auth_token, access_token):
        command = '''INSERT INTO addresses (ip_address) VALUES (?)'''
        addresses = [(i, ) for i in ip_addresses]
        
        self.db.executemany(command, addresses)

    def get_addresses(self):
        addresses = []
        for entry in self.db.get_all('''SELECT ip_address FROM addresses'''):
            addresses.append(entry[0])
        return addresses


    def upd_auth_token(self, ip_address, token):
        
        self.db.execute_args('''UPDATE addresses SET access_token = ? WHERE ip_address = ?''', (ip_address, token))

    def flush_connections(self):
        self.db.execute('''DELETE FROM addresses''')

