class Row:

    def __init__(self, t):
        self.cells = t
        self.cooked = copy(t)
        self.isEvalued = False

    