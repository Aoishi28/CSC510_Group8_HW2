from src.Data import Data
from src.utils import *

def DataTest():
    the = {"Seperator":","}
    d = Data(the, '../data/input.csv')
    cols= d.cols
    for i in cols.y:
        oo(i)
    return True
