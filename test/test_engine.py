from ast import Num
from test_csv import csv
from test_data import DataTest
from test_numeric import test_num, test_bignum
from test_stats import TestStat
from test_bad import bad
from test_list import test_list
from test_sym import test_eg_sym, test_eg_the
from test_ls import ls
from test_all import all_tests

class TestEngine:

    eg = {
        'BAD': bad(),
        'LIST': test_list(),
        'LS': ls(),
        'ALL': all_tests(),
        'the': test_eg_the(),
        'sym': test_eg_sym(),
        'num': test_num(),
        'bignum': test_bignum(),
        'csv': csv(),
        'data': DataTest(),
        'stats': TestStat() 
    }  

    def __init__(self) -> None:
        self.fails = 0
        self.eg = {}

    def runs(k):
        if k not in eg:
            return 
        old = {}
        for key, value in test_eg_the.items():
            old[key] = value
        if test_eg_the('dump'):
            status == True
            out = eg[k]
        else:
            status == False
                
            #//Apply some error catching
        for key, value in old.items():
            value = test_eg_the(key) 
        msg = status and ((out == True and 'PASS') or 'FAIL') or 'CRASH'
        print("!!!!!!", msg, k, status)
        return out or err 