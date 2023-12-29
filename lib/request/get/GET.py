import socket
import os
import sys

sys.path.append(os.getcwd())
from lib.TCP.tcpsocketinit import TCP_sock_init
from lib.logger.log import logger
from lib.cmdhandler.cmdhandler import port
from lib.cmdhandler.cmdhandler import target

def decoy():
    pass

def get_request(address:tuple=(target,port)):
    try:
        req = f"GET / HTTP/1.1\r\nHost: {address[0]}\r\n\r\n"
        sock = TCP_sock_init()
        sock.connect(address)
        sock.sendall(req.encode())
        data = sock.recv(4096)
        sock.close()
    
    finally:
        logger.info(data.decode())
    
# print(get_request(("scanme.org",22)))


