import sys

import bch_hansel
from bch_hansel.util import parse_args

USAGE_HANSEL="""
        USAGE:
            bch-hansel [--devices] [PATH ...]

        DESCRIPTION:
            list all [./bch] directories reachable from any
            of the PATH arguments.

        OPTIONS:
            --devices   include any file in DEVICE in the list.

        ENVIRONMENT:
            BCH_POETRY_HANSEL_DEVICES

            Path to the host mount directory. E.g.
                /Volumes        in macos
                /media/$USER    in pi
    """

def hansel():
    args=parse_args(sys.argv,USAGE_HANSEL)
    acc = []
    for arg in args:
        if arg=='--devices':
            acc = acc + bch_hansel.devices()
        else:
            acc.append(arg)
    for path in bch_hansel.gathers(acc):
        print(path)
