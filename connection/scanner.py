
import socket
import asyncio
from aiohttp import ClientSession
import ipaddress as ip_addr
import netifaces
import requests
from aiohttp.client_exceptions import ClientConnectorError
from contextlib import suppress

class Scanner:
    
    def get_net_addr(self, ip, mask):
        return ip_addr.ip_address(int(ip) & int(mask))

    def get_ip(self):
        interfaces = netifaces.interfaces()
        for i in interfaces:
            if i == 'lo':
                continue
            iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
            if iface != None:
                for j in iface:
                    myIP = (ip_addr.ip_address(j['addr']),ip_addr.ip_address( j['netmask']))
        return myIP
    
    
    def addresses_in_subnet(self, host_ip, mask):
        return [i for i in ip_addr.ip_network(str(host_ip) + '/' + str(mask)).hosts()]


    def scan_all(self):
        loop = asyncio.get_event_loop()
        (ip, mask) = self.get_ip()
        addresses = self.addresses_in_subnet(self.get_net_addr(ip, mask), mask)
        addresses.remove(ip)
        
        app_instances = []
        
        future = asyncio.ensure_future(self.check_all(addresses))
        responses =loop.run_until_complete(future)
        result = []
        for response in responses:
            if not response is None and response[1] == 'hey':
                result.append(response)
        
        return result
    
    async def fetch(self, ip_address, session):
        with suppress(ClientConnectorError):
            async with session.get('http://' +str(ip_address) + ':5000/greet') as response:
                return (ip_address,await  response.text())

    async def check_all(self, ip_addresses):
        tasks= []

        async with ClientSession() as session:
            for address in ip_addresses:
                task = asyncio.ensure_future(self.fetch(address, session))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)
        return responses

    def check(self, ip_address, session):
        try:
            r = session.get('http://' +str(ip_address) + ':5000/greet', timeout=1 )
            if r.text == 'hey':
                return (ip_address, True)
            else:
                return (ip_address, False)
        except:
            return (ip_address, False)

