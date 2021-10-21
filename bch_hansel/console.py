import sys
from pathlib import Path

from bch_hansel.util import parse_args, isopt

import bch_hansel as XX

USAGE_HANSEL="""
        USAGE:
            bch-hansel [OPTION] [PATH ...]

        DESCRIPTION:
            list all [./bch] directories reachable from any
            of the PATH arguments.

        OPTIONS:
            --dev   include any mounted devices in the list.
            --home  include the home directory in the list
            --all   combines --dev and --home

            The options cannot be mixed.

        ENVIRONMENT:
            BCH_POETRY_HANSEL_MOUNT

            Path to the host mount directory, where the
            devices are mounted. . E.g.
                /Volumes        in macos
                /media/$USER    in pi
    """

def lfilter(*a,**b): return list(filter(*a,**b))

def adh_parse(args):
    if   args[0] == '--all':  dev,home = True,  True  ; args.pop(0)
    elif args[0] == '--dev' : dev,home = True,  False ; args.pop(0)
    elif args[0] == '--home': dev,home = False, True  ; args.pop(0)
    else:                     dev,home = False, False ;  None
    return args,dev,home

def hansel():
    args=parse_args(sys.argv,USAGE_HANSEL)
    args,dev,home = adh_parse(args)
    if len(lfilter(isopt,args)) > 0: exit('bad options. try -h.')
    for path in XX.gathers(args,dev=dev,home=home):
        print(path)

def find():
    args=parse_args(sys.argv,"usage stub for find")
    args,dev,home = adh_parse(args)
    if not (args and args[0]=='-t'):
        exit('Missing -t')
    args.pop(0)
    target=args.pop(0)
    for path in XX.find(roots=args, target=target, dev=dev, home=home):
        print(path)
