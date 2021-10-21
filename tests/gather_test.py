from bch_hansel import gather

def test_testtree(testtree, q):
    assert sorted(gather(testtree))  == [q.R, q.G, q.GA, q.GB, q.GBB]

