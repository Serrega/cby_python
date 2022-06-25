import re

if __name__ == '__main__':
    with open('proxy.txt', 'r') as file_r:
        for line in file_r.readlines():
            res = re.match(r'(?:\d{,3}\.){3}\d{,3}', line)
            print(res.group())

