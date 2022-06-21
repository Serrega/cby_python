import re

if __name__ == '__main__':
    with open('job.txt', 'r', encoding='utf-8') as file_r:
        for line in file_r.readlines():
            res = re.search(r'[К-С].{5}к', line)
            if res:
                print(res.group())

