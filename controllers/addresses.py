from connection.scanner import Scanner
from storage.addresses_migration import AddressData
from werkzeug.security import generate_password_hash, check_password_hash 
from config import Config
from entities.address import Address as Addr


class Addresses:
    def __init__(self):
        self.sc = Scanner()
        self.db = AddressData()

    def search_for_apps(self):
        res = self.sc.scan_all()
        
        addresses = []
        for response in res:
            addresses.append(Addr(str(response[0], access_token=str(response[1]))))
            
        return self.db.add_addresses(addresses)

    def welcome(self, address):      
        random_number = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))
        auth_hash = generate_password_hash(random_number + Config.USER_NAME)

        return self.db.add_address(address, auth_hash)

    def authenticate(self, address, auth_num):
        return check_password_hash(self.db.get_address_auth(address), auth_num)
    
    def get_addresses(self):
        return self.db.get_addresses()
    
    def set_access(self, address, access_token):
        self.db.upd_access_token(address, access_token)
 
    def flush_addresses(self):
        self.db.flush_connections()

