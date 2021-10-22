def parse_dh(args):
    if   args[0] == '--all':  dev,home = True,  True  ; args.pop(0)
    elif args[0] == '--dev' : dev,home = True,  False ; args.pop(0)
    elif args[0] == '--home': dev,home = False, True  ; args.pop(0)
    else:                     dev,home = False, False ;  None
    return args,dev,home

def parse_t(args):
    if args[0]=='-t':
        target = args[1]
        args = args[2:]
    else:
        target = None
    return args, target
