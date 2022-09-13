from src.data import Data
from src.utils import *

def TestStat():
    the={"Separator":","}
    data=Data(the,'../data/input.csv')

    div=lambda col : col.div()
    mid=lambda col : col.mid()


    print('xmid',o(data.stats(2,data.cols.x,mid)))
    print('xdiv',o(data.stats(3,data.cols.x,div)))
    print('ymid',o(data.stats(2,data.cols.y,mid)))
    print('ydiv',o(data.stats(3,data.cols.y,div)))

    return True
