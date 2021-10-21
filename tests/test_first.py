from pathlib import Path
from bch_hansel import gather

def test_function__gather2(testtree, q):
    assert sorted(gather(testtree))  == [q.R, q.G, q.GA, q.GB, q.GBB]


