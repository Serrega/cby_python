#!/usr/bin/env python3
from random import randint
import rdzogs


def main():
    while not (num := rdzogs.check_input('Enter a number: ', 10)):
        continue
    if num == -1:
        print('\nGood Bye!')
        return False
    rand_num = randint(10, 100)
    print('rand number: ', rand_num)
    p = sum([x if rand_num > num else 20 for x in range(num, rand_num + 1)])
    print('summa of numbers: ', p)


if __name__ == '__main__':
    main()
