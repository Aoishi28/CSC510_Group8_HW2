import math
import random
class Num:
    '''
        Num summarize as stream of numbers
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
    def __int__(self,c,s):
        self.n=0
        self.at = c if c else 0
        self.name = s if s else ""
        lo= math.inf
        high = - math.inf
        self._has = {}
        self.isSorted  = False

    def nums(self):
        if not self.isSorted:
            self._has =sorted(self._has.items())
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
            self.lo = math.min(v, self.lo)
            self.hi = math.max(v, self.hi)
            if len(self._has) < the['nums']:
                pos = 1 + (len(self._has))
            elif random.randint(0,1)< (the['nums'] / self.n):
                pos = random.randint(1, len(self._has))
            if pos:
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

