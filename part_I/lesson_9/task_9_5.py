woman = ('ва\n', 'на\n', 'ая\n')
with open('surnames.txt', 'r', encoding='utf-8') as file_r, \
        open('woman.txt', 'a', encoding='utf-8') as woman_a, \
        open('man.txt', 'a', encoding='utf-8') as man_a:
    for line in file_r.readlines():
        line = line.title()
        if line.endswith(('ва\n','на\n','ая\n')):
            woman_a.writelines(line)
        else:
            man_a.writelines(line)
