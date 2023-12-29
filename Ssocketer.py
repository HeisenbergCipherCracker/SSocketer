from lib.TCP.socketpacket import send_socket_with_specified_size
from lib.TCP.socketpacket import send_socket as send_socket_tcp
from lib.udp.UDP import send_socket_udp
from lib.udp.UDP import send_socket_with_specified_size_udp
from lib.result.result import result
from lib.extra.banner import banner 
from lib.cmdhandler.cmdhandler import protocol
from lib.cmdhandler.cmdhandler import outfile
from lib.logger.log import logger
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
        if outfile is not None:
            result()
    
    except SystemExit:
        print("QUITTING!!!")
    
    except BrokenPipeError:
        logger.critical("Could not handle that packet size any more. use the default setting.")
    
    except ConnectionResetError as exc:
        logger.critical("Connection reset\n%s"%str(exc))
    
    except:
        traceback.print_exc()

    
    finally:
        if threading.active_count() > 1:
            sys.exit(0)
        
        else:
            os._exit(0)





