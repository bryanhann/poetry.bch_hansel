from tests.conftest import FIXTURES
from tests.lib.tools import RunCase, Result
from textwrap import dedent

case1=RunCase( "bch-hansel", ['testtree'], cd=FIXTURES )
case1.exp=Result()
case1.exp.stdout=dedent("""\
        testtree/.bch
        testtree/good/.bch
        testtree/good/A/.bch
        testtree/good/A/A/.bch
        testtree/good/B/.bch
        testtree/good/B/B/.bch
        """)

def test_case1():
    case1.run().assert_pass()

def test_case2():
    RunCase(
        "bch-hansel",
        ['/dev/null']
    ).run().assert_pass()

