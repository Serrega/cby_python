from lorem_text import lorem
from colorama import Fore
import random
import time


def time_count():
    for i in range(3, 0, -1):
        print(i, '... ', sep='', end='')
        time.sleep(1)
    print(Fore.RED + 'Start!' + '\n')


def user_input(text: str):
    start_time = time.time()
    if input('Input text above: ') == text:
        statistic(len(text), time.time() - start_time)
        return True
    else:
        if input(Fore.YELLOW + 'You are mistake! '
                 'Do you want to start again? (y/n)' + Fore.RESET) in 'nN':
            print('Good Bye!')
            return True


def statistic(len_text: int, user_time: float):
    print(Fore.GREEN + '#'*30)
    print(' You are great! '.center(30, '#'))
    print(f' Your time: {round(user_time, 2)} sec '.center(30, '#'))
    print(f' Your speed: {round(len_text/user_time, 2)} sec '.center(30, '#'))
    print('#'*30)


def main():
    while True:
        time_count()
        random_text = lorem.words(random.randint(5, 15))
        print(Fore.GREEN + random_text + Fore.RESET + '\n')
        if user_input(random_text):
            break
        else:
            continue


if __name__ == '__main__':
    main()
