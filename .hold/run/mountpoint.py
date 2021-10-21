import sys
import importlib
from lbin.bch.__bch__ import BCH

BCH._register_file(__file__)

USAGE=f""" USAGE:\n\t{BCH.fname}\nDESCRIPTION:\n\tfoo\n"""

def main():
    if len(sys.argv)>1:
        sys.stderr.write(USAGE)
    else:
        print(BCH.dimport('.config').mountpoint())

main()
