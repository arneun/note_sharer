
import socket
import asyncio
import ipaddress
import netifaces
from storage.data import Memory


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


    def scan_all(self):
        loop = asyncio.get_event_loop()
        (ip, mask) = get_ip()
        adresses = addresses_in_subnet(__get_net_addr(ip, mask), mask)
        adresses.remove(ip)
        checks = [ip for ip in adresses if self.check(ip)]
        return loop.run_until_complete(asyncio.gather(checks))

    async def check(self, ip_addr):
        r = requests.get('ip_addr' + ':5000/greet')        
        if r.text == 'hey':
            return True
        else: 
            return False



