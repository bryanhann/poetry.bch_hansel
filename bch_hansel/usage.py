import textwrap

USAGE_HANSEL="""
    USAGE:
        bch-hansel [ -t {TARGET} ] [ --all | --home | --dev ] [PATHLIST]

    DEFINITIONS:
        A *crumb* is a file or directory named [.bch]
        A directory is *marked* if it contains a crumb.
        A directory is *reachable* if it is marked and
            (i) it is in the PATH list, or
            (ii) it's parent is a reachable.

    OUTPUT:
        If {TARGET} is omitted:
            Print the path [{D}/.bch] for each reachable [{D}].
        Otherwise:
            Print the path [{D}/.bch/target] for each reachable
            [{D}] if the path exists.

    OPTIONS:
        -t  {TARGET}    restrict results as described.
        --home          add user's home directorey to the path list
        --dev           add mounted devices to the path lists.
        --all           comine --home and --dev

    ENVIRONMENT:
        BCH_POETRY_HANSEL_MOUNT

        Path to the directory on which devices are mounted.
        The option [--dev] will add each item in this directory
        to the pathlist. If variable is unset or points to a
        nonexistant path, no item will be added.
    """

USAGE_HANSEL=textwrap.dedent(USAGE_HANSEL)
