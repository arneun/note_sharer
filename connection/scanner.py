
import socket
import asyncio
import ipaddress
import netifaces

class Scanner:

    def get_ip(self):
        myIP = ('','')
        interfaces = netifaces.interfaces()
        for i in interfaces:
            if i == 'lo':
                continue
            iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
            if iface != None:
                for j in iface:
                    myIP = (j['addr'], j['netmask'])
        return myIP
    
    
    def addresses_in_subnet(self, host_ip, mask):
        
        return ipaddress.ip_network(host_ip + '/' + mask)



    def scan_all(self):
        (ip, mask) = get_ip()
        adresses = addresses_in_subnet(ip, mask)
        adresses.remove(ip)
        





