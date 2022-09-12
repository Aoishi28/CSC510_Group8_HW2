
from src.utils import *

def TestCsv( row: list, n: int):

    if n > 10:
        return
    else:
        oo(row)

def csv_read():

    csv('../data/input.csv', TestCsv)
    return True