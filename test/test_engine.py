import re
from src.Sym import Sym
from src.Num import Num
from src.data import Data
from src import utils
from src.utils import *


class TestEngine:

    def __init__(self) -> None:
        self.fails = 0
        self.eg = [method for method in dir(TestEngine) if method.startswith('test_') is True]

    def all_tests(self) -> bool:
        for k in(self.eg):
            if not self.runs(k):
                fails=fails+ 1 
        return True

    def test_ls(self) -> bool:
        print("\nLS Test Functions:")
        print(self.eg)
        return True

    def test_list(self):
        return sorted(self.eg)

    def runTest(self, testName):
        return getattr(self, testName)()

    def runs(self, k):
        if k not in self.eg:
            return 
        old = {}
        for key, value in the.items():
            old[key] = value
        
        out = self.runTest(k)
        
        for key, value in old.items():
            value = the[key] 
        msg = ('PASS' if out == True else 'FAIL') 
        print("!!!!!!", msg, k)
        return out or self.err 

    def test_the(self):
        oo(the)
        return True

    def test_sym(self):
        pairs = dict.fromkeys(["a","a","a","a","b","b","c"])
        sym = Sym()
        for key, value in pairs.items():
            sym.add(value)
        mode, entropy = sym.mid(), sym.div()
        entropy = (1000 * entropy) // 1 / 1000
        oo({'mid': mode, 'div': entropy})
        return mode == "a" and 1.37 <= entropy and entropy <= 1.38

    def test_stat(self):
        the={"Separator":","}
        data=Data(the,'../data/input.csv')

        div=lambda col : col.div()
        mid=lambda col : col.mid()


        print('xmid',o(data.stats(2,data.cols.x,mid)))
        print('xdiv',o(data.stats(3,data.cols.x,div)))
        print('ymid',o(data.stats(2,data.cols.y,mid)))
        print('ydiv',o(data.stats(3,data.cols.y,div)))

        return True

    def test_num(self):
        num =Num()
        for i in range(1,101):
            num.add(i)

        mid=num.mid()
        div=num.div()

        print(num,div)

        return (mid>=50 and mid<=52 and div>30.5 and div<32) 

    def test_bignum(self):
        num=Num(the)
        the['nums']=32
        for i in range(1,1001):
            num.add(i)

        oo(num.nums())

        return (32==len(num._has))

    def test_data(self):
        the = {"Seperator":","}
        d = Data('../data/input.csv')
        cols= d.cols
        for i in cols.y:
            oo(i)
        return True

    def test_csv(self):
        def printCsv(row: list, n: int):
            if n > 10:
                return
            else:
                utils.oo(row)
        utils.csv('../data/input.csv', printCsv)
        return True