from pathlib import Path
import pytest

FIXTURES=Path(__file__).parent/'fixtures'
TESTTREE=FIXTURES/'testtree'

class Namespace(): pass

@pytest.fixture
def testtree(): return TESTTREE

@pytest.fixture
def relpath(testtree): return lambda path: path.relative_to(testtree)

@pytest.fixture
def q(testtree):
    """Provide short names for short testpaths"""
    paths=Namespace
    paths.testtree=testtree
    paths.R     = testtree/".bch"
    paths.G     = testtree/"good/.bch"
    paths.GA    = testtree/"good/A/.bch"
    paths.A     = testtree/"good/A/.bch"
    paths.GAA   = testtree/"good/A/A/.bch"
    paths.AA    = testtree/"good/A/A/.bch"
    paths.GB    = testtree/"good/B/.bch"
    paths.B     = testtree/"good/B/.bch"
    paths.GBB   = testtree/"good/B/B/.bch"
    paths.BB    = testtree/"good/B/B/.bch"
    return paths

