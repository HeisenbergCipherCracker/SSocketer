import socket


def TCP_sock_init():
    return socket.socket(socket.AF_INET,socket.SOCK_STREAM)
