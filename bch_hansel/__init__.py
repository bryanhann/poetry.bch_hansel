#!/usr/bin/env python3
import os
from pathlib import Path

MOUNT=os.environ.get('BCH_POETRY_HANSEL_MOUNT')

def gather(path):
    bch = '.bch'
    path=Path(path)
    if (path/bch).exists():
        yield path/bch
        for child in path.glob('*'):
            yield from gather(child)

def gathers(roots):
    for root in roots:
        yield from gather(root)

def devices():
    mp = mount()
    if mp and mp.is_dir():
        return list(mp.glob('*'))
    else:
        return []

def mount():
    mp=os.environ.get(MOUNT)
    mp=BCH_POETRY_HANSEL_MOUNT
    if mp: mp=Path(mp)
    return mp
