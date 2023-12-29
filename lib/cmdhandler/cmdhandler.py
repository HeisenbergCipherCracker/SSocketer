import argparse
import os
import sys

sys.path.append(os.getcwd())

from extra.versioninfo.Version import VERSION

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
    parser.add_argument("--output","-o",help="get result as an output txt file")
    parser.add_argument("--protocol","--proto",help="specify the protocol of the packet sending",default="TCP",required=False,type=str)
    parser.add_argument("--version",help="display the version",action='version',version=f"%(prog)s {VERSION}")
    parser.add_argument("--request","-req",help="send couple of requests type,example : (--request POST)",required=False,type=str)
    parser.add_argument("--content",help="add content for the requests that will be sent",required=False)
    parser.add_argument("--nmap",help="use nmap to find the target open ports",required=False,action="store_true")
    args = parser.parse_args()
    target = args.url
    port = args.port
    size = args.size
    data = args.data
    Range = args.range
    outfile = args.output
    protocol = args.protocol
    request = args.request
    content = args.content
    nmap = args.nmap
    
    return (
        target
        ,port
        ,size
        ,data
        ,Range
        ,outfile,
        protocol,
        request,
        content,
        nmap)

target, port, size, data, Range, outfile,protocol,request,content,nmap = cmdhandler()
