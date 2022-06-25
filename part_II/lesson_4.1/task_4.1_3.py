import re


with open('surnames.txt', 'r', encoding='utf-8') as file_r, \
        open('man.txt', 'w', encoding='utf-8') as man_w, \
        open('woman.txt', 'w', encoding='utf-8') as woman_w:
    for line in file_r.readlines():
        #if re.match(r'.*ВА$|.*НА$|.*АЯ$', line):
        if re.match(r'(.*ВА|.*НА|.*АЯ)$', line):
            writer = woman_w
        else:
            writer = man_w
        writer.write(line.title())

print('Done!')
