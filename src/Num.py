import math
import random
from src.utils import *

class Num:
    '''
        Num summarizes as stream of numbers
        Attributes:
            n: number of items seen
            at: column position
            name: column name
            _has: kept data
            lo: lowest seen
            hi: highest seen
            isSorted: tracks the status of sort
            c: column position
            s: column name
        '''
    def __init__(self,the, c=0, s=""):
        self.n=0
        self.at = c
        self.name = s
        self.lo= math.inf
        self.hi = - math.inf
        self._has = {}
        self.isSorted  = False
        self.w = 1 if (s or "").find("-$") == -1 else -1
        self.the = the
        # random.seed(self.the['seed'])
        
        
    def nums(self) -> dict:
        if not self.isSorted:
            self._has = dict(zip(range(1, len(self._has)+1), sorted(self._has.values())))
            self.isSorted = True
        return self._has

    def add(self,v):

        '''
                Reservoir Sample to keep at most 'the.nums' numbers.Incase of no space, it deletes something old, at random
                Arguments:
                    v: Num to perform the above operation
        '''

        pos = -1
        global the
        if v != "?":
            self.n = self.n + 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if len(self._has) < self.the['nums']:
                pos = 1 + (len(self._has))
            elif random.random()< (self.the['nums'] / self.n):
                pos = random.randint(1, len(self._has))
            if pos != -1:
                self.isSorted = False
                self._has[pos] = v


    def div(self):
        '''
                        Computes diversity(standard deviation for Nums)
        '''
        a = self.nums()
        return (self.per(a,0.9)-self.per(a,0.1))/2.58


    def mid(self):
        '''
                        Computes central tendency (Median for Nums)
        '''
        return self.per(self.nums(),0.5)

