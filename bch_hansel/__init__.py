#!/usr/bin/env python3
import os
from pathlib import Path

MOUNT_ENV_KEY='BCH_POETRY_HANSEL_MOUNT'

def gather(path):
    bch = '.bch'
    path=Path(path)
    if (path/bch).exists():
        yield path/bch
        for child in path.glob('*'):
            yield from gather(child)

def gathers(roots, home=None, dev=None):
    if dev:  roots = devices() + roots
    if home: roots = [ Path.home() ] + roots
    for root in roots:
        yield from gather(root)

def _find(target,roots,home=None,dev=None):
    for root in gathers(roots,home=home,dev=dev):
        if (root/target).exists():
            yield root/target
def find(target,roots,home=None,dev=None):
    return list(_find(target,roots,home=None,dev=None))
def devices():
    mp = mount()
    if mp and mp.is_dir():
        return list(mp.glob('*'))
    else:
        return []

def mount():
    mp=os.environ.get(MOUNT_ENV_KEY)
    if mp: mp=Path(mp)
    return mp
