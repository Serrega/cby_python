#!/usr/bin/env python3
from random import randint
import rdzogs


def check_num(num: int, rand_n: int):
    if num == rand_n:
        print('You won!')
        return True
    elif num > rand_n:
        print('Your number is greater\n')
    elif num < rand_n:
        print('Your number is less\n')


def main():
    rand_num = randint(1, 10)
    # print(rand_num)
    for _ in range(3):
        num = rdzogs.check_input('Guess the number: ', 10, ret_non_diap=1)
        if num == -1:
            print('\nGood Bye!')
            break
        if check_num(num, rand_num):
            return True
    print('Luck is not on your side, try again!')


if __name__ == '__main__':
    main()
