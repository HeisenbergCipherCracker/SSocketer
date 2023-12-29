import socket

def get_own_ip():
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.connect(("8.8.8.8", 80))

        own_ip = sock.getsockname()[0]

        return str(own_ip)

    finally:
        sock.close()
