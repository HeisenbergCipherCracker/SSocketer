import os
import sys

sys.path.append(os.getcwd())
from lib.udp.udpinit import udp_init
from lib.logger.log import logger
from lib.Exceptions.exceptions import SsocketExcpectedRecBytesNotStr
from lib.cmdhandler.cmdhandler import port
from lib.cmdhandler.cmdhandler import size
from lib.cmdhandler.cmdhandler import target
from lib.cmdhandler.cmdhandler import data
from lib.cmdhandler.cmdhandler import Range as _range
from lib.cmdhandler.cmdhandler import request

def send_socket_udp(address:tuple=(target,port),data:bytes=data if data is not None else b'X'):
    if request is None:
        try:
            for i in range((_range+1)//2 if _range is not None else 1):
                """
                >>> address =('scanme.org',22)

                >>> send_socket(address,'hello world!')
                """
                if not isinstance(data,bytes):
                    crmsg = "Expected to get bytes data, not:%s"%"normal bytes" if isinstance(data,str) else "Unknown data"
                    logger.critical(crmsg)
                    raise SystemExit
                sock = udp_init()
                sock.connect(address)
                sock.sendall(data)
                datarec = sock.recv(1024)
                msg = f"\n sent data to the server:{address[0]} via port {address[1]}"
                msg += "\nCould receive data: %s"%datarec.decode() if isinstance(datarec,bytes) else datarec
                logger.info(msg)
                sock.close()
        except MemoryError:
            logger.critical("Out of memory")
            raise SystemExit
        
        except ConnectionRefusedError as exc:
            msg = str(exc)
            msg += "\n^^^Faced with above error:^^^"
            logger.critical(msg)
            raise SystemExit
        


    


def send_socket_with_specified_size_udp(address:tuple=(target,port),data:bytes=data if data is not None else b"X",size:int=size):
    if request is None:
        count = 0
        try:
            for i in range((_range+1)//2 if _range is not None else 1):
                """
                >>> address =('scanme.org',22)

                >>> send_socket(address,b'hello world!')
                """
                if not isinstance(data,bytes):
                    crmsg = "Expected to get bytes data, not:%s"%"normal bytes" if isinstance(data,str) else "Unknown data"
                    logger.critical(crmsg)
                    raise SystemExit
                sock = udp_init()
                sock.connect(address)
                data *= size if size is not None and i == 1 else 1
                sock.sendall(data)
                datarec = sock.recv(1024)
                count += 1
                msg = f"\n [{i}] Sent packet:{data.__sizeof__()} bytes to target:{address[0]},port:{address[1]}"
                msg += "\nCould receive data: %s"%datarec.decode() if isinstance(datarec,bytes) else datarec
                logger.info(msg)
                sock.close()
        
        except (MemoryError,TypeError) as exc:
            msg = str(exc)
            msg += "Could not handle the packet size.EXITING!!!"
            logger.critical(msg)
            raise SystemExit
    




# send_socket_with_specified_size(address=address,data=b"hello world",size=34)
