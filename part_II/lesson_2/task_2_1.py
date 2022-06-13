import os


if __name__ == '__main__':
    print('Права текущей директории: ')
    print(os.system('ls -noad | cut -f1 -d" "'))
