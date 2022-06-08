import argparse


class ChangeFile:
    def __init__(self, file_name: str):
        self.name = file_name
        self.read_file()
        print('Done!')

    def read_file(self):
        with open(self.name, 'r') as file_r:
            content = file_r.readlines()
        self.filtering(content)

    def save_file(self, mail: str):
        with open(f'email_{args.domain}.txt', 'a') as file_a:
            file_a.writelines(f"{mail}\n")

    def filtering(self, content: str):
        for mail in content:
            if (tmp := mail.split(':')[0]).endswith(f'.{args.domain}'):
                self.save_file(tmp)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('domain', help='domain name')
    args = parser.parse_args()
    ChangeFile('base.txt')
