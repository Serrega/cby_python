#!/usr/bin/env python3
from random import randint
import animals as an
import rdzogs


def menu(d_animals: dict):
    print('Help:\n')
    print(*['\t' + str(k) + ') ' + v[0]
          for k, v in d_animals.items()], sep='\n')


def user_input(d_animals: dict) -> int:
    while not (num := rdzogs.check_input('\nEnter a number: ', 7)):
        continue
    return num


def view_picture(num: int, d_animals: dict):
    if num == -1:
        print('\nGood Bye!')
    elif num == 7:
        num = randint(1, 6)
        print(d_animals[randint(1, 6)][1])
    else:
        print(d_animals[num][1])


def main():
    list_of_animals = ('deer', 'bat', 'cat', 'cow', 'frog',
                       'butterfly', 'random')
    list_of_pictures = (an.deer, an.bat, an.cat, an.cow, an.frog,
                        an.butterfly, None)
    dict_animals = {i + 1: (list_of_animals[i], list_of_pictures[i])
                    for i in range(7)}
    menu(dict_animals)
    number = user_input(dict_animals)
    view_picture(number, dict_animals)


if __name__ == '__main__':
    main()
