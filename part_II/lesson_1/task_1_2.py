import click


class ChangeFile:
    @click.argument('domain')
    def __init__(self, file_name: str, domain='com'):
        self.name = file_name
        self.domain = domain
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
