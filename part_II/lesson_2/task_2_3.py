import argparse
import os
from pathlib import Path
import stat


def system_bash():
    while (command := input('Shell command: ')) != 'exit':
        if os.system(command):
            print('Wrong command, exit!')
            return False
    print('The work was completed!')


def system_chmod():
    while (path := input('Enter the path: ')) != 'exit':
        try:
            print(oct(stat.S_IMODE(os.lstat(path).st_mode))[2:])
        except FileNotFoundError:
            print('The file or directory does not exist!')
    print('The work was completed!')


def tree(dir_path: Path, prefix: str=''):
    """A recursive generator, given a directory Path object
    will yield a visual tree structure line by line
    with each line prefixed by the same characters
    """
    # prefix components:
    space = '    '
    branch = '│   '
    # pointers:
    tee = '├── '
    last = '└── '
    contents = list(dir_path.iterdir())
    # contents each get pointers that are ├── with a final └── :
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name
        if path.is_dir(): # extend the prefix and recurse:
            extension = branch if pointer == tee else space
            # i.e. space because last, └── , above so no more |
            yield from tree(path, prefix=prefix+extension)


def save_file(name: str, string: str):
    with open(name, 'a') as file_a:
        file_a.writelines(f'{string}\n')


def system_tree():
    while (path := input('Enter the path: ')) != 'exit':
        # deleted prevision version file
        file_split = path.split('/')[-2]
        file_name = f'wood_{file_split}'
        if os.path.exists(file_name):
            os.system(f'rm {file_name}')
        print('.')
        save_file(file_name, '.')
        try:
            for p in tree(Path(path)):
                print(p)
                save_file(file_name, p)
        except FileNotFoundError:
            print('The file or directory does not exist!')
        except PermissionError:
            print('Permission denied')
    print('The work was completed!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--system', help='')
    parser.add_argument('-c', '--chmod', help='')
    parser.add_argument('-t', '--tree', help='')
    args = parser.parse_args()
    print('args', args)
    if args.system:
        system_bash()
    if args.chmod:
        system_chmod()
    if args.tree:
        system_tree()
