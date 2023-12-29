import os
import sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)
#Reference:https://stackoverflow.com/questions/11866792/how-to-prevent-errno-32-broken-pipe

sys.path.append(os.getcwd())
from lib.TCP.tcpsocketinit import TCP_sock_init
from lib.logger.log import logger
from lib.Exceptions.exceptions import SsocketExcpectedRecBytesNotStr
from lib.cmdhandler.cmdhandler import port
from lib.cmdhandler.cmdhandler import size
from lib.cmdhandler.cmdhandler import target
from lib.cmdhandler.cmdhandler import data
from lib.cmdhandler.cmdhandler import Range as _range
from lib.cmdhandler.cmdhandler import request

caps = None
tcp_data_cap = None

def send_socket(address:tuple=(target,port),data:bytes=data if data is not None else b'X'):
    if request is None:
        try:
            global tcp_data_cap
            for i in range(_range if _range is not None else 1):
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
                msg = f"\n sent data to the server:{address[0]} via port {address[1]}"
                msg += "\nCould receive data: %s"%datarec.decode() if isinstance(datarec,bytes) else datarec
                logger.info(msg)
                tcp_data_cap = [datarec]
                sock.close()
        except MemoryError:
            logger.critical("Out of memory")
            raise SystemExit
        
        finally:
            # return tcp_data_cap
            pass

    


def send_socket_with_specified_size(address:tuple=(target,port),data:bytes=data if data is not None else b"X",size:int=size):
    if request is None:
        count = 0
        try:
            global caps
            for i in range(_range+1 if _range is not None else 1):
                """
                >>> address =('scanme.org',22)

                >>> send_socket(address,b'hello world!')
                """
                if not isinstance(data,bytes):
                    crmsg = "Expected to get bytes data, not:%s"%"normal bytes" if isinstance(data,str) else "Unknown data"
                    logger.critical(crmsg)
                    raise SystemExit
                sock = TCP_sock_init()
                sock.connect(address)
                data *= size if size is not None else 1
                sock.sendall(data)
                datarec = sock.recv(1024)
                count += 1
                msg = f"\n [{i}] Sent packet:{data.__sizeof__()} bytes to target:{address[0]},port:{address[1]}"
                msg += "\nCould receive data: %s"%datarec.decode() if isinstance(datarec,bytes) else datarec
                caps = [datarec]
                logger.info(msg)
                sock.close()
        
        except (MemoryError,TypeError) as exc:
            msg = str(exc)
            msg += "\nCould not handle the packet size.EXITING!!!"
            logger.critical(msg)
            raise SystemExit
        
        finally:
            # return caps
            pass



    




# send_socket_with_specified_size(address=address,data=b"hello world",size=34)
