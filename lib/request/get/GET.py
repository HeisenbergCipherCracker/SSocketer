import socket
import os
import sys

sys.path.append(os.getcwd())
from lib.TCP.tcpsocketinit import TCP_sock_init
from lib.logger.log import logger
from lib.cmdhandler.cmdhandler import port
from lib.cmdhandler.cmdhandler import target
from lib.cmdhandler.cmdhandler import Range as _range
from lib.cmdhandler.cmdhandler import request

def decoy():
    pass

def get_request(address:tuple=(target,port)):
    if request is not None and request == "GET":
        for _ in range(_range+1 if _range is not None else 1):
            try:
                req = f"GET / HTTP/1.1\r\nHost: {address[0]}\r\n\r\n"
                sock = TCP_sock_init()
                sock.connect(address)
                sock.sendall(req.encode())
                data = sock.recv(4096)
                sock.close()
            
            finally:
                msg = str(data.decode())
                msg += "\n received the above response while sending the POST request."
                logger.info(msg)
    
# print(get_request(("scanme.org",22)))


