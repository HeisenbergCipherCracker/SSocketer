import sys

try:
    __import__("lib")
except (ImportError,ModuleNotFoundError) as exc:
    sys.exit("[!]Wrong installation:%s "%str(exc))

from lib.TCP.socketpacket import send_socket_with_specified_size
from lib.TCP.socketpacket import send_socket as send_socket_tcp
from lib.udp.UDP import send_socket_udp
from lib.udp.UDP import send_socket_with_specified_size_udp
from lib.extra.banner import banner 
from lib.cmdhandler.cmdhandler import protocol
from lib.cmdhandler.cmdhandler import outfile
from lib.cmdhandler.cmdhandler import request
from lib.request.get.GET import get_request
from lib.logger.log import logger
from lib.cmdhandler.cmdhandler import nmap
import nmap as _nmap
import threading
import os
import traceback


print(banner)

def main():
    if protocol == "TCP" or protocol == "tcp":
        threads = [send_socket_with_specified_size(),send_socket_tcp()]
        for thread in threads:
            _ = threading.Thread(thread)
            _.start()
            _.join()
    
    elif protocol == "UDP" or protocol == "udp":
        threads = [send_socket_udp(),send_socket_with_specified_size_udp()]
        for thread in threads:
            _ = threading.Thread(thread)
            _.start()
            _.join()
    
    if nmap is not None:
        from lib.pynmap.pynmaps import pynmap
        pynmap()
    
    elif request == "GET":
        get_request()

    


if __name__ == "__main__":
    try:
        main()
        if outfile is not None:
            from lib.result.result import result
            result()
    
    except SystemExit:
        print("QUITTING!!!")
    
    except BrokenPipeError:
        logger.critical("Could not handle that packet size any more. use the default setting.")
    
    except ConnectionResetError as exc:
        logger.critical("Connection reset\n%s"%str(exc))
    
    except _nmap.nmap.PortScannerError():
        logger.critical("PortScannerError.cannot run nmap right now.")
    
    except:
        traceback.print_exc()


    
    finally:
        if threading.active_count() > 1:
            sys.exit(0)
        
        else:
            os._exit(0)





