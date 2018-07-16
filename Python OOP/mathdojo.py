class  MathDojo(int):
    """docstring for MathDojo."""
    def __init__(self, add, subtract):
        self.add = add
        self.subtract = subtract
    def __add__(self,other):
        self.__add__(self,other)
        return self


    def __sub__(self,other):
        self.__sub__(self,other)
        return self


md = MathDojo(2+5)

md.add().add().subtract().result
