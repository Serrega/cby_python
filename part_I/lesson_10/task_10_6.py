import calendar
from colorama import Fore


def save_year(year: int):
    with open('calendar.txt', 'w') as file_w:
        file_w.write(calendar.calendar(year))


def print_month(num_str: int):
    print(Fore.GREEN + content[num_str] + Fore.RESET, end='')


def print_days(num_str: int):
    days = content[num_str].split()
    for day in days:
        if day == 'Sa':
            print(Fore.RED, end='')
        print(day, end=' ')
        if day == 'Su':
            print(Fore.RESET, end=' '*5)


def print_nums(starts: int, ends: int):
    print('\n', *content[starts:ends], end='')


if __name__ == '__main__':
    save_year(2022)
    with open('calendar.txt', 'r') as file_r:
        content = file_r.readlines()
    print(Fore.GREEN + content[0])
    print_month(2)
    print_days(3)
    print_nums(4, 9)
    print()
    print_month(11)
    print_days(12)
    print_nums(13, 19)
