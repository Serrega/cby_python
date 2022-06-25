import re


class ChangeFile:
    def __init__(self):
        self.name = 'base.txt'
        self.login = set()
        self.domain = set()
        self.password = set()
        self.read_file()
        self.save_file()
        print('Done!')

    def read_file(self):
        with open(self.name, 'r') as file_r:
            content = file_r.readlines()
        self.filtering(content)

    def save_file(self):
        with open(f'login.txt', 'a') as login_a, \
                open(f'domain.txt', 'a') as domain_a, \
                open(f'password.txt', 'a') as password_a:
            for string in zip(self.login, self.domain, self.password):
                login_a.writelines(f"{string[0]}\n")
                domain_a.writelines(f"{string[1]}\n")
                password_a.writelines(f"{string[2]}\n")

    def filtering(self, content):
        for line in content:
            if (tmp := re.findall(r'^(.*?)@(.*?):(.*)', line)):
                self.save_set(*tmp)

    def save_set(self, content):
        self.login.add(content[0])
        self.domain.add(content[1])
        self.password.add(content[2])


if __name__ == '__main__':
    ChangeFile()
