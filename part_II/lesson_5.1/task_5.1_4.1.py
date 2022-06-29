from multiprocessing import Pool
import time


def soldier(p):
    time.sleep(1)
    print(str(p)+' ', end='')


if __name__ == '__main__':
    for i in range(1,6):
        print(f'Курсант {i} начал снаряжать магазин')
        with Pool(1) as p:
            x = p.map(soldier, range(1, 31))
        print(f'\nКурсант {i} снарядил магазин\n')


