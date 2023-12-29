import socket
import os
import sys
sys.path.append(os.getcwd())
from lib.TCP.tcpsocketinit import TCP_sock_init
from lib.cmdhandler.cmdhandler import target
from lib.cmdhandler.cmdhandler import port
from lib.cmdhandler.cmdhandler import content
from lib.logger.log import logger

def decoy():
    pass

def POST(address=(target,port),content=content if content is not None else "X"):
    try:
        request_body = content
        content_length = len(request_body)
        request = f"POST /path/to/endpoint HTTP/1.1\r\nHost: {address[0]}\r\nContent-Type: text/plain\r\nContent-Length: {content_length}\r\n\r\n{request_body}"
        sock = TCP_sock_init()
        sock.connect(address)
        sock.sendall(request.encode())
        data = sock.recv(4096)
        sock.close()
    
    finally:
        logger.info(data.decode())