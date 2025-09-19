class Spreadsheet:

    def __init__(self, rows: int):
        self.a={}

    def setCell(self, cell: str, value: int) -> None:
        if cell not in self.a:
            self.a[cell]=value
        else:
            self.a[cell]=value

    def resetCell(self, cell: str) -> None:
        self.a[cell]=0

    def getValue(self, formula: str) -> int:
        x,y=formula[1:].split('+')
        if x.isdigit():
            x=int(x)
        else:
            if x in self.a:
                x=self.a[x]
            else:
                x=0
        if y.isdigit():
            y=int(y)
        else:
            if y in self.a:
                y=self.a[y]
            else:
                y=0
        return x+y


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)