class Trapezoid:
    def __init__(self, d1, d2, h):
        self.d1 = d1
        self.d2 = d2
        self.h = h

    def area(self):
        len1 = self.d1**2 - self.h**2
        len2 = self.d2**2 - self.h**2
        if len1 < 0 or len2 < 0:
            print('\nTrapezoid not existence, enter correct parameters')
            return False
        return self.h*(len1**0.5 + len2**0.5)/2


diag1 = int(input('Enter diagonale 1: '))
diag2 = int(input('Enter diagonale 2: '))
height = int(input('Enter height:'))
trip = Trapezoid(diag1, diag2, height)
print(f'\nArea of trapezoid is {trip.area():.2f}')
