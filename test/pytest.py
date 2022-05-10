import sys
sys.path.append('..')
from import_abc import child

def test_greek():
    assert import_abc.r.geeks == "child class"
