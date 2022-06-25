import re


class ChangeFile:
    def __init__(self):
        self.name = 'base.txt'
        self.read_file()
        print('Done!')

    def read_file(self):
        with open(self.name, 'r') as file_r:
            content = file_r.readlines()
        self.filtering_login(content)
        self.filtering_domain(content)
        self.filtering_pass(content)

    def save_file(self, content, name):
        with open(f'{name}.txt', 'a') as file_a:
            file_a.writelines(f"{content}\n")

    def filtering_login(self, content):
        for line in content:
            if (tmp := re.match(r'^[\w\.-]+', line)):
                self.save_file(tmp.group(), 'login')

    def filtering_domain(self, content):
        for line in content:
            if (tmp := re.search(r'(?<=@)[\w.-]+', line)):
                self.save_file(tmp.group(), 'domain')

    def filtering_pass(self, content):
        for line in content:
            if (tmp := re.search(r'(?<=:)[\w.-]+', line)):
                self.save_file(tmp.group(), 'password')


if __name__ == '__main__':
    ChangeFile()
