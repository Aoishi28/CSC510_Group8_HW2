
from src import utils

def TestCsv( row: list, n: int):

    if n > 10:
        return
    else:
        utils.oo(row)

def csv_read():

    utils.csv('../data/input.csv', TestCsv)
    return True