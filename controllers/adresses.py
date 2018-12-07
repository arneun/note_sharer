from connection.scanner import Scanner
from storage.addresses_migration import AddressData

class Addresses:
    def __init__(self):
        self.sc = Scanner()
        self.db = AddressData()

    def search_for_apps(self):
        res = self.sc.scan_all()
        
        addresses = []
        for response in res:
            addresses.append(str(response[0]))
        self.db.add_addresses(addresses)

    def welcome(self, address):      
        return self.db.add_address(address)
    
    def get_addresses(self):
        return self.db.get_addresses()


    def flush_addresses(self):
        pass

