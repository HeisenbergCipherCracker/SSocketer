import socket
import os
import sys
sys.path.append(os.getcwd())

def udp_init():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return sock