
# -- `Row` holds one record
from src.utils import copy

class Row:

    def __init__(self, t):
        self.cells = t                      # -- one record
        self.cooked = copy(t)               # -- used if we discretize data
        self.isEvalued = False              # -- true if y-values evaluated

