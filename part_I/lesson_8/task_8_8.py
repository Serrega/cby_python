#!/usr/bin/env python3
from colorama import Fore
from colorama import init
import signal
import sys
import vlc


def handler(x, y):
    print(Fore.LIGHTMAGENTA_EX + "\nBang! Bang!!!")
    sys.exit()


def start_alarm():
    p = vlc.MediaPlayer("alarm.mp3")
    p.play()
    try:
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(30)
    except AttributeError:
        print('Start this code on Linux')
        sys.exit()


def check_code(code: str) -> bool:
    if code == 'swordfish':
        print(Fore.LIGHTGREEN_EX + '\nSelf-destruct operation cancelled!\n')
        return True
    else:
        print(Fore.LIGHTRED_EX + '\nCode not accepted!')
        return False


def user_input():
    try:
        chek = check_code(input(Fore.LIGHTGREEN_EX))
    except(EOFError, KeyboardInterrupt) as eo:
        print('\nEOF or Interrupt - ', eo)
        sys.exit()
    else:
        if chek:
            signal.alarm(0)
            return True


def main():
    init(autoreset=True)
    print(Fore.LIGHTRED_EX +
          '\nATTENTION! The self-destruct mechanism has been launched!')
    start_alarm()
    for _ in range(3):
        print('\nEnter the code to cancel the self-destruct operation: ', end='')
        if user_input():
            return True

    print(Fore.LIGHTMAGENTA_EX + "\nBang! Bang!!!")


if __name__ == '__main__':
    main()
