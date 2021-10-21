#!/usr/bin/env python3

from pathlib import Path
CFG='.config/lbin.bch.hansel/host.mountpoint'

class ExcHansel(Exception): pass

def mountpoint():
    cfg = Path.home()/CFG
    if not cfg.is_file():
        raise ExcHansel( f'\n\tMissing config file: [{cfg}]' )
    try:
        text = Path( cfg.read_text().strip() )
        mp = Path( cfg.read_text().strip() )
    except:
        raise ExcHansel( f'\n\tConfig file contains unpathable string [{repr(text)}]')
    if not mp.is_dir():
        raise ExcHansel( f'\n\tHost has no directory at mountpoint [{repr(str(mp))}]' )
    return mp
