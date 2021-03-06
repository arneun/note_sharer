from storage.data import Database
from entities.address import Address


class AddressData:
    def __init__(self):
        self.db = Database()

    def add_address(self, addr_entity):
        self.db.execute_args('''INSERT INTO addresses (ip_address, auth_token, access_token) VALUES (?,?,?)''', (addr_entity.ip_address, addr_entity.auth_token, addr_entity.access_token))

    def add_addresses(self, addresses):
        command = '''INSERT INTO addresses (ip_address, auth_token, access_token) VALUES (?,?,?)'''
        addresses = [(i.ip_address, i.auth_token, i.access_token) for i in addresses]
       
        self.db.executemany(command, addresses)

    def get_addresses(self):
        addresses = []
        for entry in self.db.get_all('''SELECT ip_address FROM addresses'''):
            addresses.append(entry[0])
        return addresses

    def get_address_auth(self, address):
        return self.db.get_one_where('''SELECT ip_address, auth_token WHERE ip_address = ? ''', (address, )  )

    def upd_auth_token(self, ip_address, token):
        self.db.execute_args('''UPDATE addresses SET auth_token = ? WHERE ip_address = ?''', (ip_address, token))

    def upd_access_token(self, ip_address, token):
        self.db.execute_args('''UPDATE addresses SET access_token = ? WHERE ip_address = ?''', (ip_address, token))

    def flush_connections(self):
        self.db.execute('''DELETE FROM addresses''')

    def update_address(self, addr_entity):
        if addr_entity.auth_token is not None:
            self.upd_auth_token(self, addr_entity.auth_token)
        if addr_entity.access_token is not None:
            self.upd_access_token(self, add_entity.access_token)


