import argparse


class Phone:
    def __init__(self):
        self.name = 'phonebook_al.txt'
        self.read_file()

    def read_file(self):
        with open(self.name, 'r', encoding='utf-8') as file_r:
            content = file_r.readlines()
        self.filtering(content)

    def save_file(self, data: list):
        with open('phones.txt', 'a', encoding='utf-8') as file_a:
            file_a.writelines(f"{data[0].title()} {' '.join(data[1:])}\n")

    def filtering(self, content: str):
        for string in content:
            if '-' in string:
                data = string.split()
                if args.finds in data:
                    if '@' in data[-1]:
                        data.pop()
                    self.save_file(data)
        self.print_phone()

    def print_phone(self):
        with open('phones.txt', 'r', encoding='utf-8') as file_r:
            content = file_r.readlines()
            print(f'Найдено {len(content)} записей\n')
            for line in content:
                print(line, end='')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('finds', help='finding parameters')
    args = parser.parse_args()
    Phone()
