#!/usr/bin/env python3
import string


def check_first_letter(letter: str) -> bool:
    if not (letter in string.ascii_uppercase):
        print('The first character must be capitalized english letter')
        return False
    return True


def check_last_letter(letter: str) -> bool:
    if not (letter in (string.digits + string.ascii_letters)):
        print('The last character must be a english letter or number')
        return False
    return True


def check_len(text: str) -> bool:
    if not 8 <= len(text) <= 20:
        print('password length must be between 8 and 20 characters')
        return False
    return True


def check_alnum_and_underline(text: str) -> bool:
    symbols = string.digits + string.ascii_letters + '_'
    if not all([letter in symbols for letter in text]):
        print('Password must contian only english letters, '
              'digits and underline')
        return False
    return True


def check_underline(text: str) -> bool:
    if not ('_' in text[1:-1]):
        print('Password must contain an underline')
        return False
    return True


def check_digits(text: str) -> bool:
    if not any((letter in string.digits for letter in text[1:])):
        print('Password must contain a digit')
        return False
    return True


if __name__ == '__main__':
    passw = input('Enter password: ')
    check = all([check_first_letter(passw[0]),
                 check_last_letter(passw[-1]),
                 check_len(passw),
                 check_underline(passw),
                 check_digits(passw),
                 check_alnum_and_underline(passw)])
    if check:
        print('Password accepted!')
    else:
        print('The password does not match the requirements!')
