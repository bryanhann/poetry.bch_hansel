import bch_hansel
import sys
def hansel():
    for path in bch_hansel.gather(sys.argv[1]):
        print(path)
