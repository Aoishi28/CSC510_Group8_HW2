# `Data` is a holder of `rows` and their sumamries (in `cols`).
from audioop import add
from utils import csv, rnd, push
from row import Row
from cols import Cols

class Data:
    def __init__(self, src):
        self.cols = None # summaries of data
        self.rows = []  # kept data
        if   type(src) == "string":
            csv(src, add(row)) 
        else:
            for row in(src or {}):
                self.add(row)
        pass
    
    def add(self, xs):
        if   not self.cols:
            self.cols = Cols(xs) 
        else:
            row = Row(xs) if type(xs) == list else xs # ensure xs is a Row
            self.rows.append(row)
            for todo in [self.cols.x, self.cols.y]:
                for col in (todo):
                    col.add(row.cells[col.at]) 
        
    def stats(self, places, showCols, fun, t=None, v=None):
        showCols, fun = showCols or self.cols.y, fun or "mid"
        t={} 
        for col in showCols: 
            v=fun(col)
            v=type(v)=="number" and rnd(v,places) or v
            t[col.name]=v 
        return t 
        