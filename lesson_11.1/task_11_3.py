class Ellipse:
    def __init__(self, half_axis1, half_axis2):
        self.x = half_axis1
        self.y = half_axis2

    @staticmethod
    def count(x, y):
        res = 3.14*x*y
        print(f'Площадь эллипса: {res:.2f}')


class Cone:
    def __init__(self, height, radius):
        self.h = height
        self.r = radius

    @staticmethod
    def count(h, r):
        res = 3.14*h*r**2/3
        print(f'Объем конуса: {res:.2f}')


if __name__ == '__main__':
    try:
        half_axis_1 = float(input('Вычисление площади эллипса\nвведите полуось 1: '))
        half_axis_2 = float(input('введите полуось 2: '))
        assert half_axis_1 > 0 and half_axis_2 > 0
    except (ValueError, AssertionError):
        print('\nВведите корректные данные')
    else:
        Ellipse.count(half_axis_1, half_axis_2)
        try:
            height = float(input('\nВычисление объема конуса\nвведите высоту: '))
            radius = float(input('введите радиус: '))
            assert height > 0 and radius > 0
        except (ValueError, AssertionError):
            print('\nВведите корректные данные')
        else:
            Cone.count(height, radius)