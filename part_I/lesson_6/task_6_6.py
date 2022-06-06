def squares(*args):
    print(type(args))
    print(len(args))
    print(args)
    argv = [int(x) for x in args[0]]
    if len(argv) == 1:
        circle_area = 3.14 * (argv[0] / 2)**0.5
        print('area of a circle is: ', circle_area, ' sq.m')
    elif len(argv) == 2:
        rect_area = argv[0] * argv[1]
        print('area of a rectangle is: ', rect_area, ' sq.m')
    elif len(argv) == 3:
        triangle_area = sum(argv)**2 / (12 * 3**0.5)
        print('area of a triangle is: ', triangle_area, ' sq.m')
    else:
        print('enter correct number')


if __name__ == '__main__':
    squares(input('enter int numbers separated by a space: ').split())


