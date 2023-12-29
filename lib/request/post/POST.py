import socket
import os
import sys
sys.path.append(os.getcwd())
from lib.TCP.tcpsocketinit import TCP_sock_init

def decoy():
    pass

def POST(address,content):
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
        return data.decode()