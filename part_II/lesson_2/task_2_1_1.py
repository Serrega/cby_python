import os
import stat


def calc(ch):
    mod = {0: '---', 1: '--x', 2: 'r--', 3: 'r-x', 4: '-w-', 5: '-wx', 6: 'rw-', 7: 'rwx'}
    res = []
    if len(ch) == 3:
        for dig in ch:
          res.append(mod[int(dig)])
    print(f'Права текущей директории: {"".join(res)}')


if __name__ == '__main__':
    cwd = os.getcwd()
    calc(oct(stat.S_IMODE(os.lstat(cwd).st_mode))[2:])

