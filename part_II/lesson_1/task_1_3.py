import argparse


class Phone:
    def __init__(self, file_name: str):
        self.name = file_name
        parser = argparse.ArgumentParser()
        parser.add_argument('finds', help='finding parameters')
        args = parser.parse_args()
        self.finds = args.finds
        self.find_str()
        self.print_phone()

    def find_str(self):
        with open(self.name, 'r', encoding='utf-8') as file_r, \
                open('phones.txt', 'w', encoding='utf-8') as file_w:
            for string in file_r.readlines():
                if '-' in string:
                    data = string.split()
                    if self.finds in data:
                        file_w.writelines(f"{data[0].title()} {' '.join(data[1:4])}\n")

    def print_phone(self):
        with open('phones.txt', 'r', encoding='utf-8') as file_r:
            content = file_r.readlines()
            print(f'Найдено {len(content)} записей\n')
            for line in content:
                print(line, end='')


if __name__ == '__main__':
    p = Phone('phonebook_al.txt')
