import click


@click.command()
@click.option('-d', '--domain')
class ChangeFile:
    def __init__(self, domain):
        self.name = 'base.txt'
        self.domain = domain
        self.read_file()
        print('Done!')

    def read_file(self):
        with open(self.name, 'r') as file_r:
            content = file_r.readlines()
        self.filtering(content)

    def save_file(self, mail: str):
        with open(f'email_{self.domain}.txt', 'a') as file_a:
            file_a.writelines(f"{mail}\n")

    def filtering(self, content: str):
        for mail in content:
            if (tmp := mail.split(':')[0]).endswith(f'.{self.domain}'):
                self.save_file(tmp)


if __name__ == '__main__':
    ChangeFile()
