from colorama import Fore
from random import randint


def print_res(num_1: int, num_2: int, win=False):
    stat = {'Dima': num_1, 'Vova': num_2}
    if win:
        print(Fore.GREEN)
        win_text = ' You winner!' + Fore.RESET
    else:
        win_text = ''
    p = sorted(stat.items(), key=lambda x: x[1], reverse=True)
    print(f"Gambler {p[0][0]} scored {p[0][1]:0>2} points.{win_text}")
    print(f"Gambler {p[1][0]} scored {p[1][1]:0>2} points.")


if __name__ == '__main__':
    while (coob_1 := randint(2, 12)) == (coob_2 := randint(2, 12)):
        print_res(coob_1, coob_2)
    print_res(coob_1, coob_2, True)
