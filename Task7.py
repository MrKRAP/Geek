

class Complex:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __mul__(self):
        print('Вы сделали нечто странное',self.x + self.y)




x = Complex(1+2j,3+1j)
x.__mul__()
