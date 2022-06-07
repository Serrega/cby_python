import argparse


class ChangeFile:
    def __init__(self, file_name: str):
        self.name = file_name
        parser = argparse.ArgumentParser()
        parser.add_argument('domain', help='domain name')
        args = parser.parse_args()
        self.domain = args.domain
        self.new_file()
        print('Done!')

    def new_file(self):
        with open(self.name, 'r') as file_r, \
                open(f'email_{self.domain}.txt', 'a') as file_a:
            for mail in file_r.readlines():
                if f'.{self.domain}:' in mail:
                    file_a.writelines(f"{mail[:mail.index(':')]}\n")


if __name__ == '__main__':
    p = ChangeFile('base.txt')
