#!/usr/bin/env python3
from multiprocessing import Pool
import time


def func(y):
    time.sleep(1)
    print(str(y)+' ', end='\r')


if __name__ == '__main__':
    print('Старт!')
    with Pool(1) as p:
        x = p.map(func, range(10, 0, -1))
    print('Время вышло!')





