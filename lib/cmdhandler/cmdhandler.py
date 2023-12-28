import argparse
import os
import sys


def cmdhandler():
    """
    >>> cmdhandler()
    *returns: target,port,size in order
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--url","-u",type=str,help="specify the target url",required=True)
    parser.add_argument("--port","-p",type=int,help="specify the target port",required=True)
    parser.add_argument("--batch",help="use default setting while performing attack",required=False)
    parser.add_argument("--size","-s",type=int,help="specify the size of the packet",required=False)
    parser.add_argument("--data","-d",type=bytes,help="specify the data to be sent.",required=False)
    parser.add_argument("--range","-r",type=int,help="specify the attack range number",required=False)
    args = parser.parse_args()
    target = args.url
    port = args.port
    size = args.size
    data = args.data
    Range = args.range
    
    return target,port,size,data,Range

target,_,_,_,_ = cmdhandler()
_,port,_,_,_ = cmdhandler()
_,_,size,_,_ = cmdhandler()
_,_,_,data,_ = cmdhandler()
_,_,_,_,Range = cmdhandler()
