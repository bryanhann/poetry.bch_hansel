import sys
from textwrap import dedent

def parse_args(args,block):
    args=sys.argv[1:]
    if not args or args[0] in '-h --help'.split():
        exit(print(dedent(block)))
    return args
