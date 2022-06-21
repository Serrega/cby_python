#!/usr/bin/env python3
import re


def check(text: str):
    if re.match(r'(?=.*[_])(?=.*[\d])(?=.*\w{6,})(?=.*^[A-Z])(?=.*[^_]$)(?!.*[\W])', text):
        print('Password accepted!')
    else:
        print('The password does not match the requirements!')


if __name__ == '__main__':
    check(input('Enter password: '))

'''
r'^[A-Z](?=.*[0-9])(?=.*[_])(?=.*[a-z])\w{8,20}[a-z0-9]$'
'''