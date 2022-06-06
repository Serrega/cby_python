#!/usr/bin/env python3
from time import sleep
import sys
import rdzogs


def main():
    try:
        while not rdzogs.check_input(number := input('\nEnter a number: '), 30):
            pass
    except(EOFError, KeyboardInterrupt) as eo:
        print('\nEOF or Interrupt - ', eo)
        sys.exit()
    except BaseException as be:
        # for Ctrl+C in PyCharm in Windows
        print('\nBaseException - ', be)
        sys.exit()
    else:
        for i in range(int(number), -1, -1):
            print(str(i) + ' ', end='\r')
            sleep(1)


if __name__ == '__main__':
    main()

