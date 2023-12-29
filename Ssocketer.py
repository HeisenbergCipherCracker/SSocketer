from lib.TCP.socketpacket import send_socket_with_specified_size
from lib.TCP.socketpacket import send_socket as send_socket_tcp
from lib.udp.UDP import send_socket_udp
from lib.udp.UDP import send_socket_with_specified_size_udp
from lib.extra.banner import banner 
from lib.cmdhandler.cmdhandler import protocol
import threading
import os
import sys
import traceback


print(banner)

def main():
    if protocol == "TCP":
        threads = [send_socket_with_specified_size(),send_socket_tcp()]
        for thread in threads:
            _ = threading.Thread(thread)
            _.start()
            _.join()
    
    elif protocol == "UDP":
        threads = [send_socket_udp(),send_socket_with_specified_size_udp()]
        for thread in threads:
            _ = threading.Thread(thread)
            _.start()
            _.join()

    


if __name__ == "__main__":
    try:
        main()
    
    except SystemExit:
        print("QUITTING!!!")
    
    except:
        traceback.print_exc()

    
    finally:
        if threading.active_count() > 1:
            sys.exit(0)
        
        else:
            os._exit(0)





