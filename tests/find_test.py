import pytest
import bch_hansel as XX
def FN(target,roots): return XX.find(target=target, roots=roots)

class Namespace: pass
@pytest.fixture
def r(q,testtree):
    """root lists for find"""
    xx=Namespace()
    xx.R = testtree
    xx.A   = testtree/'good/A'
    xx.B   = testtree/'good/B'
    return xx

def test__find_apples(q,r):     assert FN('apple',  [r.R]     ) == [q.G/'apple'  , q.AA/'apple'  ]
def test__find_bananas(q,r):    assert FN('banana', [r.R]     ) == [q.G/'banana' , q.BB/'banana' ]
def test__find_figs(q,r):       assert FN('fig',    [r.R]     ) == [q.AA/'fig'   , q.BB/'fig'    ]
def test__find_fig_on_A(q,r):   assert FN('fig',    [r.A]     ) == [q.AA/'fig'                   ]
def test__find_fig_on_B(q,r):   assert FN('fig',    [r.B]     ) == [q.BB/'fig'                   ]
def test__find_figs_on_AB(q,r): assert FN('fig',    [r.A,r.B] ) == [q.AA/'fig', q.BB/'fig'      ]
def test__find_figs_on_BA(q,r): assert FN('fig',    [r.B,r.A] ) == [q.BB/'fig', q.AA/'fig'      ]

def test__find__order_matters(q,r):
    ab = FN( 'fig', [r.A, r.B] )
    ba = FN( 'fig', [r.B, r.A] )
    assert not ab==ba
    assert sorted(ab)==sorted(ba)

