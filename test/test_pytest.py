import sys
import os
sys.path.append('..')
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import import_abc

def test_greek():
    assert import_abc.r.geeks == "child class"
