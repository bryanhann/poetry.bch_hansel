import sys
from pathlib import Path
import bch_hansel as XX

from bch_hansel.util import parse_args

dL = XX.devices()
hL = [ Path.home() ]
aL = hL + dL

USAGE_HANSEL="""
        USAGE:
            bch-hansel [-d] [-h] [a] [PATH ...]

        DESCRIPTION:
            list all [./bch] directories reachable from any
            of the PATH arguments.

        OPTIONS:
            -d   include any mounted devices in the list.
            -h   include the home directory in the list
            -a   combines -d and -h

        ENVIRONMENT:
            BCH_POETRY_HANSEL_MOUNT

            Path to the host mount directory, where the
            devices are mounted. . E.g.
                /Volumes        in macos
                /media/$USER    in pi
    """

def hansel():
    args=parse_args(sys.argv,USAGE_HANSEL)
    acc = []
    for arg in args:
        if   arg=='-d' : acc = acc + XX.devices()
        elif arg=='-h' : acc = acc + [ Path.home() ]
        elif arg=='-a' : acc = acc + [ Path.home() ] + XX.devices()
        else:            acc = acc + [arg]
    for path in XX.gathers(acc):
        print(path)
