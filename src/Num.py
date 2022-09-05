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

    def per(self, t, p):

        '''
                        Return the pth item from the sorted list 't'
                        Arguments:
                            p: Denotes index
                            t: Denotes sorted list
        '''
        p = math.floor(((p or 0.5) * len(t)) + 0.5)
        return t[math.max(1, math.min(len(t), p))]


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

    def o(self,t):
        '''
                        Generates a string from nested list
                        Arguments:
                            t: Denotes list of values
        '''

        if type(t) != list:
            return str(t)

        def show(self,k, v):
            if str(k).find('^_') == -1:
                v = self.o(v)
                return len(t) == 0 and format(':{} {}', k, v) or str(v)

        u = []
        index = 0
        dict_keys = list(t.keys())
        for key in dict_keys:
            u[index] = show(key, t[key])
        if len(t) == 0:
            u.sort()
        return '{' + ' '.join(str(item) for item in u) + '}'

    def oo(self,t):
        '''
                        Prints the string from o()
                        Arguments:
                            t: Denotes list of values
        '''
        print(self.o(t))
        return t