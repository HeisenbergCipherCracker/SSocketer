import nmap
import json
import os
import sys
sys.path.append(os.getcwd())
from lib.datastruct.nmapcap import Nmapcap
from lib.datastruct.sockdict import Sockdict
from lib.cmdhandler.cmdhandler import nmap as _nmap
from lib.cmdhandler.cmdhandler import target as _target



def pynmap(target=_target):
    if _nmap is not None:
        """
        >>> print(pynmap("scanme.org"))
        """
        nm = nmap.PortScanner()
        port_range = '1-1000'

        nm.scan(target, arguments=f'-p {port_range}')
        port_range = '1-1000'

        nm.scan(target, arguments=f'-p {port_range}')
        for host in nm.all_hosts():
            print(f"Open ports for {host}:")
            for proto in nm[host].all_protocols():
                ports = nm[host][proto].keys()
                for port in ports:
                    if nm[host][proto][port]['state'] == 'open':
                        print(f"Port {port}: {nm[host][proto][port]['name']}")
                        caps = Nmapcap()
                        Caps = Sockdict()
                        caps.save_nmap_datas(nm[host][proto][port]['name'])
                        Caps.set_address_of_socket(host, port)
                        return Caps

