import os
import sys

sys.path.append(os.getcwd())
from lib.cmdhandler.cmdhandler import outfile

def result(filename=outfile):

    with open(filename, 'w') as file:
        for line in file:
            print(line)