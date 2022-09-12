import pytest
import re
from src.utils import *
from src.Sym import Sym

def test_eg_the():
    oo(the)
    assert True

def test_eg_sym():
    pairs = dict.fromkeys(["a","a","a","a","b","b","c"])
    sym = Sym()
    for key, value in pairs.items():
        sym.add(value)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000 * entropy) // 1 / 1000
    oo({'mid': mode, 'div': entropy})
    assert mode == "a" and 1.37 <= entropy and entropy <= 1.38




