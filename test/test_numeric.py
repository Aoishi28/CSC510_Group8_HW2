import pytest
from src.Num import Num
from src.utils import *

def test_num():
    num =Num()
    for i in range(1,101):
        num.add(i)

    mid=num.mid()
    div=num.div()

    print(num,div)

    assert (mid>=50 and mid<=52 and div>30.5 and div<32) 

def test_bignum():
    num=Num()
    the[nums]=32
    for i in range(1,1001):
        num.add(i)

    oo(num.nums())

    assert (32==len(num._has))

