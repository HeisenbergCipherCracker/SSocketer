import os
import sys

sys.path.append(os.getcwd())
from lib.TCP.tcpsocketinit import TCP_sock_init
from lib.logger.log import logger
from lib.Exceptions.exceptions import SsocketExcpectedRecBytesNotStr
from lib.cmdhandler.cmdhandler import port
from lib.cmdhandler.cmdhandler import size
from lib.cmdhandler.cmdhandler import target
from lib.cmdhandler.cmdhandler import data

def send_socket(address:tuple=(target,port),data:bytes=data):
    """
    >>> address =('scanme.org',22)

    >>> send_socket(address,'hello world!')
    """
    if not isinstance(data,bytes):
        crmsg = "Expected to get bytes data, not:%s"%"normal bytes" if isinstance(data,str) else "Unknown data"
        logger.critical(crmsg)
        raise SystemExit
    sock = TCP_sock_init()
    sock.connect(address)
    sock.sendall(data)
    datarec = sock.recv(1024)
    msg = "Could receive data: %s"%datarec.decode() if isinstance(datarec,bytes) else datarec
    logger.info(msg)
    sock.close()


def send_socket_with_specified_size(address:tuple=(target,port),data:bytes=data if data is not None else b"X",size:int=size):
    try:
        """
        >>> address =('scanme.org',22)

        >>> send_socket(address,'hello world!')
        """
        if not isinstance(data,bytes):
            crmsg = "Expected to get bytes data, not:%s"%"normal bytes" if isinstance(data,str) else "Unknown data"
            logger.critical(crmsg)
            raise SystemExit
        sock = TCP_sock_init()
        sock.connect(address)
        data *= size
        sock.sendall(data)
        datarec = sock.recv(1024)
        msg = f"\n Sent packet:{size} bytes to target:{address[0]},port:{address[1]}"
        msg += "\nCould receive data: %s"%datarec.decode() if isinstance(datarec,bytes) else datarec
        logger.info(msg)
        sock.close()
    
    except MemoryError as exc:
        msg = str(exc)
        msg += "Could not handle the packet size.EXITING!!!"
        logger.critical(msg)
        raise SystemExit

address =('scanme.org',22)

send_socket_with_specified_size(address=address,data=b"hello world",size=34)
