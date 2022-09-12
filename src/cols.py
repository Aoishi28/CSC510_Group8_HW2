import re

class Cols:
    '''
    Columns holds summaries of columns

    Attribures:
        names: all column names
        all: all columns
        klass: single dependent klass column (if exists)
        x: independent columns that are not skipped
        y: dependent columns that are not skipped
    '''

    def __int__(self, names):
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []

        for cNum, cName in self.names():

            isNumeric = re.search(r'^[A-Z]*', cName)        # Numeric columns begin with an uppercase letter
            col = Num(cNum,cName) if isNumeric else Sym(cNum,cName)
            all.append(col)

            if not ":" in cName:                            # Checking for skipped columns (skipped columns contain a trailing ':')
                isDependent = re.search(r'[!+-]', cName)
                if isDependent:
                    y.append(col)
                else:
                    x.append(col)
                if "!" in cName:                            # single dependent klass column
                    self.klass = col




