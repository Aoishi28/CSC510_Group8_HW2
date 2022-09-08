import math

class Sym:
    '''
    Syms summarize as stream of symbols.

    Attributes:
        n: number of items seen
        at: column position
        name: column name
        _has: kept data
    '''

    def __init__(self, c=0, s=""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}


    def add(self, v):
        '''
        Add or increment occurence of sym in dictionary.

        Arguments:
            v: Sym to add/to increment its occurence
        '''
        if v != "?":
            self.n += 1
            self._has[v] = 1 + self._has.get(v, 0)
 

    def mid(self, col="") -> str:
        '''
        Finds the mode of stored values
        '''

        most = -1
        mode = ""
        for v in self._has:
            if (self._has.get(v) > most):
                mode = v
                most = self._has.get(v)
        return mode


    def div(self) -> float:
        '''
        Calculates diversity of store Symbols using entropy
        '''

        def fun(p):
            return p*math.log(p,2)

        e = 0
        for v, n in self._has.items():
            if n > 0:
                e = e-(fun(n/self.n))
        return e