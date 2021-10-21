#!/usr/bin/env python3
from pathlib import Path
dot = '.bch'
def gather(path):
    path=Path(path)
    if (path/dot).exists():
        yield path/dot
        for child in path.glob('*'):
            yield from gather(child)


