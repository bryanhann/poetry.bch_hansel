import sys
from pathlib import Path

from bch_hansel.util import lfilter
from bch_hansel.util import isopt
from bch_hansel.util import parse_args

from bch_hansel.usage import USAGE_HANSEL

from bch_hansel.parse import parse_dh
from bch_hansel.parse import parse_t

from bch_hansel import gathers

def hansel():
    args=parse_args(sys.argv,USAGE_HANSEL)
    args,target = parse_t(args)
    args,dev,home = parse_dh(args)
    options = lfilter(isopt,args)
    if len(options) > 0:
        exit('bad options. try -h.')

    for path in gathers(args,dev=dev,home=home):
        if not target:
            print(path)
        else:
            if (path/target).exists():
                print( path/target )
