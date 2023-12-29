import socket
import os
import sys

sys.path.append(os.getcwd())
from lib.TCP.tcpsocketinit import TCP_sock_init

def decoy():
    pass

def get_request(address=tuple):
    try:
        req = f"GET / HTTP/1.1\r\nHost: {address[0]}\r\n\r\n"
        sock = TCP_sock_init()
        sock.connect(address)
        sock.sendall(req.encode())
        data = sock.recv(1024)
        sock.close()
    
    finally:
        return data.decode()
    
print(get_request(("scanme.org",22)))


