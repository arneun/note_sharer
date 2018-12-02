
import socket
import asyncio
import ipaddress
import netifaces
from data import Memory


class Scanner:
    
    def __get_net_addr(ip, mask):
        return ipaddress.ip_adress(int(ip) & int(netmask))

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



    async def scan_all(self):
        (ip, mask) = get_ip()
        adresses = addresses_in_subnet(__get_net_addr(ip, mask), mask)
        adresses.remove(ip)
        
    async def check(self):
        pass




