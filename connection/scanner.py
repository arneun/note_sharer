
import socket
import request
import asyncio
import ipaddress

class Scanner:

    def getIP(self):
        myIP = ipaddress.ip_address( socket.gethostbyname(socket.gethostname()) )
        return myIP
    
    
    def addresses_in_subnet(self, host_ip):
        ipaddress.ip_network(host_ip)



    def scanAll(self):
        
        





