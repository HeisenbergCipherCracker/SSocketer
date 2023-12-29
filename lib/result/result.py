import os
import sys

sys.path.append(os.getcwd())
from lib.cmdhandler.cmdhandler import outfile
from lib.TCP.socketpacket import send_socket_with_specified_size

def result(filename=outfile):

    with open(filename, 'w') as file:
        file.write(send_socket_with_specified_size()[0].decode()) if send_socket_with_specified_size() is not None else "None" 




# result()